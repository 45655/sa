# TravelGPT - Travel Domain Language Model

## Project Structure

```text
minGPT/
│
├── mingpt/
│   ├── model.py
│   ├── trainer.py
│   ├── utils.py
│   └── bpe.py
│
├── projects/
│   ├── chargpt/
│   │
│   └── travelgpt/
│       ├── create_input.py
│       ├── travel_input.txt
│       ├── travelgpt.py
│       ├── generate_travel.py
│       └── out/
│           └── travelgpt/
│               └── model.pt
│
└── setup.py
```

---

# Project Overview

TravelGPT is a Transformer-based language model built using the minGPT framework and trained on a custom travel FAQ dataset.

The goal of this project is to demonstrate the core concepts of Large Language Model (LLM) architecture including:

* Tokenization
* Vocabulary Creation
* Embeddings
* Self-Attention
* Forward Propagation
* Loss Calculation
* Backpropagation
* Weight Updates
* Text Generation (Inference)

The model was trained on travel-related questions and answers covering destinations, temples, itineraries, visa information, honeymoon trips, family trips, budgets, hotels, and adventure travel.

---

# File Description

## model.py

Contains the GPT Transformer architecture.

Responsibilities:

* Token Embeddings
* Positional Embeddings
* Self-Attention
* Transformer Blocks
* MLP Layers
* Text Generation

This file represents the core neural network of TravelGPT.

---

## trainer.py

Responsible for model training.

Responsibilities:

* Forward Pass
* Loss Calculation
* Backpropagation
* Optimizer Updates
* Training Loop

This file updates the model weights during training.

---

## create_input.py

Converts the travel dataset into a training corpus.

Input:

```csv
Question,Answer
```

Output:

```text
Question: Best time to visit Tirumala?
Answer: September to March is ideal.

Question: Budget for Maldives trip?
Answer: ₹80,000 to ₹1,50,000 depending on season.
```

Generated File:

```text
travel_input.txt
```

---

## travel_input.txt

Training corpus used by TravelGPT.

Generated from:

```text
travel_faq_production.csv
```

Contains all travel questions and answers in a format suitable for GPT training.

---

## travelgpt.py

Main training script.

Responsibilities:

1. Load travel_input.txt
2. Build vocabulary
3. Convert characters into tokens
4. Create training batches
5. Initialize GPT model
6. Train model
7. Calculate loss
8. Perform backpropagation
9. Save trained model

Output:

```text
model.pt
```

---

## model.pt

Trained TravelGPT model.

Stores learned weights after training.

Training Results:

```text
Initial Loss : 4.39
Final Loss   : 0.16
Iterations   : 3000
```

The reduction in loss indicates successful learning of travel-domain text patterns.

---

## generate_travel.py

Loads the trained TravelGPT model and generates travel-related responses.

Example:

Input:

```text
When should I visit Sri Lanka?
```

Output:

```text
Answer: December to March for the west and south coasts; differs by region due to two monsoon systems.
```

---

# Execution Flow

```text
travel_faq_production.csv
            │
            ▼
    create_input.py
            │
            ▼
    travel_input.txt
            │
            ▼
      travelgpt.py
            │
            ▼
     GPT Training
            │
            ▼
    Loss Calculation
            │
            ▼
    Backpropagation
            │
            ▼
      model.pt
            │
            ▼
 generate_travel.py
            │
            ▼
      User Query
            │
            ▼
    TravelGPT Response
```

---

# How TravelGPT Learns

```text
Travel Dataset
       │
       ▼
Character Tokenization
       │
       ▼
Vocabulary Creation
       │
       ▼
Embedding Layer
       │
       ▼
Self-Attention
       │
       ▼
MLP Layers
       │
       ▼
Forward Pass
       │
       ▼
Loss Calculation
       │
       ▼
Backpropagation
       │
       ▼
Weight Updates
       │
       ▼
Learned Travel Knowledge
       │
       ▼
Text Generation
```

---

# Training Summary

Dataset: Custom Travel FAQ Dataset

Framework: minGPT

Model Type: GPT-Mini

Training Iterations: 3000

Initial Loss: 4.39

Final Loss: 0.16

Objective: Train a Transformer-based model capable of generating travel-domain responses through model inference.

---

# Conclusion

TravelGPT demonstrates the complete lifecycle of a GPT-style Transformer model, including data preparation, tokenization, training, optimization, and inference.

The project successfully implements the backbone of LLM architecture and generates travel-related responses using a trained Transformer model rather than simple keyword matching or retrieval.
