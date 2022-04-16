from utils import *

questions = load_questions()
statistics = {"points": 0, "correct": 0, "incorect": 0}
questions_total = count_all_questions(questions)
questions_used = 0

# цикл выполняется, пока число итераций не превысит общее количество вопросов
while questions_used < questions_total:
    show_fild(questions)
    user_input = input("Выберите категорию:\n")

    # возможность выйти из игры досрочно
    if user_input.lower() == "стоп":
        break

    questions_current = parse_input(user_input, questions)

    # если пользователь ввел некорректную категорию
    if not questions_current:
        print("Нет такого вопроса")
        continue

    category = questions_current.get("category")
    price = questions_current.get("price")
    question_text = questions_current.get("questions")
    question_answer = questions_current.get("answer")

    # вывод вопроса
    show_question(question_text)

    # ответ пользователя
    user_input = input()

    if user_input == question_answer:
        print("Ответ верный!")
        statistics["points"] += int(price)
        statistics["correct"] += 1
    else:
        print("Ответ неверный!")
        statistics["points"] -= int(price)
        statistics["incorect"] += 1

    # вопрос помечается как использованный
    questions[category][price]["asked"] = True

    # увеличиваем счетчик итераци1
    questions_used += 1

# вывод статистики и сохранение результата в файл
print()
show_stats(statistics)
save_results_to_file(statistics)
