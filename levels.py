from utils import escreva

def play_level(questions, config):
    vidas = config["lives"]
    pontos = 0
    pontos_por_questao = config["points_per_question"]

    total = len(questions)

    for index, q in enumerate(questions, start=1):
        escreva("\n" + "-" * 40)
        escreva(f"Question {index}/{total}")
        escreva(f"Lives: {vidas} | Score: {pontos}")
        escreva("-" * 40 + "\n")

        escreva(q["question"])

        for i, option in enumerate(q["options"]):
            escreva(f"{chr(97+i)}) {option}")

        resposta = input("\nYour answer (a/b/c/d): ").strip().lower()

        while resposta not in ["a", "b", "c", "d"]:
            resposta = input("Choose a valid option (a/b/c/d): ").strip().lower()

        if resposta == q["answer"]:
            escreva("✅ Correct!")
            pontos += pontos_por_questao
        else:
            vidas -= 1
            escreva("❌ Incorrect!")
            escreva(f"Correct answer: {q['answer']}")
            escreva(f"Lives left: {vidas}")

        if vidas == 0:
            escreva("\n💀 GAME OVER")
            escreva(f"Final score: {pontos}")
            input("\nPress Enter to continue...")
            return pontos

        input("\nPress Enter for the next question...")

    escreva("\n🎉 LEVEL COMPLETED!")
    escreva(f"Final score: {pontos}")
    input("\nPress Enter to continue...")
    return pontos
