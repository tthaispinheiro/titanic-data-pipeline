# Titanic Data Pipeline

## Sobre o projeto

Este projeto consiste na construção de um pipeline básico de Engenharia de Dados utilizando Python e Pandas.

O objetivo é realizar o processamento do dataset Titanic, passando pelas etapas de leitura dos dados, tratamento de valores ausentes, remoção de duplicidades, padronização, transformação, validação da qualidade dos dados e exportação de uma base processada.

O projeto também possui um notebook de Análise Exploratória de Dados (EDA), utilizado para compreender a estrutura e a qualidade dos dados antes da implementação do pipeline.

## Fonte dos dados

Os dados utilizados neste projeto foram obtidos a partir do dataset **Titanic**, disponível na plataforma Kaggle.

O dataset contém informações sobre os passageiros do Titanic, incluindo dados como idade, sexo, classe da passagem, tarifa, familiares a bordo, porto de embarque e informação sobre sobrevivência.

Fonte: https://www.kaggle.com/datasets/amineipad/titanic-dataset


## Objetivo

Desenvolver um pipeline simples de processamento de dados para praticar conceitos fundamentais de Engenharia de Dados, incluindo:

* Ingestão de dados
* Análise exploratória
* Qualidade de dados
* Tratamento de valores ausentes
* Remoção de registros duplicados
* Padronização de dados
* Transformação de dados
* Criação de novas variáveis
* Validação dos dados
* Exportação de dados processados

## Tecnologias utilizadas

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook

## Estrutura do projeto

```text
titanic-data-pipeline/
│
├── data/
│   ├── raw/
│   │   └── train.csv
│   │
│   └── processed/
│       └── titanic_processed.csv
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── src/
│   └── pipeline.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Fluxo do pipeline

```text
Dados brutos
    ↓
Leitura dos dados
    ↓
Padronização das colunas
    ↓
Remoção de duplicados
    ↓
Tratamento de valores nulos
    ↓
Padronização de dados categóricos
    ↓
Criação de novas variáveis
    ↓
Validação da qualidade
    ↓
Dados processados
```

## Transformações realizadas

O pipeline realiza as seguintes transformações:

### Padronização dos nomes das colunas

Os nomes das colunas são convertidos para letras minúsculas e algumas colunas são renomeadas para melhorar a legibilidade.

Exemplos:

* `PassengerId` → `passenger_id`
* `Pclass` → `passenger_class`
* `SibSp` → `siblings_spouses`
* `Parch` → `parents_children`

### Tratamento de valores ausentes

* Os valores ausentes da coluna `Age` são preenchidos utilizando a mediana.
* Os valores ausentes da coluna `Embarked` são preenchidos utilizando o valor mais frequente.
* A coluna `Cabin` é removida devido à grande quantidade de valores ausentes.

### Registros duplicados

O pipeline verifica a existência de registros duplicados e realiza a remoção quando necessário.

### Padronização de dados categóricos

Os dados das colunas categóricas são padronizados para evitar inconsistências.

### Criação de novas variáveis

São criadas duas novas colunas:

* `family_size`: representa o tamanho da família do passageiro.
* `age_group`: classifica os passageiros em grupos de idade:

  * `child`
  * `adult`
  * `senior`

## Validações de qualidade

Após o processamento, o pipeline realiza validações para verificar:

* Existência de valores nulos
* Existência de registros duplicados
* Valores negativos na coluna `age`
* Valores negativos na coluna `fare`

Caso alguma inconsistência seja encontrada, o pipeline gera um erro para impedir que dados inválidos sejam considerados como saída final.

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/tthaispinheiro/titanic-data-pipeline
```

### 2. Acesse a pasta do projeto

```bash
cd titanic-data-pipeline
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o pipeline

```bash
python src/pipeline.py
```

## Resultado

Após a execução, o pipeline gera o arquivo:

```text
data/processed/titanic_processed.csv
```

O arquivo contém os dados tratados e transformados, prontos para análises posteriores.

## Próximos passos

Possíveis melhorias futuras para o projeto:

* Adicionar testes automatizados
* Implementar logging
* Adicionar validações mais avançadas de qualidade de dados
* Utilizar um banco de dados como camada de armazenamento
* Orquestrar o pipeline utilizando ferramentas como Apache Airflow
* Containerizar a aplicação com Docker

## Autor

Projeto desenvolvido por Thais Pinheiro como parte dos estudos e projetos práticos em Engenharia de Dados.
