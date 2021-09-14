class Game_Node:
    Value: int
    Visited: bool
    def  __init__(self, pValue) -> None:
        self.Value = pValue
        self.Visited = False
    def __str__(self) -> str:
        return str(self.Value)