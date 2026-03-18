from Novice import Novice

class Swordsman(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.str(5)
        self.vit(10)
        self.setHp(self.getHp() + self.getVit())

    def slashAttack(self, character):
        self.newDamage = self.getDamage() + self.getStr()
        character.reduceHp(self.newdamage)
        print(f"{self.getUsername()} performed Slash Attack! -{self.newdamage}")
