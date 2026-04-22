from src.base_agent import BaseAgent

class ResearcherAgent(BaseAgent):
    def __init__(self, model: str = "llama3"):
        system_prompt = """You are a Research Agent. Your goal is to find accurate information, documentation, and best practices for the given task.
        Provide clear, concise summaries of your findings."""
        super().__init__(name="Researcher", model=model, system_prompt=system_prompt)

class CoderAgent(BaseAgent):
    def __init__(self, model: str = "llama3"):
        system_prompt = """You are a Coder Agent. Your goal is to write high-quality, efficient, and well-documented code.
        Provide the code in blocks and explain your implementation choices."""
        super().__init__(name="Coder", model=model, system_prompt=system_prompt)

class ReviewerAgent(BaseAgent):
    def __init__(self, model: str = "llama3"):
        system_prompt = """You are a Reviewer Agent. Your goal is to check code or research for errors, security vulnerabilities, or quality issues.
        Provide constructive feedback and suggest improvements."""
        super().__init__(name="Reviewer", model=model, system_prompt=system_prompt)

if __name__ == "__main__":
    researcher = ResearcherAgent()
    coder = CoderAgent()
    reviewer = ReviewerAgent()
    print("Worker Agents are ready.")
