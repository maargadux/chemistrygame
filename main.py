# main.py

from menu import show_menu
from dificuldades import choose_difficulty, LEVELS
from levels import play_level
from questions import EASY_QUESTIONS, MEDIUM_QUESTIONS, HARD_QUESTIONS
from utils import escreva, leaving_the_game
from data import load_game, show_ranking

QUESTIONS_BY_LEVEL = {
    "easy": EASY_QUESTIONS,
    "medium": MEDIUM_QUESTIONS,
    "hard": HARD_QUESTIONS
}

def start_level(difficulty):
    escreva(f"\n🎮 Starting {difficulty.upper()} level...\n")
    play_level(
        QUESTIONS_BY_LEVEL[difficulty],
        difficulty
    )
    input("\nPress Enter to return to menu...")

def start_game():
    while True:
        show_menu()
        escolha = input("\nChoose an option: ").strip()

        if escolha == "1":
            diff = choose_difficulty()

            if diff not in LEVELS:
                escreva("🤔 No difficulty selected. Try again.")
                input("\nPress Enter to continue...")
                continue

            start_level(diff)

        elif escolha == "2":
            escreva("📂 Loading saved game...")
            load_game()
            input("\nPress Enter to continue...")

        elif escolha == "3":
            escreva("\n🏆 Ranking\n")
            show_ranking()
            input("\nPress Enter to continue...")
        elif escolha == "4":
            escreva("About the chemistry quiz game:")
            escreva("This is a simple quiz game made to help you practice basic chemistry concepts.")
            escreva("You will face multiple-choice questions with options from A to D.")
            escreva("Each correct answer gives you points.")
            escreva("Each wrong answer costs you one life.")
            escreva("You start with 3 lives.")
            escreva("If you lose all your lives, the game is over.")
            escreva("The game has three levels: easy, medium, and hard.")
            escreva("The objective is to have fun and learn at the same time.")
            escreva("Thank you for playing my game, and I hope you enjoy it!")
            escreva("See you next time! By: m4L1")
            input("Press Enter to continue...")

        elif escolha == "5":
            leaving_the_game()
            break

        else:
            escreva("❌ Invalid option. Please choose a valid number.")

if __name__ == "__main__":
    start_game()
