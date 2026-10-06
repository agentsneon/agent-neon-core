class NeonAgent:
    def __init__(self, name="Neon"):
        self.name = name

    def start(self):
        print(f"{self.name} is starting...")

if __name__ == "__main__":
    agent = NeonAgent()
    agent.start()
