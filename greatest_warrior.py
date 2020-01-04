#!python3.8.0
# -*-encoding:utf-8-*-


class Warrior:
    ranks = ("Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage",
             "Elite", "Conqueror", "Champion", "Master","Greatest")

    def __init__(self):
        self.experience = 100
        self.achievements = []

    def gained_experience(self, experience):
        if self.experience + experience <= 10000:
            self.experience += experience
        else:
            self.experience = 10000

    @property
    def level(self):
        return self.experience // 100

    @property
    def rank(self):
        return self.ranks[self.level // 10]

    def battle(self, enemy_level):
        if 1 <= self.level <= 100:
            if enemy_level - self.level >= 5:
                return "You have been defeated"
            else:
                if self.level == enemy_level:
                    self.gained_experience(10)
                    return "A good fight! You won!!!"
                elif self.level - enemy_level == 1:
                    self.gained_experience(5)
                    return "A good fight! You won!"
                elif self.level - enemy_level >= 2:
                    return "Easy fight! You won!!!"
                elif enemy_level - self.level >= 1:
                    self.gained_experience(20 * (enemy_level - self.level) ** 2)
                    return "An intense fight!"
        return "Invalid level"

    def training(self, training_name, experience, required_level):
        if self.level >= required_level:
            self.gained_experience(experience)
            self.achievements.append(training_name)
            return training_name
        else:
            return "Not strong enough"

    def print_status(self):
        print("Level:", self.level)
        print("Experience:", self.experience)
        print("Rank:", self.rank)
        print("Achievements:", self.achievements)


if __name__ == "__main__":
    print('\n______________________________________________________________________________________________________\n')
    bruce_lee = Warrior()
    bruce_lee.print_status()

    print('\n______________________________________________________________________________________________________\n')
    print(bruce_lee.training("Defeated Chuck Norris", 9000, 1))
    bruce_lee.print_status()

    print('\n______________________________________________________________________________________________________\n')
    print(bruce_lee.battle(90))
    bruce_lee.print_status()

    print('\n_______________________________________________________________________________________________________\n')
