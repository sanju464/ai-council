# AI-Council  
### Structured Multi-Agent Deliberative Framework for Risk-Aware LLM Decision Making

AI-Council is an experimental framework that transforms large language models from single-shot text generators into structured deliberative decision systems.

Instead of asking an LLM for one answer, AI-Council simulates a multi-phase reasoning process:

1. Strategy generation
2. Adversarial critique
3. Quantitative scoring
4. Deterministic utility computation
5. Stability testing under stochastic sampling

The system is designed to improve robustness, interpretability, and decision consistency in high-uncertainty scenarios.

---

## 🧠 Motivation

LLMs often produce:

- Overconfident answers
- First-response bias
- Unstable outputs across sampling temperatures
- Unstructured reasoning

AI-Council addresses these issues by introducing:

- Multi-strategy divergence
- Persona-based adversarial evaluation
- Structured JSON scoring
- Explicit utility modeling
- Reproducible experiment logging

This project explores whether structured prompting + deterministic aggregation improves decision stability and risk awareness.

---

## 🏗 System Architecture

