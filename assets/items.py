
__all__ = ["Dirt","Log","Stick","Stone","Beef","CookedBeef","Pork","CookedPork","Fiber"]


class Dirt:
    def __init__(self) -> None:
        self.codename = "item_dirt"
        self.name = "Горсть земли"
        self.stack = 16

class Log:
    def __init__(self) -> None:
        self.codename = "item_log"
        self.name = "Бревно"
        self.stack = 2

class Stick:
    def __init__(self) -> None:
        self.codename = "item_wooden_stick"
        self.name = "Деревянная палка"
        self.stack = 30

class Stone:
    def __init__(self) -> None:
        self.codename = "item_stone"
        self.name = "Камень"
        self.stack = 12

class Beef:
    def __init__(self) -> None:
        self.codename = "item_beef"
        self.name = "Говядина"
        self.stack = 6

class Pork:
    def __init__(self) -> None:
        self.codename = "item_pork"
        self.name = "Свиниа"
        self.stack = 6

class CookedPork:
    def __init__(self) -> None:
        self.codename = "item_cooked_pork"
        self.name = "Приготовленная свиниа"
        self.stack = 6

class CookedBeef:
    def __init__(self) -> None:
        self.codename = "item_cooked_beef"
        self.name = "Приготовленная говядина"
        self.stack = 6

class Fiber:
    def __init__(self) -> None:
        self.codename = "item_fiber"
        self.name = "Нить"

