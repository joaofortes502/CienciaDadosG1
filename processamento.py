import pandas as pd

# Carregar dados
df = pd.read_csv('digital_diet_mental_health.csv')

# Verificar estrutura
print("\nInformações do dataset:")
print(df.info())


# Verificar valores nulos
print(df.isnull().sum())
# Sem valores nulos

# Verificar tipos de dados
print(df.dtypes)  

