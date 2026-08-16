from pathlib import Path

import pandas as pd


# CONFIGURAÇÃO DOS CAMINHOS

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "train.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "titanic_processed.csv"


# 1. EXTRAÇÃO

def load_data():
    """Carrega os dados brutos."""
    print("Carregando dados...")
    df = pd.read_csv(RAW_DATA_PATH)
    print(f"Dados carregados: {df.shape[0]} linhas e {df.shape[1]} colunas")
    return df



# 2. PADRONIZAÇÃO DAS COLUNAS

def standardize_columns(df):
    """Padroniza os nomes das colunas."""
    print("Padronizando nomes das colunas...")
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )
    df = df.rename(columns={
        "passengerid": "passenger_id",
        "pclass": "passenger_class",
        "sibsp": "siblings_spouses",
        "parch": "parents_children"
    })

    return df


# 3. REMOVER DUPLICADOS
def remove_duplicates(df):
    """Remove registros duplicados."""

    print("Verificando registros duplicados...")
    duplicates = df.duplicated().sum()
    print(f"Registros duplicados encontrados: {duplicates}")
    df = df.drop_duplicates()

    return df


# 4. TRATAR VALORES NULOS

def handle_missing_values(df):

    """Realiza o tratamento de valores ausentes."""
    print("Tratando valores nulos...")
    # Preencher idade com a mediana
    df["age"] = df["age"].fillna(df["age"].median())
    # Preencher Embarked com o valor mais frequente
    df["embarked"] = df["embarked"].fillna(
        df["embarked"].mode()[0]
    )

    # Remover Cabin devido à grande quantidade de valores nulos
    df = df.drop(columns=["cabin"])
    return df


# 5. PADRONIZAR DADOS

def standardize_categorical_data(df):

    """Padroniza dados categóricos."""
    print("Padronizando dados categóricos...")

    df["sex"] = (
        df["sex"]
        .str.strip()
        .str.lower()
    )

    df["embarked"] = (
        df["embarked"]
        .str.strip()
        .str.upper()
    )

    return df


# 6. CRIAR NOVAS COLUNAS

def create_features(df):
    """Cria novas colunas a partir dos dados existentes."""

    print("Criando novas variáveis...")

    # Tamanho da família
    df["family_size"] = (
        df["siblings_spouses"]
        + df["parents_children"]
        + 1
    )

    # Grupo de idade
    def categorize_age(age):
        if age < 18:
            return "child"
        elif age < 60:
            return "adult"
        return "senior"

    df["age_group"] = df["age"].apply(categorize_age)

    return df


# 7. VALIDAÇÃO DOS DADOS

def validate_data(df):

    """Realiza validações de qualidade dos dados."""
    print("Validando dados...")
    # Verificar valores nulos
    missing_values = df.isnull().sum().sum()
    if missing_values > 0:
        raise ValueError(
            f"Existem {missing_values} valores nulos no dataset."
        )

    # Verificar duplicados
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        raise ValueError(
            f"Existem {duplicates} registros duplicados."
        )

    # Verificar idades negativas
    negative_age = (df["age"] < 0).sum()

    if negative_age > 0:
        raise ValueError("Existem idades negativas.")

    # Verificar tarifas negativas
    negative_fare = (df["fare"] < 0).sum()

    if negative_fare > 0:
        raise ValueError("Existem valores negativos na coluna fare.")

    print("Validação concluída com sucesso!")

    return df


# 8. CARREGAMENTO DOS DADOS
def save_data(df):
    """Salva os dados processados."""

    print("Salvando dados tratados...")

    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )

    print(f"Total de registros processados: {df.shape[0]}")
    print(f"Total de colunas finais: {df.shape[1]}")
    print(f"Arquivo salvo em: {PROCESSED_DATA_PATH}")

# PIPELINE PRINCIPAL

def main():

    print("\nIniciando pipeline de dados...\n")

    df = load_data()

    df = standardize_columns(df)

    df = remove_duplicates(df)

    df = handle_missing_values(df)

    df = standardize_categorical_data(df)

    df = create_features(df)

    df = validate_data(df)

    save_data(df)

    print("\nPipeline finalizado com sucesso!")


if __name__ == "__main__":
    main()