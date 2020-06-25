class PlayerCharacter:
    membership = True

    def __init__(self, value):
        super().__init__()
        self.membership = value


player = PlayerCharacter(True)
print(player.membership)

player2 = PlayerCharacter(False)
print(player2.membership)

print(player.membership)