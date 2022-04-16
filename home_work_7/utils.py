import json
import math


# подсчет общего количества вопросов
def count_all_questions(questions):
    count = 0
    for category in questions.values():
        count += len(category)
    return count


# загрузка словаря с вопросами и ответами из файла
def load_questions():
    with open("questions.json", encoding='utf-8') as file:
        questions = json.load(file)
    return questions


# вывод игрового поля
def show_fild(questions):
    headlines = questions.keys()
    for k in headlines:
        print(k.ljust(12), end='')
        cat_questions = questions[k]
        for question_price, question_data in cat_questions.items():
            if question_data["asked"]:
                print(' ' * 3, end='   ')
            else:
                print(question_price, end='   ')
        print()


# обработка выбора пользователем категории
def parse_input(user_input, questions_received):
    user_input_parsed = user_input.split()
    if len(user_input_parsed) != 2:
        return False
    category = user_input_parsed[0].title()
    price = user_input_parsed[1]
    if category not in questions_received:
        return False
    category_from_questions = questions_received[category]
    if price not in category_from_questions:
        return False
    questions_data = category_from_questions[price]
    if questions_data["asked"]:
        return False
    question_text = questions_data["questions"]
    question_answer = questions_data["answer"]
    return {"category": category, "price": price, "questions": question_text, "answer": question_answer}


# вывод вопроса
def show_question(question_text):
    print(f"Слово {question_text} в переводе означает ...")


# вывод статистики по итогам игры
def show_stats(statistics):
    print("У нас закончились вопросы!")
    print()
    print(f"Ваш счет: {statistics['points']}")
    print(f"Верных ответов: {statistics['correct']}")
    print(f"Неверных ответов: {statistics['incorect']}")


# сохранение результатов в файл
def save_results_to_file(statistics):
    file_name = "records.json"
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(statistics, file, ensure_ascii=False)
