# Movimento Médio Diário de Passageiros no Município do Rio de Janeiro (1995–2025)

## Identificação Acadêmica
* **Instituição:** [Nome da Instituição]
* **Curso:** Bacharelado em Sistemas de Informação — 6º Período
* **Disciplina:** Linguagem de Programação (Análise e Visualização de Dados com Python)
* **Autores:** [Nome do Aluno 1], [Nome do Aluno 2], [Nome do Aluno 3]
* **Artigo Interativo (GitHub Pages):** `https://<seu-usuario>.github.io/<nome-do-repositorio>/`

---

## Resumo Executivo
Este projeto investiga a evolução do movimento médio diário de passageiros nos sistemas de transporte rodoviário (ônibus), ferroviário (metrô, trem e bonde), hidroviário e aeroviário no Município do Rio de Janeiro ao longo de 31 anos (1995–2025). Utilizando um pipeline determinístico em Python aderente aos princípios **FAIR** (*Findable, Accessible, Interoperable, Reusable*), o estudo analisa a transição estrutural da matriz modal entre pneus e trilhos, o impacto do ciclo dos megaeventos (2011–2016) e a retração assimétrica causada pela pandemia de COVID-19 (2020–2025).

**Palavras-chave:** Mobilidade Urbana; Transporte Público; Rio de Janeiro; Análise Exploratória de Dados; Ciência Aberta (FAIR).

---

## Fonte Original dos Dados (Proveniência)
* **Conjunto de Dados:** Tabela 728 — *Movimento médio diário de passageiros, segundo os transportes rodoviário, ferroviário, hidroviário e aeroviário no Município do Rio de Janeiro entre 1995-2025*
* **Portal Oficial:** [Data.Rio — Instituto Pereira Passos (IPP) / Prefeitura do Rio de Janeiro](https://www.data.rio/)
* **Fontes Primárias Consolidadas:** SMTU, Metrô-RJ / Opportrans / MetrôRio, Flumitrens / SuperVia, TRANSTUR / Barcas S.A. / CONERJ e INFRAERO.

---

## Perguntas de Pesquisa (RQs)
1. **RQ1 (Transição da Matriz Modal):** Como a participação relativa (*modal share*) entre o transporte rodoviário (ônibus) e os sistemas sobre trilhos (metrô e trem) se reconfigurou entre 1995 e 2025?
2. **RQ2 (Choque e Recuperação Pós-Pandemia):** Qual foi a magnitude da retração provocada pela pandemia de COVID-19 (2020–2021) em cada modal e quais sistemas recuperaram os patamares pré-pandemia (2019) até 2025?
3. **RQ3 (Ciclo de Megaeventos vs. Demanda Estrutural):** De que maneira o ciclo de investimentos dos megaeventos (2011–2016) alterou a trajetória de crescimento dos passageiros diários em comparação com a década seguinte (2017–2025)?

---

## Estrutura do Repositório
```text
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   └── 728.xls
│   ├── processed/
│   │   ├── passageiros_rio_1995_2025.parquet
│   │   └── passageiros_rio_1995_2025.csv.gz
│   └── data_dictionary.md
├── notebooks/
│   └── analise_exploratoria.ipynb
├── src/
│   ├── __init__.py
│   └── etl.py
└── docs/
    ├── index.html
    └── assets/
