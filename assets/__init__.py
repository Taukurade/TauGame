from .items import *
from .npc import *
from .player import *
from .resources import *
from .storage import *
from .structure import *
from .world import *

import random




class Registry:
    def __init__(self) -> None:
        self.all = {x().codename:x for x in [
        Forest,Plains,Rocks,Mountains,Tree,FallenTree,
        Stone,Rock,Dirt,Log,Stick,Stone,Beef,CookedBeef,
        Pork,CookedPork,Fiber,Pig,Cow,Chicken,Spider,Wolf,Trader,Chest,Crate,PlayerInventory]}
        
        self.biomes = {x().codename:x for x in [Forest,Plains,Rocks,Mountains]}
        self.resources = {x().codename:x for x in [Tree,FallenTree,Stone,Rock]}
        self.items = {x().codename:x for x in [Dirt,Log,Stick,Stone,Beef,CookedBeef,Pork,CookedPork,Fiber]}
        self.npcs = {x().codename:x for x in [Pig,Cow,Chicken,Spider,Wolf,Trader]}
        self.structures = {x().codename:x for x in [AbandonedHouse,Village]}
        self.storages = {x().codename:x for x in [Chest,Crate,PlayerInventory]}


class Game:
    def __init__(self) -> None:
        self.current_step = 0
        self.registry = Registry()
        self.world = World(256)
        self.player = Player("Tau",100,100,self.world.size)
        
        self.commands = {
            "help":self.cmd_help,
            "wai":self.cmd_wai,
            "go":self.cmd_go,
            "move":self.cmd_go
        }
        
        
        self.generate_world()
        self.player.spawn()

        

    def cmd_help(self,*args):
        print()

    def cmd_wai(self,*args):
        cell = self.world.cells[self.player.x][self.player.y]
        print(f"Вы находитесь в биоме {cell.biome.name}")
        print(f"NPC неподалеку:")
        for npc in cell.biome.npcs:
            print(f"{npc.name} HP:{npc.health}/{npc.max_health} ATK:{npc.attack_damage}")
        print(f"Структуры неподалеку:")
        for structure in cell.biome.structures:
            print(f"{structure.name}")
        print(f"Ресурсы неподалеку:")
        for res in cell.biome.resources:
            print(res.name)

    def cmd_go(self,*dir):
        self.player.move(dir[0])



    def generate_world(self):
        self.world.cells = []
        for x in range(0,self.world.size):
            self.world.cells.append([])
            for y in range(0,self.world.size):
                cell = Cell()
                cell.biome = random.choice(list(self.registry.biomes.items()))[1]()
                self.world.cells[x].append(cell)

    def spawn_npc(self):
        if self.world.cells[self.player.x][self.player.y].biome.last_spawn <= self.current_step:
            match self.world.cells[self.player.x][self.player.y].biome.codename:
                case "biome_forest" | "biome_plains":
                    for a in range(0,random.choice(range(1,8))):
                        self.world.cells[self.player.x][self.player.y].biome.npcs.append(random.choice([Pig,Cow,Chicken])())
                        self.world.cells[self.player.x][self.player.y].biome.last_spawn += 100
                case "biome_rocks":
                    for a in range(0,random.choice(range(1,8))):
                        self.world.cells[self.player.x][self.player.y].biome.npcs.append(random.choice([Pig,Cow,Spider])())
                        self.world.cells[self.player.x][self.player.y].biome.last_spawn += 100
                case "biome_mountains":
                    for a in range(0,random.choice(range(1,8))):
                        self.world.cells[self.player.x][self.player.y].biome.npcs.append(random.choice([Cow,Wolf,Spider])())
                        self.world.cells[self.player.x][self.player.y].biome.last_spawn += 100
    def spawn_structures(self):
        if self.world.cells[self.player.x][self.player.y].biome.struct_spawned == 0:
            self.world.cells[self.player.x][self.player.y].biome.structures.append(random.choice(list(self.registry.structures.items()))[1]())
            self.world.cells[self.player.x][self.player.y].biome.struct_spawned = 1
    def spawn_resources(self):
        if self.world.cells[self.player.x][self.player.y].biome.res_spawned == 0:
            match self.world.cells[self.player.x][self.player.y].biome.codename:
                case "biome_forest" | "biome_plains":
                    for a in range(0,random.choice(range(1,8))):
                        self.world.cells[self.player.x][self.player.y].biome.resources.append(random.choice([Tree,FallenTree,Stone])())
                        self.world.cells[self.player.x][self.player.y].biome.res_spawned = 1
                case "biome_rocks" | "biome_mountains":
                    for a in range(0,random.choice(range(1,8))):
                        self.world.cells[self.player.x][self.player.y].biome.resources.append(random.choice([Stone,Rock])())
                        self.world.cells[self.player.x][self.player.y].biome.res_spawned = 1


    def gameloop(self):
        self.spawn_npc()
        self.spawn_resources()
        self.spawn_structures()
        cmd = input(">")
        cmd = cmd.split(" ")
        if cmd[0] in self.commands.keys():
            if len(cmd) >= 2:
                self.commands[cmd[0]](cmd[1])
            else:
                self.commands[cmd[0]]()
        else:
            print("такого действия нет")
        self.gameloop()