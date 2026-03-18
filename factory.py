from models import Ability, Hero, Enemy

def create_ability(name: str):
  if name == "fireball":
    return Ability("Fireball", 50, 20)
  elif name == "hammer":
    return Ability("Hammer", 40, 22)
  elif name == "kamehameha":
    return Ability("Kamehameha", 60, 30)
  
  raise ValueError(f"Unknown ability: {name}")

def create_hero(name: str):
  if name == "batman":
    return Hero("Batman", 5, 100, 80, create_ability('fireball'))
  elif name == "thor":
    return Hero("Thor", 7, 160, 130, create_ability('hammer'))
  elif name == 'goku':
    return Hero("Goku", 8, 180, 150, create_ability('kamehameha'))
  
  raise ValueError(f"Unknown hero: {name}")

def create_joker():
  return Enemy("Joker", 4, 90, 50, "Clown")

def create_thanos():
  return Enemy("Thanos", 6, 110, 70, "God")

def create_freeza():
  return Enemy("Freeza", 8, 130, 80, "Alien")