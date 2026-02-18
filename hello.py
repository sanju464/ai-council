import json
import re
import random
import requests
import uuid
import os
import statistics
from datetime import datetime

# =========================
# CONFIG
# =========================

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3:8b"
TIMEOUT = 45
RESULTS_DIR = "results"

os.makedirs(RESULTS_DIR, exist_ok=True)

# =========================
# SAFE LLM CALL
# =========================

def call_llm(prompt, temperature=0.2):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "temperature": temperature,
            },
            timeout=TIMEOUT
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception:
        return ""

# =========================
# JSON EXTRACTION (SAFE)
# =========================

def extract_json(text):
    try:
        start = text.index("{")
        end = text.rindex("}") + 1
        return json.loads(text[start:end])
    except Exception:
        return None

# =========================
# PHASE 1: PROPOSALS
# =========================

def generate_proposals(question, temperature=0.4):
    prompt = f"""
Generate 4 strategies.
STRICT JSON ONLY.

Format:
{{ "S1": "...", "S2": "...", "S3": "...", "S4": "..." }}

Question:
{question}
"""
    raw = call_llm(prompt, temperature)
    data = extract_json(raw)

    if isinstance(data, dict) and len(data) >= 3:
        return data

    return {
        "S1": "Delay major action and gather more data.",
        "S2": "Take a small reversible step forward.",
        "S3": "Optimize current system before scaling.",
        "S4": "Scale selectively with rollback safeguards."
    }

# =========================
# PHASE 2: CRITIQUE
# =========================

PERSONAS = [
    "Risk-averse critic",
    "Aggressive optimizer",
    "Pragmatic engineer",
]

def generate_critiques(proposals):
    critiques = []
    for persona in PERSONAS:
        for strategy in proposals.values():
            prompt = f"""
You are a {persona}.
Critique this strategy briefly:

{strategy}
"""
            text = call_llm(prompt, temperature=0.3)
            if text:
                critiques.append({
                    "persona": persona,
                    "strategy": strategy,
                    "critique": text
                })
    return critiques

# =========================
# PHASE 3: SCORING LAYER
# =========================

def score_strategies(proposals, critiques):
    prompt = f"""
Rate each strategy from 1-10 on:
- reversibility
- learning_value
- cost_risk
- downside_risk

Return STRICT JSON ONLY.

Strategies:
{json.dumps(proposals, indent=2)}

Critiques:
{json.dumps(critiques, indent=2)}

Format:
{{
  "S1": {{
    "reversibility": 8,
    "learning_value": 6,
    "cost_risk": 4,
    "downside_risk": 3
  }}
}}
"""
    raw = call_llm(prompt, temperature=0.0)
    data = extract_json(raw)

    if isinstance(data, dict):
        return data

    # Fallback scoring
    fallback = {}
    for key in proposals:
        fallback[key] = {
            "reversibility": random.randint(5, 8),
            "learning_value": random.randint(5, 8),
            "cost_risk": random.randint(3, 6),
            "downside_risk": random.randint(3, 6)
        }
    return fallback

# =========================
# UTILITY FUNCTION
# =========================

def compute_utility(scores):
    utilities = {}
    for k, v in scores.items():
        utility = (
            0.4 * v["reversibility"] +
            0.3 * v["learning_value"] -
            0.2 * v["cost_risk"] -
            0.1 * v["downside_risk"]
        )
        utilities[k] = round(utility, 3)
    return utilities

# =========================
# FINAL DECISION
# =========================

def select_best(utilities):
    return max(utilities, key=utilities.get)

# =========================
# SINGLE RUN PIPELINE
# =========================

def run_pipeline(question, temperature=0.2):
    proposals = generate_proposals(question)
    critiques = generate_critiques(proposals)
    scores = score_strategies(proposals, critiques)
    utilities = compute_utility(scores)
    decision_key = select_best(utilities)

    result = {
        "question": question,
        "proposals": proposals,
        "scores": scores,
        "utilities": utilities,
        "decision": decision_key,
        "decision_text": proposals[decision_key]
    }

    return result

# =========================
# STABILITY TEST
# =========================

def stability_test(question, runs=5):
    decisions = []

    for i in range(runs):
        temp = random.choice([0.0, 0.2, 0.4])
        result = run_pipeline(question, temperature=temp)
        decisions.append(result["decision"])

    most_common = max(set(decisions), key=decisions.count)
    stability = decisions.count(most_common) / runs

    return {
        "decisions": decisions,
        "stability_score": round(stability, 2)
    }

# =========================
# EXPERIMENT LOGGER
# =========================

def log_experiment(data):
    run_id = str(uuid.uuid4())[:8]
    filename = f"{RESULTS_DIR}/run_{run_id}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    return filename

# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":
    question = input("Enter your decision question: ")

    print("\nRunning multi-agent deliberative framework...\n")

    result = run_pipeline(question)
    stability = stability_test(question, runs=5)

    full_output = {
        "timestamp": str(datetime.now()),
        "result": result,
        "stability_test": stability
    }

    file_path = log_experiment(full_output)

    print("Final Decision:", result["decision"])
    print("Decision Strategy:", result["decision_text"])
    print("Utilities:", result["utilities"])
    print("Stability Score:", stability["stability_score"])
    print("Saved to:", file_path)
