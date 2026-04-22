import sys
from src.supervisor_agent import SupervisorAgent
from src.worker_agents import ResearcherAgent, CoderAgent, ReviewerAgent

class WorkflowManager:
    def __init__(self, model: str = "llama3"):
        self.supervisor = SupervisorAgent(model=model)
        self.workers = {
            "researcher": ResearcherAgent(model=model),
            "coder": CoderAgent(model=model),
            "reviewer": ReviewerAgent(model=model)
        }

    def execute(self, user_request: str):
        print(f"\n🚀 Starting workflow for: '{user_request}'")
        
        # 1. Decompose task
        print("🔍 Supervisor is decomposing the task...")
        sub_tasks = self.supervisor.decompose_task(user_request)
        
        results = []
        
        # 2. Execute sub-tasks
        for i, sub in enumerate(sub_tasks):
            task_desc = sub.get("task", "No description")
            assigned_to = sub.get("assigned_to", "none").lower()
            
            print(f"\n--- Sub-task {i+1} ---")
            print(f"📋 Task: {task_desc}")
            print(f"👤 Assigned to: {assigned_to}")
            
            if assigned_to in self.workers:
                worker = self.workers[assigned_to]
                result = worker.run(task_desc)
                results.append({"task": task_desc, "result": result, "agent": assigned_to})
                print(f"✅ Result from {assigned_to}:\n{result}")
            else:
                print(f"⚠️ Warning: No agent found for role '{assigned_to}'")
        
        print("\n✨ Workflow complete!")
        return results

if __name__ == "__main__":
    manager = WorkflowManager()
    
    print("🤖 Welcome to Multi-Agent Workflows!")
    print("Type 'exit' or 'quit' to stop.\n")
    
    while True:
        try:
            user_task = input("👉 Enter your task: ")
            if user_task.lower() in ["exit", "quit"]:
                break
            
            if not user_task.strip():
                continue
                
            manager.execute(user_task)
            print("\n" + "="*50 + "\n")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
