import getpass

DB_NAME = "snake_db"
DB_USER = getpass.getuser()
DB_HOST = "localhost"

CELL_SIZE = 22
GRID_WIDTH = 26
GRID_HEIGHT = 26

SCREEN_W = CELL_SIZE * GRID_WIDTH
SCREEN_H = CELL_SIZE * GRID_HEIGHT

MAX_FOODS = 3
BASE_SPEED = 6
PU_LIFETIME = 8000
FOOD_TYPES = [
    {"value": 10, "weight": 60, "lifetime": 7000, "color": (220, 50, 50)},
    {"value": 25, "weight": 30, "lifetime": 5000, "color": (255, 150, 0)},
    {"value": 50, "weight": 10, "lifetime": 3000, "color": (255, 50, 180)},
]
POISON_COLOR = (100, 0,  20)
PU_COLORS = {
    "speed": (0, 200, 220),
    "slow": (180, 100, 220),
    "shield": (50, 200, 50),
}

DEFAULT_SETTINGS = {
    "snake_color": [60, 200, 60],
    "grid_overlay": True,
    "sound": False,
}
