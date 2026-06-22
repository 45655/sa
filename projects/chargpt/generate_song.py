import torch
from mingpt.model import GPT

# Load training text
text = open("input.txt", "r", encoding="utf-8").read()

# Recreate vocabulary
chars = sorted(list(set(text)))
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}

# Model config
config = GPT.get_default_config()
config.model_type = "gpt-mini"
config.vocab_size = len(chars)
config.block_size = 128

# Load trained model
model = GPT(config)
model.load_state_dict(torch.load("./out/chargpt/model.pt", map_location="cpu"))
model.eval()

def generate(prompt, max_new_tokens=300):
    # Handle unknown characters
    for ch in prompt:
        if ch not in stoi:
            print(f"Character '{ch}' not found in vocabulary")
            return ""

    x = torch.tensor([stoi[c] for c in prompt], dtype=torch.long)[None, ...]

    with torch.no_grad():
        y = model.generate(
            x,
            max_new_tokens=max_new_tokens,
            temperature=1.0,
            do_sample=True,
            top_k=10
        )[0]

    return ''.join([itos[int(i)] for i in y])

print("\nSpotify Lyrics GPT")
print("Type any word to generate lyrics.")
print("Type 'exit' to quit.\n")

while True:
    prompt = input("Enter prompt: ")

    if prompt.lower() == "exit":
        print("Goodbye!")
        break

    result = generate(prompt)

    print("\nGenerated Lyrics:\n")
    print(result)
    print("\n" + "=" * 80 + "\n")