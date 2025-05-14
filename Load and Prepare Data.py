import pandas as pd

# Load and clean data
df = pd.read_csv("C:\\Users\\niyor\\Downloads\\Airpassenger.csv")
df[['Month', 'Passengers']] = df['Month,#Passengers'].str.split(',', expand=True)
df.drop(columns=['Month,#Passengers'], inplace=True)

# Convert data types
df['Month'] = pd.to_datetime(df['Month'])
df['Passengers'] = pd.to_numeric(df['Passengers'])