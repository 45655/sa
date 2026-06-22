import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Downloads\archive\spotify_millsongdata.csv")

# Use first 1000 songs only for demo
lyrics = "\n\n".join(df["text"].head(1000).astype(str))

with open("input_small.txt", "w", encoding="utf-8") as f:
    f.write(lyrics)

print("input_small.txt created successfully")