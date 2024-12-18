import random

def dice(schnecke_steps, number_of_schnecke):
    random_number = random.randint(0, number_of_schnecke - 1)
    schnecke_steps[random_number] += 1
    return schnecke_steps

def check_winner(schnecke_steps):
    max_step = max(schnecke_steps)
    if max_step >= 8:
        return schnecke_steps.index(max_step)
    return None

def simulation(number_of_schnecke, dice, check_winner, head_start=0):
    schnecke_steps = [head_start] + [0] * (number_of_schnecke - 1)
    while True:
        schnecke_steps = dice(schnecke_steps, number_of_schnecke)
        winner = check_winner(schnecke_steps)
        if winner is not None:
            return winner