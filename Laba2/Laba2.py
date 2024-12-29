from abc import ABC, abstractmethod

class GameObject(ABC):
    def __init__(self, id, name, x, y):
        self._id = id
        self._name = name
        self._x = x
        self._y = y

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getX(self):
        return self._x

    def getY(self):
        return self._y

class Unit(GameObject):
    def __init__(self, id, name, x, y, hp):
        super().__init__(id, name, x, y)
        self._hp = hp

    def isAlive(self):
        return self._hp > 0

    def getHp(self):
        return self._hp

    def receiveDamage(self, damage):
        self._hp = max(0, self._hp - damage)

class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass

class Moveable(ABC):
    @abstractmethod
    def move(self, dx, dy):
        pass

class Archer(Unit, Attacker, Moveable):
    def __init__(self, id, name, x, y, hp, damage):
        super().__init__(id, name, x, y, hp)
        self._damage = damage

    def attack(self, unit):
        if isinstance(unit, Unit) and unit.isAlive():
            unit.receiveDamage(self._damage)

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

class Building(GameObject):
    def __init__(self, id, name, x, y, built):
        super().__init__(id, name, x, y)
        self._built = built

    def isBuilt(self):
        return self._built

class Fort(Building, Attacker):
    def __init__(self, id, name, x, y, built, damage):
        super().__init__(id, name, x, y, built)
        self._damage = damage

    def attack(self, unit):
        if isinstance(unit, Unit) and unit.isAlive():
            unit.receiveDamage(self._damage)

class MobileHome(Building, Moveable):
    def move(self, dx, dy):
        self._x += dx
        self._y += dy

# Example usage
archer = Archer(1, "Archer", 0, 0, 100, 15)
fort = Fort(2, "Fort", 10, 10, True, 30)
mobile_home = MobileHome(3, "MobileHome", 5, 5, True)

archer.attack(archer)  # Archer attacking itself as a test
print(archer.getHp())
