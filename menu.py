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