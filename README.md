# 🧠 AI Council – Multi-Agent Deliberative Decision Framework

## 🚀 Overview

AI Council is a multi-agent decision-making system that simulates structured reasoning using multiple AI personas.

Instead of relying on a single model output, the system:

1. Generates multiple strategies
2. Critiques them using different personas
3. Scores them across key decision metrics
4. Selects the most robust strategy

---

## 🎯 Problem

Single-shot AI decisions can be unstable, biased, or incomplete.

This project explores:

* Multi-agent reasoning
* Structured critique systems
* Decision robustness through simulation

---

## ⚙️ System Pipeline

```text
User Question
     ↓
Strategy Generation (4 proposals)
     ↓
Multi-Persona Critique
  - Risk-averse critic
  - Aggressive optimizer
  - Pragmatic engineer
     ↓
Scoring Layer
  - Reversibility
  - Learning value
  - Cost risk
  - Downside risk
     ↓
Utility Computation
     ↓
Best Strategy Selection
     ↓
Stability Testing (multiple runs)
     ↓
Experiment Logging
```

---

## 🧠 Key Features

### 🔹 Multi-Agent Proposal Generation

Generates multiple strategies using an LLM to avoid single-path bias.

### 🔹 Persona-Based Critique

Each strategy is evaluated from different perspectives:

* Risk-sensitive
* Optimization-focused
* Practical engineering view

### 🔹 Quantitative Scoring System

Each strategy is scored on:

* Reversibility
* Learning Value
* Cost Risk
* Downside Risk

### 🔹 Utility-Based Decision Selection

A weighted utility function selects the optimal strategy.

### 🔹 Stability Testing

Runs multiple simulations with varying randomness to measure decision consistency.

### 🔹 Experiment Logging

Each run is saved with:

* Inputs
* Scores
* Final decision
* Stability metrics

---

## 🛠️ Tech Stack

* Python
* Local LLM via Ollama
* JSON-based structured reasoning
* Modular pipeline design

---

## 📊 Example Use Case

```text
Question:
"Should I scale a project now or optimize it further?"

Output:
- Best Strategy: "Take a small reversible step forward"
- Utility Scores:
  S1: 5.2
  S2: 7.8
  S3: 6.1
  S4: 6.9
- Stability Score: 0.8
```

---

## 📂 Project Structure

```text
ai-council/
├── main.py
├── results/
│   └── run_*.json
```

---

## ▶️ How to Run

```bash
python main.py
```

Make sure you have:

* Ollama running locally
* Model: llama3:8b

---

## 📌 Future Improvements

* Add real ML-based evaluators (not just LLM scoring)
* Improve aggregation logic (voting / weighted consensus)
* Add UI dashboard for experiment visualization
* Extend to cybersecurity decision systems

---

## 🤝 Why This Project Matters

This project demonstrates:

* Multi-agent AI system design
* Decision theory + AI integration
* Experimental evaluation (stability testing)

---

## 📎 Author

Sanju – ML + Cybersecurity focused developer


