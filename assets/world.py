from uuid import uuid1

__all__=["Cell","Forest","Plains","Rocks","Mountains","World"]

class Cell:
    def __init__(self) -> None:
        self.uid = uuid1()
        self.biome = None

class Forest:
    def __init__(self) -> None:
        self.codename = "biome_forest"
        self.name = "Лес"
        self.last_spawn = 0
        self.struct_spawned = 0
        self.res_spawned = 0
        self.npcs = []
        self.structures = []
        self.resources = []

class Plains:
    def __init__(self) -> None:
        self.codename = "biome_plains"
        self.name = "Равнины"
        self.last_spawn = 0
        self.struct_spawned = 0
        self.res_spawned = 0
        self.npcs = []
        self.structures = []
        self.resources = []

class Rocks:
    def __init__(self) -> None:
        self.codename = "biome_rocks"
        self.name = "Скалы"
        self.last_spawn = 0
        self.struct_spawned = 1
        self.res_spawned = 0
        self.npcs = []
        self.structures = []
        self.resources = []

class Mountains:
    def __init__(self) -> None:
        self.codename = "biome_mountains"
        self.name = "Горы"
        self.last_spawn = 0
        self.struct_spawned = 1
        self.res_spawned = 0
        self.npcs = []
        self.structures = []
        self.resources = []

class World:
    def __init__(self,size:int) -> None:
        self.size = size
        self.cells = []
