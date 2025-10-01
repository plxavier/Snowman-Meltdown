from game_logic import play_game, ask_replay

def main():
    """main function to play and replay snowman and keep tally"""
    play_count = 0
    wins = 0

    while True:
        play_count += 1
        print(f"Playing game number {play_count} of snowman game")

        won = play_game()
        if won:
            wins += 1

        print(f"Wins: {wins}")

        if not ask_replay():
            break

    print("*" * 60)
    print("Thanks for playing Snowman-Meltdown!")
    print(f"Final stats: You won {wins} out of {play_count} snowman games")
    print("Hope you enjoyed!")
    print("*" * 60)

if __name__ == "__main__":
    main()