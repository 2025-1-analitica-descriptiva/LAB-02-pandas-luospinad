"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd  # type: ignore
import glob
import os

def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    file_path = os.path.join("files", "input")
    dataframe = load_input(file_path, 0)
    return len(dataframe)

def load_input(input_directory, fileNumber):
    """Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #
    files = glob.glob(f"{input_directory}/tbl{fileNumber}.tsv")
    dataframes = [
        pd.read_csv(
            file,
            delimiter="\t",
            index_col=None,
        )
        for file in files
    ]

    dataframe = pd.concat(dataframes, ignore_index=True)

    return dataframe
