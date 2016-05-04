from enum import Enum


class Rank():
    def __init__(self, name, level):
        self.name = name
        self.level = level


unranked = Rank("Unranked", 0)
prospect_1 = Rank("Prospect I", 1)
prospect_2 = Rank("Prospect II", 2)
prospect_3 = Rank("Prospect III", 3)
prospect_elite = Rank("Prospect Elite", 4)
challenger_1 = Rank("Challenger I", 5)
challenger_2 = Rank("Challenger II", 6)
challenger_3 = Rank("Challenger III", 7)
challenger_elite = Rank("Challenger Elite", 8)
rising_star = Rank("Rising Star", 9)
shooting_star = Rank("Shooting Star", 10)
all_star = Rank("All-Star", 11)
superstar = Rank("Superstar", 12)
champion = Rank("Champion", 13)
super_champion = Rank("Super Champion", 14)
grand_champion = Rank("Grand Champion", 15)


# class Ranks(object):
#     unranked = 0
#     prospect_1 = 1
#     prospect_2 = 2
#     prospect_3 = 3
#     prospect_elite = 4
#     challenger_1 = 5
#     challenger_2 = 6
#     challenger_3 = 7
#     challenger_elite = 8
#     rising_star = 9
#     shooting_star = 10
#     all_star = 11
#     superstar = 12
#     champion = 13
#     super_champion = 14
#     grand_champion = 15


class Levels(Enum):
    rookie = 0
    semipro = 1
    pro = 2
    veteran = 3
    expert = 4
    master = 5
    legend = 6
    rocketeer = 7


color_blue = "Blue"
color_orange = "Orange"


class Player:
    def __init__(self, name, level, rank, score, goals, assists, saves, shots):
        self.name = name
        self.level = level
        self.rank = rank
        self.score = score
        self.goals = goals
        self.assists = assists
        self.saves = saves
        self.shots = shots


class Team:
    def __init__(self, score, color, players):
        self.score = score
        self.color = color
        self.players = players


class Game:
    def __init__(self, team_0, team_1):
        self.winner, self.loser = (team_0, team_1) if team_0.score > team_1.score else (
            team_1, team_0)

    def show(self):
        print("================================= WINNER ================================")
        Game.show_team(self.winner)
        print("================================= LOSER =================================")
        Game.show_team(self.loser)

    @staticmethod
    def show_team(t):
        print("{}{:>10}".format(t.score, t.color.upper()))
        print("{:>25}{:>10}{:>10}{:>10}{:>10}".format("SCORE", "GOALS", "ASSISTS", "SAVES", "SHOTS"))
        for p in t.players:
            print("{:<20}{:<10}{:<10}{:<10}{:<10}{:<10}".format(p.name, p.score, p.goals, p.assists, p.saves, p.shots))
