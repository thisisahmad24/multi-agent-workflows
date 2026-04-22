# Multi-Agent Workflows 🤖

Autonomous AI task execution environment powered by interconnected LLM agents.

## Overview
This project implements a multi-agent system where different agents collaborate to solve complex tasks. It uses local LLMs via Ollama and LangChain/LangGraph for orchestration.

## Setup
1. Install [Ollama](https://ollama.com/).
2. Pull required models: `ollama pull llama3` (or your preferred model).
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Features
- **Task Decomposition**: Break complex tasks into manageable sub-tasks.
- **Specialized Agents**: Different agents for research, coding, and review.
- **Local Execution**: Completely free to run with local LLMs.
