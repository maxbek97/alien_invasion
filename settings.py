class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        # Параметры экрана
        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (0, 0, 64)

        # Настройки скорости корабля
        self.ship_speed = 2