import pandas as pd
import glob

print("Day 1 - Data Ingestion")
files = glob.glob("data/raw/*.csv")
print(f"Total files mile: {len(files)}")

for f in files:
    df = pd.read_csv(f)
    print(f"\nFile: {f}")
    print("Shape:", df.shape)
    print(df.head(2))
    print("Missing Values:", df.isnull().sum().sum())
    df.to_csv("data/processed/cleaned_nav.csv", index=False)
    print("cleaned_nav.csv ban gaya!")

print("\nDay 1 Data Ingestion Complete!")