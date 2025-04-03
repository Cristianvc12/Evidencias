import pandas as pd

# Crear un DataFrame
data = {'Nombre': ['Juan', 'Ana', 'Luis'],
        'Edad': [25, 30, 22],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia']}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

# Filtrar personas mayores de 25 años
df_mayores_25 = df[df['Edad'] > 25]
print(df_mayores_25)
