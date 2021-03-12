from enum import Enum


class Ant:
    def __init__(self, type, health, locationCell):
        # ANT_TYPES
        self.type = type
        # Current Cell
        self.locationCell = locationCell
        self.health = health

    # get current location
    def get_location(self):
        return self.locationCell

    # get cells in this ants view
    def get_neighbours_cell(self):
        return currentState.around_cells

    def get_health(self):
        return self.health


class Map:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self.cells = []


class Cell:
    def __init__(self, x, y, type, resource_value, resource_type):
        self.x = x
        self.y = y
        # CELL_TYPES
        self.type = type
        # current ants in this cell
        self.ants = []
        self.resource_value = resource_value
        self.resource_type = resource_type


class Resource:
    def __init__(self, type, amount):
        # RESOURCE_TYPES
        self.type = type
        self.amount = amount

    def get_type(self):
        return self.type

    def get_amount(self):
        return self.amount


class Message:
    def __init__(self, text: str, turn: int):
        self.text = text
        self.turn = turn


class GameConfig:
    map_width = 0  # int
    map_height = 0  # int
    ant_type = None
    base_x = -1  # int
    base_y = -1  # int
    health_kargar = 0  # int
    health_sarbaaz = 0  # int
    attack_distance = 0  # int
    generate_kargar = 0
    generate_sarbaz = 0  # int
    generate_sarbaaz = 0
    rate_death_resource = 0  # float

    def __init__(self, message):
        self.__dict__ = message

    def get_base_cell(self):
        return Cell(x, y, CellType.BASE, None, None)


class CurrentState:
    around_cells = []  # List["Cell"]
    chat_box = []  # List["Message"]
    current_x = -1  # int
    current_y = -1  # int
    current_resource_type = None  # ResourceTypes
    current_resource_value = 0  # int
    health = 0  # int

    def __init__(self, message):
        self.__dict__ = message


class AntType(Enum):
    SARBAAZ = 0
    KARGAR = 1

    @staticmethod
    def get_value(string: str):
        if string == "SARBAAZ":
            return AntType.SARBAAZ
        if string == "KARGAR":
            return AntType.KARGAR
        return None


class Direction(Enum):
    CENTER = 0
    RIGHT = 1
    UP = 2
    LEFT = 3
    DOWN = 4

    @staticmethod
    def get_value(string: str):
        if string == "CENTER":
            return Direction.CENTER
        if string == "right":
            return Direction.RIGHT
        if string == "UP":
            return Direction.UP
        if string == "LEFT":
            return Direction.LEFT
        if string == "DOWN":
            return Direction.DOWN
        return None


class CellType(Enum):
    BASE = 0
    EMPTY = 1
    WALL = 2

    @staticmethod
    def get_value(string: str):
        if string == "BASE":
            return CellType.BASE
        if string == "EMPTY":
            return CellType.EMPTY
        if string == "WALL":
            return CellType.WALL
        return None


class ResourceType(Enum):
    BREAD = 0
    GRASS = 1

    @staticmethod
    def get_value(string: str):
        if string == "BREAD":
            return ResourceType.BREAD
        if string == "GRASS":
            return ResourceType.GRASS
        return None


class ServerConstants:
    KEY_INFO = "info"
    KEY_TURN = "turn"
    KEY_TYPE = "type"

    # CONFIG_KEY_IP = "ip"
    # CONFIG_KEY_PORT = "port"
    CONFIG_KEY_TOKEN = "token"

    MESSAGE_TYPE_INIT = "3"
    MESSAGE_TYPE_TURN = "4"
    MESSAGE_TYPE_KILL = "7"


class ServerMessage:
    def __init__(self, type, turn, info):
        self.type = type
        self.info = info
        self.turn = turn
