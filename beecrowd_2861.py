def question_answer(test_cases):
    i = 0
    while i != test_cases:         # ask question and print answer
        question = input().split()
        print('gzuz')
        i += 1
# Read input
test_cases = int(input())
if  2 <= test_cases <= 99:        # test case is valid or not?
    question_answer(test_cases)