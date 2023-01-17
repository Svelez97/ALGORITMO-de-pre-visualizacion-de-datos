%config IPCompleter.greedy=True
import pandas as pd
from google.colab import drive
drive.mount('/content/drive')
MainPath = "/content/drive/MyDrive/Curso MAchine Learning/python-ml-course/datasets/" # Raiz del dataset.

archivo = 'titanic/titanic3.csv' # Puntero del archivo específico con extensión
ruta = MainPath + archivo
data_set = pd.read_csv(ruta)
## previsualizacion del dataset para verificar que si se abrio el archivo correcto
data_set.head()

col_names = data_set.columns.values  # se obtiene el listado de los nombre de las columnas

for name in col_names:
    total = pd.isnull(data_set[name])

    lista_nulos = []  # Se reinicia el listado nulo.
    lista_no_nulos = []  # Se reinicia el listado No nulo.

    for i in range(len(total)):  # se recorre cada dato de la lista.
        if total[i]:
            lista_nulos.append(i)
        else:
            lista_no_nulos.append(i)

    porcentaje_util = round(len(lista_no_nulos) * 100 / len(total), 2)

    print(f'En la columna "{name}": \n\t >>> Existen {len(lista_nulos)} datos NULOS de un total de {len(total)}.')
    print(f'\t >>> {porcentaje_util}% de los datos es ÚTIL.')

    if porcentaje_util < 100.0:
        print(f'\t SE RECOMIENDA REVIZAR LOS DATOS NULOS DE LA COLUMNA.\n')
    else:
        print('\n')

data_set.dtypes # si algun dato como por ejemplo la edad sale en un dato no numérico como 'object' alguno varios datos de esa columna no tienen sentido