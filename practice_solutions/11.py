"""
Ask number of games played in a tournament. Ask the user number of games won and number of games loss. Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)
"""
games_played = int(input("Enter the total number of games played in tournament= "))
games_won = int(input("Enter the number of games won in tournament= "))
games_loss = int(input("Enter the number of games loss in tournament= "))
games_tie = games_played - games_won - games_loss
total_points = games_won * 4 + games_tie * 2
print(f"Number of games tie in tournament is {games_tie}")
print(f"Number of total points is {total_points}")
