class player:
  
  def __init__(self, Name, Health, Magic_Points, Lives, Alive):

    self.Name = Name
    self.Health = Health
    self.Magic_Points = Magic_Points
    self.Lives = Lives
    self.Alive = Alive

  def print(self):
    print("Generic RPG")
    print()
    print(f"{self.Name}  {self.Health}  {self.Magic_Points}")
    print(f"{self.Lives}  {self.Alive}")
    print()


class Boris(player):

  def __init__(self, Name: str, Health, Magic_Points, Type, Strength, DayorNight):

    self.Name = "Boris"
    self.Health = Health
    self.Magic_Points = Magic_Points
    self.Type = Type
    self.Strength = Strength
    self.DayorNight = DayorNight

  def print(self):
    print("Generic RPG")
    print()
    print(f"{self.Name}  {self.Health}  {self.Magic_Points}")
    print(f"{self.Type}  {self.Strength}  {self.DayorNight}")
    print()


class Rishi(player):

  def __init__(self, Name, Health, Magic_Points, Type, Strength, DayorNight):

    self.Name = "Rishi"
    self.Health = Health
    self.Magic_Points = Magic_Points
    self.Type = Type
    self.Strength = Strength
    self.DayorNight = DayorNight

  def print(self):
    print("Generic RPG")
    print()
    print(f"{self.Name}  {self.Health}  {self.Magic_Points}")
    print(f"{self.Type}  {self.Strength}  {self.DayorNight}")
    print()


class Bill(player):

  def __init__(self, Name, Health, Magic_Points, Type, Strength, Speed):

    self.Name = "Bill"
    self.Health = Health
    self.Magic_Points = Magic_Points
    self.Type = Type
    self.Strength = Strength
    self.Speed = Speed

  def print(self):
    print("Generic RPG")
    print()
    print(f"{self.Name}  {self.Health}  {self.Magic_Points}")
    print(f"{self.Type}  {self.Strength}  {self.Speed}")
    print()


class Ted(player):

  def __init__(self, Name, Health, Magic_Points, Type, Strength, Speed):

    self.Name = "Ted"
    self.Health = Health
    self.Magic_Points = Magic_Points
    self.Type = Type
    self.Strength = Strength
    self.Speed = Speed

  def print(self):
    print("Generic RPG")
    print()
    print(f"{self.Name}  {self.Health}  {self.Magic_Points}")
    print(f"{self.Type}  {self.Strength}  {self.Speed}")
    print()


class Station(player):

  def __init__(self, Name, Health, Magic_Points, Type, Strength, Speed):

    self.Name = "Station"
    self.Health = Health
    self.Magic_Points = Magic_Points
    self.Type = Type
    self.Strength = Strength
    self.Speed = Speed

  def print(self):
    print("Generic RPG")
    print()
    print(f"{self.Name}  {self.Health}  {self.Magic_Points}")
    print(f"{self.Type}  {self.Strength}  {self.Speed}")
    print()



David = player("David", 100, 50, 3, "Yes")
David.print()

Boris = Boris("Boris", 45,70,"Vampire",3,"Night")
Boris.print()

Rishi = Rishi("Rishi",70, 10, "Vampire", 75, "Day")
Rishi.print()

Bill = Bill("Bill",60, 5, "Orc", 75, 90)
Bill.print()

Ted = Ted( "Ted",75, 40, "Orc", 75, 90)
Ted.print()

Station = Station("Station",35, 40, "Orc", 49, 50)
Station.print()