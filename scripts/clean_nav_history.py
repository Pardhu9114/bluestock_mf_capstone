import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Validate NAV > 0
df = df[df["nav"] > 0]

# Forward fill NAV within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

df.to_csv("data/processed/clean_nav_history.csv", index=False)

print(df.shape)