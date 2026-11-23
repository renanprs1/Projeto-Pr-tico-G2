from pathlib import Path
import pandas as pd

RAW_FILE = Path("data/raw/728.xls")
PROCESSED_DIR = Path("data/processed")
PARQUET_OUT = PROCESSED_DIR / "passageiros_rio_1995_2025.parquet"
CSV_GZ_OUT = PROCESSED_DIR / "passageiros_rio_1995_2025.csv.gz"
CSV_OUT = PROCESSED_DIR / "passageiros_rio_1995_2025.csv"

MODAL_COLS = [
    "onibus_mil",
    "metro_mil",
    "trem_mil",
    "bonde_mil",
    "hidroviario_mil",
    "aeroviario_mil",
]


def extract_raw(filepath: Path = RAW_FILE) -> pd.DataFrame:
    if not filepath.exists():
        raise FileNotFoundError(f"Arquivo bruto não encontrado: {filepath}")

    df_raw = pd.read_excel(
        filepath,
        sheet_name="T 728",
        skiprows=8,
        nrows=31,
        header=None,
    )
    df_raw.columns = ["ano", *MODAL_COLS]
    return df_raw


def transform_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    df = df_raw.copy()

    df["ano"] = pd.to_numeric(df["ano"], errors="raise").astype("int64")

    for col in MODAL_COLS:
        # Converte marcadores textuais como '...' (bonde 2012-2014) em NaN rastreável
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("float64")

    if not df["ano"].is_monotonic_increasing or df["ano"].nunique() != 31:
        raise ValueError("Validação falhou: a série temporal deve conter 31 anos únicos ordenados.")

    df["ferroviario_total_mil"] = df[["metro_mil", "trem_mil", "bonde_mil"]].sum(
        axis=1, min_count=1
    )
    df["total_geral_mil"] = df[MODAL_COLS].sum(axis=1, min_count=1)

    for col in MODAL_COLS:
        modal_name = col.removesuffix("_mil")
        df[f"share_{modal_name}_pct"] = (df[col] / df["total_geral_mil"]) * 100.0

    df["share_ferroviario_pct"] = (
        df["ferroviario_total_mil"] / df["total_geral_mil"]
    ) * 100.0

    base_2019 = df.loc[df["ano"] == 2019].iloc[0]
    for col in [*MODAL_COLS, "total_geral_mil"]:
        series_name = col.removesuffix("_mil")
        df[f"idx_2019_{series_name}"] = (df[col] / base_2019[col]) * 100.0

    return df


def load_processed(df: pd.DataFrame) -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_parquet(PARQUET_OUT, index=False)
    df.to_csv(CSV_GZ_OUT, index=False, compression="gzip", float_format="%.6f")
    df.to_csv(CSV_OUT, index=False, float_format="%.4f")


def run_pipeline() -> pd.DataFrame:
    df_raw = extract_raw()
    df_processed = transform_data(df_raw)
    load_processed(df_processed)
    return df_processed


if __name__ == "__main__":
    result = run_pipeline()
    print(f"Pipeline concluído com sucesso: {result.shape[0]} linhas x {result.shape[1]} colunas.")
    print(f"Arquivos gerados: {PARQUET_OUT}, {CSV_GZ_OUT} e {CSV_OUT}")
