class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        # Параметры экрана
        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (0, 0, 64)

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 5

        # Настройки скорости корабля
        self.ship_speed = 2