from .physics_engine import PhysicsEngine

class Environment:
    """
    Среда, объединяющая физику, агентов и шаги симуляции.
    """

    def __init__(self, gravity=9.81, time_step=0.01):
        self.physics = PhysicsEngine(gravity, time_step)
        self.objects = []
        self.agents = []

    def add_agent(self, agent):
        """Добавить агента в среду."""
        self.agents.append(agent)
        self.physics.add_object(agent)
        self.objects.append(agent)

    def step(self):
        """Шаг симуляции: обновление физики и агентов."""
        self.physics.step()
        for agent in self.agents:
            agent.update()
