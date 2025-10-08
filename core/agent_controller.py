import numpy as np
from .sensory_input import SensorSystem

class Agent:
    """
    Агент, взаимодействующий с окружением через сенсоры и действия.
    """

    def __init__(self, name, environment, position=None):
        self.name = name
        self.environment = environment
        self.position = np.array(position or [0.0, 0.0, 0.0], dtype=float)
        self.velocity = np.zeros(3)
        self.energy = 100.0
        self.sensors = SensorSystem(self)
        self.reward = 0.0

    def act(self, action_vector):
        """Совершить действие — применить силу к агенту."""
        self.velocity += np.array(action_vector) * 0.1
        self.energy -= np.linalg.norm(action_vector) * 0.5

    def observe(self):
        """Получить данные сенсоров."""
        return self.sensors.read()

    def update(self):
        """Обновить состояние агента."""
        self.position += self.velocity * 0.1
        self.energy = max(0.0, self.energy - 0.1)
