"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
from homework.load_input import load_input

def pregunta_04():
    """
    Calcule el promedio de `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: c2, dtype: float64
    """
    
    file_path = 'files/input'
    dataframe = load_input(file_path, 0)
    df_avg = dataframe.groupby("c1")["c2"].mean()

    return df_avg