import random
import time

start_time = time.time()
schnecke = [range(6)]
schnecke_winner_list = [0] * 6

def wurfel(schnecke_steps):
    random_number = random.randint(0, 5)
    schnecke_steps[random_number] += 1
    return schnecke_steps

def check_winner(schnecke_steps):
    maximum_number = max(schnecke_steps)
    if maximum_number >= 8:
        return schnecke_steps.index(maximum_number)
    return None

def simulation():
    schnecke_steps = [0] * 6
    while True:
        schnecke_steps = wurfel(schnecke_steps)
        winner = check_winner(schnecke_steps)
        if winner is not None:
            return winner
    
for i in range(10000):
    winner = simulation()

    schnecke_winner_list[winner] += 1
print(schnecke_winner_list)

summ = sum(schnecke_winner_list)
relativ_frequency = [round(i/summ*100, 2) for i in schnecke_winner_list]
print(relativ_frequency)

end_time = time.time()

total_time = end_time - start_time

print(f"{total_time = :.2f}s")