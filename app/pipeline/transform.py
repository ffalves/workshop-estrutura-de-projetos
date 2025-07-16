"""Módulo responsável por transformar os arquivos em Excel em um único dataframe."""

from typing import List

import pandas as pd


def concat_data_frame(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """Função para transformar uma lista de dataframes em um único dataframe."""
    return pd.concat(data_frame_list, ignore_index=True)
