from classes import *

player_orange_0 = Player("Psyonix-Adam", semipro, unranked, 740, 2, 0, 1, 6)
player_orange_1 = Player("MintRhino", rocketeer, shooting_star, 560, 1, 2, 1, 7)
player_orange_2 = Player("[Psyonix] Jadkins", legend, challenger_elite, 130, 0, 0, 1, 1)

player_blue_0 = Player("Psyonix_Ben", semipro, challenger_elite, 730, 1, 1, 6, 1)
player_blue_1 = Player("corey", rocketeer, superstar, 380, 1, 1, 1, 1)
player_blue_2 = Player("Josh", rookie, challenger_elite, 200, 0, 0, 1, 2)

team_orange = Team(3, color_orange, [player_orange_0, player_orange_1, player_orange_2])
team_blue = Team(2, color_blue, [player_blue_0, player_blue_1, player_blue_2])

game = Game(team_blue, team_orange)
game.show()