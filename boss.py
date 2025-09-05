import random
from enemy import Enemy 

class Giant(Enemy):
    def attack(self):
        return random.randint(1, self.attack_power) * 6
        


        
    

