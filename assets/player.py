

__all__=["Player"]


class Player:
    def __init__(self,nickname,health,max_health,border) -> None:
        self.codename = "player"
        self.nickname = nickname
        self.health = health
        self.max_health = max_health
        self.border = border - 1
        self.x = 0
        self.y = 0

    def spawn(self):
        self.x = int(self.border/2)
        self.y = int(self.border/2)

    def move(self,dir):
        match dir:
            case "n" | "north":
                if self.x > 0:
                    self.x -= 1
                    print("Вы прошли на север")
                else:
                    print("Севернее живет чистое зло...")
            case "s" | "south":
                if self.x < self.border:
                    self.x += 1
                    print("Вы прошли на юг")
                else:
                    print("Южнее живет чистое зло...")
            case "w" | "west":
                if self.y > 0:
                    self.y -= 1
                    print("Вы прошли на запад")
                else:
                    print("Западнее живет чистое зло...")
            case "e" | "east":
                if self.y < self.border:
                    self.y += 1
                    print("Вы прошли на восток")
                else:
                    print("Восточнее живет чистое зло...")