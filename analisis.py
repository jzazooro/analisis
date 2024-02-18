import pandas as pd

# Cargando los archivos CSV
equipo_df = pd.read_csv('equipo.csv')
partidos_df = pd.read_csv('partidos.csv')

# Visualizando las primeras filas de cada DataFrame para entender su estructura
equipo_df_head = equipo_df.head()
partidos_df_head = partidos_df.head()

equipo_df_head, partidos_df_head


# Corrigiendo la carga de 'equipo.csv' para incluir encabezados de columna
equipo_df = pd.read_csv('equipo.csv', header=None, names=['Nombre', 'Imagen', 'País', 'ID'])

# Corrigiendo la carga de 'partidos.csv' para incluir encabezados de columna, asumiendo una estructura estándar basada en la vista previa
# Asumiendo que las columnas son: Fecha, Hora, Equipo_Local, Equipo_Visitante, y otros identificadores o estadísticas
partidos_df.columns = ['Fecha_Hora', 'Equipo_Local', 'Equipo_Visitante', 'Unknown1', 'Unknown2', 'Unknown3']

# Visualizando nuevamente las primeras filas para confirmar los ajustes
equipo_df_head_corrected = equipo_df.head()
partidos_df_head_corrected = partidos_df.head()

equipo_df_head_corrected, partidos_df_head_corrected


# Análisis Exploratorio de Datos (EDA) para 'equipo.csv'
equipo_describe = equipo_df.describe(include='all')
equipo_paises_count = equipo_df['País'].value_counts()

# Análisis Exploratorio de Datos (EDA) para 'partidos.csv'
partidos_describe = partidos_df.describe()

equipo_describe, equipo_paises_count, partidos_describe


import matplotlib.pyplot as plt

# Visualización de la distribución de equipos por país
plt.figure(figsize=(10, 8))
equipo_paises_count.plot(kind='bar')
plt.title('Distribución de Equipos por País')
plt.xlabel('País')
plt.ylabel('Número de Equipos')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')

# Preparando datos para visualizar la cantidad de partidos jugados por equipo
partidos_por_equipo = pd.concat([partidos_df['Equipo_Local'], partidos_df['Equipo_Visitante']]).value_counts().sort_index()

# Visualización de la cantidad de partidos jugados por equipo
plt.figure(figsize=(10, 8))
partidos_por_equipo.plot(kind='bar')
plt.title('Cantidad de Partidos Jugados por Equipo')
plt.xlabel('ID del Equipo')
plt.ylabel('Cantidad de Partidos')
plt.grid(axis='y', linestyle='--')

plt.show()


# Conversión de la columna 'Fecha_Hora' a datetime para facilitar el análisis
partidos_df['Fecha_Hora'] = pd.to_datetime(partidos_df['Fecha_Hora'])

# Extrayendo componentes de fecha como año y mes para análisis
partidos_df['Año'] = partidos_df['Fecha_Hora'].dt.year
partidos_df['Mes'] = partidos_df['Fecha_Hora'].dt.month

# Contando la cantidad de partidos por mes
partidos_por_mes = partidos_df.groupby(['Año', 'Mes']).size()

# Visualizando la cantidad de partidos por mes
plt.figure(figsize=(14, 7))
partidos_por_mes.plot(kind='bar')
plt.title('Cantidad de Partidos por Mes')
plt.xlabel('Mes')
plt.ylabel('Cantidad de Partidos')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.show()



# Calculando estadísticas descriptivas para la cantidad de partidos jugados por equipo
estadisticas_partidos_por_equipo = partidos_por_equipo.describe()

print(estadisticas_partidos_por_equipo)


