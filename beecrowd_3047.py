def different_ages(mother, first_son, second_son, third_son):
    sons_total_age = first_son + second_son
    third_son = mother - sons_total_age
    if first_son > third_son and first_son > second_son:
        print(first_son)
    elif second_son > first_son and second_son > third_son:
        print(second_son)
    elif third_son > first_son and third_son > second_son:
        print(third_son)


# Read input
mother = int(input())
first_son = int(input())
second_son = int(input())
third_son = 0
if 40 <= mother <= 110 and 1 <= first_son < mother and 1 <= second_son < mother:    # input is valid or not
    different_ages(mother, first_son, second_son, third_son)                  # iterate the program