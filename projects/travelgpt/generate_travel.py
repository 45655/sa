import torch
from mingpt.model import GPT

# Load training text
text = open("travel_input.txt", "r", encoding="utf-8").read()

# Recreate vocabulary
chars = sorted(list(set(text)))
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}

# Model configuration
config = GPT.get_default_config()
config.model_type = "gpt-mini"
config.vocab_size = len(chars)
config.block_size = 128

# Load trained model
model = GPT(config)
model.load_state_dict(
    torch.load("./out/travelgpt/model.pt", map_location="cpu")
)
model.eval()


def generate(prompt, max_new_tokens=100):

    # Handle unknown characters
    prompt = ''.join([c for c in prompt if c in stoi])

    x = torch.tensor(
        [stoi[c] for c in prompt],
        dtype=torch.long
    )[None, ...]

    with torch.no_grad():
        y = model.generate(
            x,
            max_new_tokens=max_new_tokens,
            temperature=0.8,
            do_sample=True,
            top_k=10
        )[0]

    result = ''.join([itos[int(i)] for i in y])

    parts = result.split("\nQuestion:")

    if len(parts) > 2:
        result = parts[0] + "\nQuestion:" + parts[1]

    return result
    


print("\n=== TravelGPT ===\n")

while True:

    user_input = input("Ask TravelGPT: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    print("\nResponse:\n")

    print(generate(user_input))

    print("\n" + "=" * 80 + "\n")