def monty_hall_simulation(num_games):
    wins = 0

    for i in range(num_games):
        player_choice = int(input())
        # Check if the player won (car is behind their final choice)
        if player_choice == 1 :
            pass
        else:
            wins += 1

    print(wins)

# Number of simulations
num_simulations = int(input())

# Run the simulation
monty_hall_simulation(num_simulations)
