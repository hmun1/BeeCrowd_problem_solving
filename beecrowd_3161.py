def check_fruit_preferences(sheldon_preferences, fruits_to_check):
    for sheldon_fruit in sheldon_preferences:
        reversed_sheldon_fruit = sheldon_fruit[::-1]
        found = any(sheldon_fruit in fruit or reversed_sheldon_fruit in fruit for fruit in fruits_to_check)

        if found:
            print(f"Sheldon come a fruta {sheldon_fruit}")
        else:
            print(f"Sheldon detesta a fruta {sheldon_fruit}")

if __name__ == "__main__":
    # Read the number of fruits liked by Sheldon and the number of fruits to be checked
    n, m = map(int, input().split())

    # Read Sheldon's fruit preferences
    sheldon_preferences = [input().lower() for _ in range(n)]

    # Read the list of fruits to be checked
    fruits_to_check = [input().lower() for _ in range(m)]

    # Check and print the results
    check_fruit_preferences(sheldon_preferences, fruits_to_check)
