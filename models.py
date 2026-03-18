import random 

class Character:
  def __init__(self, name: str, level: int, life_points: int, mana: int):
    self._name = name
    self._level = level
    self._life_points = life_points
    self._mana = mana

  @property
  def name(self) -> str:
    return self._name
  
  @property
  def level(self) -> int:
    return self._level
  
  @property
  def life_points(self) -> int:
    return self._life_points
  
  @property
  def mana(self) -> int:
    return self._mana
  
  @mana.setter
  def mana(self, value: int) -> None:
      if value < 0:
        self._mana = 0
      else:
        self._mana = value

  @life_points.setter
  def life_points(self, value: int) -> None:
      if value < 0:
        self._life_points = 0
      else:
        self._life_points = value
  
  def is_alive(self) -> bool:
    return self.life_points > 0
  
  def take_damage(self, amount: int) -> None:
    self.life_points -= amount

class Ability:
  def __init__(self, name: str, damage: int, mana_cost: int):
    self._name = name
    self._damage = damage
    self._mana_cost = mana_cost

  @property
  def name(self) -> str:
    return self._name
  
  @property
  def damage(self) -> int:
    return self._damage
  
  @property
  def mana_cost(self) -> int:
    return self._mana_cost

  def use(self, caster: Character, target: Character) -> None:
    if caster.mana < self.mana_cost:
      print(f"{caster.name} is out of mana! Using basic attack!")
      target.take_damage(10)
      return
    
    caster.mana -= self.mana_cost
    target.take_damage(self.damage)
    
    print(f"{caster.name} used {self.name} on {target.name}, dealing {self.damage} damage!")

    if not target.is_alive():
      print(f"Game over! {caster.name} wins!")

class Hero(Character): 
    def __init__(self, name: str, level: int, life_points: int, mana: int, ability: Ability):
      super().__init__(name, level, life_points, mana)
      self._ability = ability

    def attack(self, target: Character) -> None:
      self._ability.use(self, target)

class Enemy(Character): 
    def __init__(self, name: str, level: int, life_points: int, mana: int, enemy_type: str):
      super().__init__(name, level, life_points, mana)
      self._enemy_type = enemy_type

    @property
    def enemy_type(self) -> str:
      return self._enemy_type
    
    @property
    def damage(self) -> int:
      return random.randint(self.level * 2, self.level * 6)
    
    def attack(self, target: Character) -> None:
      damage = self.damage
      target.take_damage(damage)
      print(f"{self.name} attacked {target.name}, dealing {damage} damage!")

      if not target.is_alive():
        print(f"Game over! {self.name} wins!")