"""Módulo responsável por carregar o dataframe em um arquivo Excel no data/output."""

import os

import pandas as pd


def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    """
    Recebe um DataFrame e salva como arquivo Excel.

    Args:
        data_frame (pd.DataFrame): DataFrame a ser salvo.
        output_path (str): Caminho onde o arquivo será salvo.
        file_name (str): Nome do arquivo (sem extensão).

    Returns:
        str: Mensagem de sucesso após salvar o arquivo.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo salvo com sucesso"


if __name__ == "__main__":
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    print(load_excel(df, "data/output", "test"))
