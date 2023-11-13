import unittest
from math_quiz import random_num, random_operator, func_num_operator


class TestMathGame(unittest.TestCase):

    def random_num_generator(self):
        """
        Test if random numbers generated are within the specified range
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_num(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def random_oper_generator(self):
        """
        Test if operator from random operator generated are +,-,*.
        """
        for _ in range(1000):
            rand_oper = random_operator()
            self.assertTrue(rand_oper == '+' or rand_oper == '-' or rand_oper == '*')



    def test_case(self):
        """
        Test if fun_num_operator give correct function and answer. Check those value with few test cases
        """
        test_cases = (

            [5, 2, '+', '5 + 2', 7],
            [6, 7, '+', '6 + 7', 13],
            [8, 3, '-', '8 - 3', 5],
            [2, 4, '*', '2 * 4', 8],
            [7, 4, '-', '7 - 4', 3],
            [4, 5, '*', '4 * 5', 20],
            [2, 4, '-', '2 - 4', -2]


        )

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, correct_ans = func_num_operator(num1, num2, operator)
            self.assertTrue(expected_problem == problem)
            self.assertTrue(expected_answer == correct_ans)


if __name__ == "__main__":
    unittest.main()
