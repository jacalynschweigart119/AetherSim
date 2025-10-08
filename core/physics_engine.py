import numpy as np

class PhysicsEngine:
    """
    Простой физический движок с моделированием столкновений и гравитации.
    """

    def __init__(self, gravity: float = 9.81, time_step: float = 0.01):
        self.gravity = gravity
        self.time_step = time_step
        self.objects = []

    def add_object(self, obj):
        """Добавить физический объект в симуляцию."""
        self.objects.append(obj)

    def step(self):
        """Сделать шаг симуляции."""
        for obj in self.objects:
            # Применяем гравитацию
            obj.velocity[1] -= self.gravity * self.time_step
            obj.position += obj.velocity * self.time_step

            # Проверка столкновения с "землей"
            if obj.position[1] < 0:
                obj.position[1] = 0
                obj.velocity[1] *= -0.5  # теряем часть энергии
