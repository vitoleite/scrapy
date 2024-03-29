import pandas as pd
from pandas import DataFrame


def formatting(file: str, file_name: str, month_name: str, save_local: str):
    """
    Efetuando a limpeza dos dados para a utilização final.

    Args
    ---
    - file [str]: Local do arquivo a ser formatado.
    - save_local [str]: Local onde o arquivo deverá ser salvo.
    - file_name [str]: Nome do arquivo.
    - month_name [str]: Aplica o formato Mês/Ano para diferenciar arquivos

    Return
    ---
    Salva o arquivo no local de acordo com os parâmetros estabelecidos na função.
    """

    # DataFrame Refactoring
    df: DataFrame = pd.read_csv(file, encoding="ISO=8859-1", sep=";", decimal=",")

    colunas: dict[str, str] = {
        "Data": "Data",
        "24 - Captação líquida diária de depósitos de poupança - SBPE e rural - u.m.c. (mil)": "Captação diária de poupança - mil",
    }

    df = df.rename(columns=colunas)

    # Deleting the last row
    df = df[:-1]

    # Refactoring the data values
    df["Captação diária de poupança - mil"] = df[
        "Captação diária de poupança - mil"
    ].str.replace(",", "", regex=True)
    df["Captação diária de poupança - mil"] = df[
        "Captação diária de poupança - mil"
    ].str.replace("\.", "", regex=True)
    df["Captação diária de poupança - mil"] = pd.to_numeric(
        df["Captação diária de poupança - mil"], errors="ignore"
    )

    # Divide values cause formatting is stucking to identifying right values
    df["Captação diária de poupança - mil"] = (
        df["Captação diária de poupança - mil"] / 100
    )

    # Obtaining the sum of all values
    total = df["Captação diária de poupança - mil"].sum()
    df["Captação mensal acumulada - mil"] = total

    # Removing duplicated values
    df["Captação mensal acumulada - mil"] = df["Captação mensal acumulada - mil"].mask(
        df.duplicated(["Captação mensal acumulada - mil"])
    )

    print("Tratamento realizado com sucesso!!!")
    return df.to_csv(
        f"{save_local}{file_name}{month_name}.csv",
        index=False,
        encoding="utf-8-sig",
        sep=";",
        decimal=",",
    )
