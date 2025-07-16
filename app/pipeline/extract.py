"""Módulo responsável por extrair os arquivos em Excel de data/input."""

import glob  # lib para listar arquivos
import os  # lib para manipular arquivos e pastas
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """Lê arquivos Excel de data/input e retorna uma lista de dataframes.

    Args:
        path (str): Caminho da pasta com os arquivos.

    Returns:
        List[pd.DataFrame]: Lista de dataframes.
    """
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


if __name__ == "__main__":
    dfs = extract_from_excel(path="data/input")
    print(dfs)
