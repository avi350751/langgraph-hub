# LangGraph Hub 🧩

Tutorial notebooks to learn and experiment with **[LangGraph](https://langchain-ai.github.io/langgraph/)** — from installation checks to building small workflows with tools and LLMs.

This repo is meant to be a **hands-on playground**: open a notebook, run the cells, and see LangGraph in action.

---

## 🔁 What is LangGraph (in one line)?

> LangGraph is a framework built on top of LangChain that lets you design conversational and agentic systems as **graphs of nodes** (LLMs, tools, routers, state, etc.) instead of one long chain.

If you’re exploring agentic AI, tool-calling, or multi-step workflows, LangGraph gives you a clean, composable way to model them.

---

## 📂 Repository Structure

| File/Folder                    | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `0_test_installation.ipynb`    | Quick environment & installation check. Verify Python + dependencies work. |
| `1_bmi_workflow.ipynb`         | Intro workflow example using LangGraph (e.g., a simple BMI-style pipeline).|
| `2_llm_workflow.ipynb`         | LLM-powered workflow using LangGraph (build a minimal LLM graph).          |
| `requirements.txt`             | Python dependencies for all notebooks.                                     |

> Start from `0_test_installation.ipynb`, then move to `1_bmi_workflow.ipynb` and `2_llm_workflow.ipynb` in order.

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/avi350751/langgraph-hub.git
cd langgraph-hub
