import pandas as pd


import glob


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