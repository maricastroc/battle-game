from factory import create_hero, create_joker, create_thanos, create_freeza

def select_hero():
  print("Choose your hero:")
  print("1 - Batman")
  print("2 - Thor")
  print("3 - Goku")

  choice = input("> ")

  if choice == "1":
    return create_hero("batman")
  elif choice == "2":
    return create_hero("thor")
  elif choice == "3":
    return create_hero("goku")
  else:
    print("Invalid choice, try again.")
    return select_hero()
  
def select_enemy():
  print("\nChoose your enemy:")
  print("1 - Joker")
  print("2 - Thanos")
  print("3 - Freeza")

  choice = input("> ")

  if choice == "1":
    return create_joker()
  elif choice == "2":
    return create_thanos()
  elif choice == "3":
    return create_freeza()
  else:
    print("Invalid choice, try again.")
    return select_enemy()
  
hero = select_hero()
enemy = select_enemy()

print(f"\nYou chose {hero.name}!")
print(f"You will fight against {enemy.name}!")

while hero.is_alive() and enemy.is_alive():
  print(f"\n{hero.name}: {hero.life_points} HP | {hero.mana} Mana")
  print(f"{enemy.name}: {enemy.life_points} HP")

  action = input("\n1 - Attack (ability)\n2 - Basic attack\nq - Quit\n> ")

  if action == "1":
    hero.attack(enemy)

  elif action == "2":
    print(f"{hero.name} used a basic attack!")
    enemy.take_damage(10)

  elif action == "q":
    print("Game finished!")
    break

  else:
    print("Invalid action!")
    continue

  if enemy.is_alive():
    input("Press ENTER for enemy turn...")
    enemy.attack(hero)