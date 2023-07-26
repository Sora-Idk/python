import random


class Human:
    def __init__(self, pos_x=0, pos_y=0, health=10, speed=1, strength=1, facing=random.randint(1,4), weight=1,
                 inventory=None,):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        self.uuid = random.randint(0,5000)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = health
        self.speed = speed
        self.strength = strength
        self.facing = facing
        self.weight = weight


    def check_collision(self):
        pass

    def __str__(self):
        return f"[uuid:{self.uuid},health:{self.health},position:{self.pos_x, self.pos_y},speed:{self.speed},strength:{self.strength}" \
               f"facing:{self.facing},weight:{self.weight},inv:{self.inventory}]"

