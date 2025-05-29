# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import pandas as pd
import zipfile 


def pregunta_01():
    zip_file_name = './files/input.zip'
    extracted_folder_name = './files' 
# 1. Unzip the file
    with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
        zip_ref.extractall(extracted_folder_name)
        print(f"'{zip_file_name}' unzipped to '{extracted_folder_name}/'")
    def extract_data_from_folder(folder_path):
        data = []
        for sentiment in ['negative', 'positive', 'neutral']:
            sentiment_path = os.path.join(folder_path, sentiment)
            for file_name in os.listdir(sentiment_path):
                file_path = os.path.join(sentiment_path, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    phrase = file.read().strip()
                    data.append({'phrase': phrase, 'target': sentiment})
        return data

    # Extraer datos de las carpetas de entrenamiento y prueba
    train_data = extract_data_from_folder('files/input/train')
    test_data = extract_data_from_folder('files/input/test')

    # Convertir los datos en DataFrames de pandas
    train_df = pd.DataFrame(train_data)
    test_df = pd.DataFrame(test_data)

    # Crear la carpeta de salida si no existe
    output_path = './files/output'
    os.makedirs(output_path, exist_ok=True)

    # Guardar los DataFrames en archivos CSV
    train_csv_path = os.path.join(output_path, 'train_dataset.csv')
    test_csv_path = os.path.join(output_path, 'test_dataset.csv')

    train_df.to_csv(train_csv_path, index=False)
    test_df.to_csv(test_csv_path, index=False)

    print(f'Archivos CSV generados en la carpeta {output_path}')
    

def extract_data_from_folder(folder_path):
    data = []
    for sentiment in ['negative', 'positive', 'neutral']:
        sentiment_path = os.path.join(folder_path, sentiment)
        for file_name in os.listdir(sentiment_path):
            file_path = os.path.join(sentiment_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                phrase = file.read().strip()
                data.append({'phrase': phrase, 'sentiment': sentiment})
    return data

print(pregunta_01()) 

"""
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """