# I will try to code a turn based rpg rogue-lite game (text based).
GAME_VERSION = '0.1'

class Entity:
    def __init__(self, name, health, magic, level, cards):
        self.name   = name
        self.health = health
        self.magic  = magic
        self.level  = level
        self.cards  = cards

    def set_name(self, name):
        self.name = name

    def set_health(self, health):
        self.health = health
    
    def set_magic(self, magic):
        self.magic = magic

    def set_level(self, level):
        self.level = level

    def set_cards(self, cards):
        self.cards = cards

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health
    
    def get_magic(self):
        return self.magic

    def get_level(self):
        return self.level

    def get_cards(self):
        return self.cards

    def display(self):
        print(f'[Name: {self.name}] [HP: {self.health}] [MP: {self.magic}] [LVL: {self.level}]')
        print(f'Cards: {self.cards}\n')

player  = Entity('Ethereum', 10, 10, 1, ['Fireball', 'Ice Shard', 'Heal', 'Weaken', 'Defense Up'])
monster = Entity('XR Pee'  , 20,  5, 1, ['Fireball II', 'Demon Stone', 'Cannibalism', 'Attack Up', 'Defense Up'])

print(f'Monsters v{GAME_VERSION}\n')

player.display()
monster.display()
player.set_health(200)
player.set_magic(50)
player.set_level(2)
player.display()
print(player.get_cards())

#class Cards:

#class Game:

