from utils import simulation, dice, check_winner
from parameters import NUMBER_OF_SCHNECKE, NUMBER_OF_SIMULATIONS, HEAD_STARTS

def main():

    for head_start in HEAD_STARTS:
        schnecke_winner_list = [0] * NUMBER_OF_SCHNECKE
        for _ in range(NUMBER_OF_SIMULATIONS):
            winner = simulation(NUMBER_OF_SCHNECKE, dice, check_winner, head_start)
            schnecke_winner_list[winner] += 1

        relative_frequency = [round(winner/NUMBER_OF_SIMULATIONS*100, 2) for winner in schnecke_winner_list]
        print("-"*10)
        print(f"Vorspung für Schnecke_0: {head_start}")
        print(f"Absolute Häufigkeit {schnecke_winner_list}")
        print(f"Relative Häufigkeit {relative_frequency}%")
    return

if __name__ == '__main__':
    main()