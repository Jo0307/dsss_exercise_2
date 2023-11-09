import random


def random_num(min_num, max_num):
    """

    :return: The random number in range (min, max)
    :rtype: int


    """
    return random.randint(min_num, max_num)


def random_operator():
    """"
    Choose one arithmetic operator for calculate

    :return: The random arithmetic operator
    :rtype: float

    """
    return random.choice(['+', '-', '*'])


def func_num_operator(num_1, num_2, calcul_oper):
    """
    The name of create function with chosen random numbers and arithmetic operators
    Calculate the result of chosen random numbers and operator
    :Args:
    :param func_name: The name of create function
    :type func_name: string

    :retrun: The name of create function and The calculated result of function
    :rtype: string, int

    """
    func_name = f"{num_1} {calcul_oper} {num_2}"
    if calcul_oper == '+':
        func_res = num_1 + num_2
    elif calcul_oper == '-':
        func_res = num_1 - num_2
    else:
        func_res = num_1 * num_2
    return func_name, func_res


def math_quiz():
    """
    Calculate the score of math quiz und print it

    :param score: The score of the math quiz
    :type score : int

    :param total_quiz : The number of quizzes run
    :type total_quiz : int

    for _ in range(total_quiz) : run the quiz total_quiz times

    :param num_1: random number in range (1,10)
    :type num_1: int

    :param num_2: random number in range (1,5)
    :type num_2: int

    :param operator: choose one operator for calculate
    :type operator: float

    :param problem: The name of random create function
    :type problem: string

    :param correct_ans: The correct answer of problem
    :type correct_ans: int

    :unser_Ans: in terminal input

    :if unser_Ans is correct,
     score += 1 : score will be counted +1 according to correct mathquiz
     if not,
     go exception.

    """


    score = 0
    total_quiz = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_quiz):
        num_1 = random_num(1, 10)
        num_2 = random_num(1, 5)
        operator = random_operator()

        problem, correct_ans = func_num_operator(num_1, num_2, operator)
        print(f"\nQuestion: {problem}")
        user_Ans = input("Your answer: ")
        user_Ans = int(user_Ans)

        if user_Ans == correct_ans:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_ans}.")

    print(f"\nGame over! Your score is: {score}/{total_quiz}")


if __name__ == "__main__":
    math_quiz()
