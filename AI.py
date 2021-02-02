from random import randint

class AI():
    def do_turn(self, world):
        my_nodes = world.my_player.player_nodes
        for node in my_nodes:
            neighbours = node.neighbours
            if len(neighbours) > 0:
                destination = neighbours[randint(0, len(neighbours) - 1)]
                world.my_player.move(source, destination, randint(0,2)))
