from typing import List, Dict
from src.base_agent import BaseAgent
import json

class SupervisorAgent(BaseAgent):
    def __init__(self, model: str = "llama3"):
        system_prompt = """You are a Task Supervisor. Your job is to take a complex user request and break it down into a list of smaller, actionable sub-tasks.
        Each sub-task should be assigned to one of the following agent types:
        - researcher: For finding information or documentation.
        - coder: For writing, refactoring, or debugging code.
        - reviewer: For checking work and ensuring quality.
        
        Output your response ONLY as a JSON list of objects with the following keys:
        - task: The description of the sub-task.
        - assigned_to: The agent type (researcher, coder, reviewer).
        
        Example:
        [{"task": "Research the library API", "assigned_to": "researcher"}, {"task": "Implement the function", "assigned_to": "coder"}]
        """
        super().__init__(name="Supervisor", model=model, system_prompt=system_prompt)
        
    def decompose_task(self, task: str) -> List[Dict[str, str]]:
        response = self.run(f"Decompose this task: {task}")
        try:
            # Attempt to find JSON in the response
            start = response.find('[')
            end = response.rfind(']') + 1
            if start != -1 and end != 0:
                json_str = response[start:end]
                return json.loads(json_str)
            return [{"task": "Error: Could not parse tasks", "assigned_to": "none"}]
        except Exception as e:
            return [{"task": f"Error parsing response: {str(e)}", "assigned_to": "none"}]

if __name__ == "__main__":
    supervisor = SupervisorAgent()
    tasks = supervisor.decompose_task("Build a simple calculator in Python and write tests for it.")
    print("Decomposed Tasks:")
    for i, t in enumerate(tasks):
        print(f"{i+1}. [{t['assigned_to']}] {t['task']}")
