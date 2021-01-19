class Graph:
    def __init__(self, nodes):
        self.nodes = nodes


class Node:
    def __init__(self, id):
        self.id = id
        self.owner = 0
        self.neighbours = []
        self.value = 1

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours

    def set_owner(self, ownerarmy_count = 0):
        self.owner = owner

    def set_id(self, id):
        self.id = id

    def set_value(self, value):
        self.value = value


class World:
    def __init__(self):
        self.total_turns = None
        self.turn_number = 0
        self.my_player = None
        self.enemy_player = None
        self.map = None
        self.scoreboard = []

    def handle_init_message(self, msg):
        pass

    def update_map(self, node_list):
        pass

    def set_players(self, my_player, enemy_player):
        self.my_player = my_player
        self.enemy_player = enemy_player

    def update_scoreboard(self):
        pass
        
class Player:
    def __init__(self, id):
        self.id = id
        self.player_nodes = []
        self.points = 0

    def move(self, src, dst, action_type):
        pass
