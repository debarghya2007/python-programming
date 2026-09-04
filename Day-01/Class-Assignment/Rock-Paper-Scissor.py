import random

MOVES = ["Rock", "Paper", "Scissors"]

def play_round(player_move: str, computer_move: str) -> str:
    
    #Determines the round winner using standard Rock-Paper-Scissors rules.
    
    p_move = player_move.capitalize()
    c_move = computer_move.capitalize()

    if p_move == c_move:
        return "Draw"
    
    # Winning conditions for the player
    if (
        (p_move == "Rock" and c_move == "Scissors") or
        (p_move == "Paper" and c_move == "Rock") or
        (p_move == "Scissors" and c_move == "Paper")
    ):
        return "Player Wins"
    else:
        return "Computer Wins"


def main():
    total_rounds = 5
    history = []
    wins = 0
    losses = 0
    draws = 0

    print("=== Welcome to the College Coding Arcade: Rock-Paper-Scissors ===")
    print(f"Playing a {total_rounds}-round match!\n")

    for round_num in range(1, total_rounds + 1):
        # Prompt for player input with basic validation
        while True:
            user_input = input(f"Round {round_num} - Enter move (Rock, Paper, Scissors): ").strip()
            if user_input.capitalize() in MOVES:
                player_move = user_input.capitalize()
                break
            print("Invalid move! Please enter Rock, Paper, or Scissors.")

        # Generate computer move
        computer_move = random.choice(MOVES)

        # Evaluate round
        result = play_round(player_move, computer_move)
        print(f"Computer chose: {computer_move}")
        print(f"Outcome: {result}\n")

        # Track statistics
        if result == "Player Wins":
            wins += 1
        elif result == "Computer Wins":
            losses += 1
        else:
            draws += 1

        # Record round details for summary table
        history.append({
            "round": round_num,
            "player": player_move,
            "computer": computer_move,
            "result": result
        })

    # Display final formatted summary table
    print("=" * 55)
    print(f"{'Round':<8} | {'Player Move':<12} | {'Computer Move':<13} | {'Result':<13}")
    print("-" * 55)
    for record in history:
        print(f"{record['round']:<8} | {record['player']:<12} | {record['computer']:<13} | {record['result']:<13}")
    print("=" * 55)

    # Calculate and display statistics
    win_percentage = (wins / total_rounds) * 100
    print(f"\nFinal Summary (after {total_rounds} rounds)")
    print(f"Wins: {wins} | Losses: {losses} | Draws: {draws} | Win % = {win_percentage:.1f}%")


if __name__ == "__main__":
    main()
