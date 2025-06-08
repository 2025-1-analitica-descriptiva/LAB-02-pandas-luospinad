"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
from homework.load_input import load_input
import pandas as pd

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    
    file_path = 'files/input'
    dataframe_0 = load_input(file_path, 0)
    dataframe_2 = load_input(file_path, 2)

    df_group_2 = dataframe_2.groupby("c0")["c5b"].sum()
    df_joined = pd.merge(dataframe_0, df_group_2, on="c0", how="inner")

    print(df_joined)
    result = df_joined.groupby("c1")["c5b"].sum()

    return result
