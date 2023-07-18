
__all__ = ["Tree","FallenTree","Stone","Rock"]


class Tree:
    def __init__(self) -> None:
        self.codename = "resource_tree"
        self.name = "Дерево"
        self.contains = [("item_log",2),("item_stick",7)]
        self.tool_level = 1

class FallenTree:
    def __init__(self) -> None:
        self.codename = "resource_fallen_tree"
        self.name = "Упавшее дерево"
        self.contains = [("item_stick",4)]
        self.tool_level = 0

class Stone:
    def __init__(self) -> None:
        self.codename = "resource_stone"
        self.name = "Камешек"
        self.contains = [("item_stone",2)]
        self.tool_level = 0

class Rock:
    def __init__(self) -> None:
        self.codename = "resource_stone"
        self.name = "Скала"
        self.contains = [("item_stone",15)]
        self.tool_level = 1