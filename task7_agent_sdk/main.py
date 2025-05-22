class Agent:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

class Runner:
    @classmethod
    def run(cls, agent_cls, prompt):
        agent = agent_cls()
        return f"{agent.name} says: The answer to '{prompt}' is 'Abuja'."

class MyAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Smart Helper",
            instructions="You are a concise and friendly assistant."
        )

response = Runner.run(MyAgent, "What's the capital of Nigeria?")
print(response)
