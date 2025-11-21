import pandas as pd

df = pd.read_csv("data/GlobalWeatherRepository.csv")

# Convert timestamp column
df['last_updated'] = pd.to_datetime(df['last_updated'])

# Drop duplicate rows (if any)
df = df.drop_duplicates()

print("Shape after cleaning:", df.shape)
