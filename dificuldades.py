from utils import escreva

LEVELS = {
    "easy": {
        "lives": 3,
        "points_per_question": 10,
        "label": "🟢 Easy"
    },
    "medium": {
        "lives": 3,
        "points_per_question": 20,
        "label": "🟡 Medium"
    },
    "hard": {
        "lives": 3,
        "points_per_question": 30,
        "label": "🔴 Hard"
    }
}

def choose_difficulty() -> str | None:
    while True:
        escreva("\n🎯 CHOOSE DIFFICULTY\n")

        for i, key in enumerate(LEVELS, start=1):
            lvl = LEVELS[key]
            escreva(f"{i} - {lvl['label']}")
            escreva(f"{lvl['lives']} lives | {lvl['points_per_question']} pts/question\n")

        choice = input("Your choice (1/2/3 or B to go back): ").lower().strip()

        match choice:
            case "1":
                confirm_difficulty("easy")
                return "easy"
            case "2":
                confirm_difficulty("medium")
                return "medium"
            case "3":
                confirm_difficulty("hard")
                return "hard"
            case "b":
                escreva("↩️ Backing out...")
                return None
            case _:
                escreva("⚠️ Invalid choice. Please try again.")

def confirm_difficulty(diff: str) -> None:
    lvl = LEVELS[diff]
    escreva("\n✅ Difficulty selected!")
    escreva(lvl["label"])
    escreva(f"Lives: {lvl['lives']}")
    escreva(f"Points per question: {lvl['points_per_question']}")
    input("\nPress Enter to continue...")
