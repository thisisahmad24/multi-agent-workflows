from typing import List, Dict, Any
from langchain_community.chat_models import ChatOllama
from langchain.schema import HumanMessage, SystemMessage, BaseMessage

class BaseAgent:
    def __init__(self, name: str, model: str = "llama3", system_prompt: str = ""):
        self.name = name
        self.model_name = model
        self.system_prompt = system_prompt
        self.llm = ChatOllama(model=model)
        
    def _get_messages(self, user_input: str, chat_history: List[BaseMessage] = None) -> List[BaseMessage]:
        messages = []
        if self.system_prompt:
            messages.append(SystemMessage(content=self.system_prompt))
        
        if chat_history:
            messages.extend(chat_history)
            
        messages.append(HumanMessage(content=user_input))
        return messages

    def run(self, user_input: str, chat_history: List[BaseMessage] = None) -> str:
        messages = self._get_messages(user_input, chat_history)
        response = self.llm.invoke(messages)
        return response.content

if __name__ == "__main__":
    # Quick test
    agent = BaseAgent(name="TestAgent", system_prompt="You are a helpful assistant.")
    print(f"Agent {agent.name} is ready.")
