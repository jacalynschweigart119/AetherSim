class RewardSystem:
    """
    Система вознаграждения для обучения с подкреплением.
    """

    def __init__(self, target_height=5.0):
        self.target_height = target_height

    def compute_reward(self, agent):
        """
        Вознаграждение за приближение к целевой высоте и сохранение энергии.
        """
        height_reward = -abs(agent.position[1] - self.target_height)
        energy_bonus = agent.energy * 0.01
        reward = height_reward + energy_bonus
        agent.reward += reward
        return reward
