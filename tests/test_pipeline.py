import pandas as pd
from app.pipeline.transform import concat_data_frames

"""
    Testa a concatenação da lista de dataframes
    Pattern: Arrange-Act-Assert
"""

def testar_a_concatenacao_da_lista_de_dataframe():
    # arrange
    df1 = pd.DataFrame({'col1': [2, 3], 'col2': [5, 6]})
    df2 = pd.DataFrame({'col1': [3, 2], 'col2': [6, 5]})
    data_frame_list = [df1, df2]

    # act
    df = concat_data_frames(data_frame_list)

    # assert
    assert df.shape == (4, 2)
