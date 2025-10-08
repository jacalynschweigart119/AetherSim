import numpy as np

class SensorSystem:
    """
    Простая сенсорная система, воспринимающая ближайшие объекты.
    """

    def __init__(self, agent, range_radius: float = 5.0):
        self.agent = agent
        self.range = range_radius

    def read(self):
        """Вернуть список ближайших объектов."""
        visible = []
        for obj in self.agent.environment.objects:
            if obj is self.agent:
                continue
            dist = np.linalg.norm(obj.position - self.agent.position)
            if dist <= self.range:
                visible.append({
                    "name": getattr(obj, "name", "object"),
                    "distance": dist,
                    "relative_pos": obj.position - self.agent.position
                })
        return visible
