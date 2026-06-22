import pandas as pd

# Load CSV
df = pd.read_csv(r"C:\Users\hp\Downloads\travel_faq_production.csv")

with open("travel_input.txt", "w", encoding="utf-8") as f:

    for _, row in df.iterrows():

        question = str(row["Question"]).strip()
        answer = str(row["Answer"]).strip()

        f.write(f"Question: {question}\n")
        f.write(f"Answer: {answer}\n\n")

print("travel_input.txt created successfully!")