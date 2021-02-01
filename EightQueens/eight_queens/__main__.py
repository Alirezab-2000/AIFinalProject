from eight_queens.simulatedAnnealingAlgoritm import SimulatedAnnealing


if __name__ == "__main__":
    algoritm = SimulatedAnnealing()
    algoritm.randomStart()

    print("")
    print("algoritm started...")
    print("")

    algoritm.saAlgoritm()