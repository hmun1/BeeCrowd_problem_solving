def count_walks(n, row, col, memo):
    if n == 0:
        return 1  # If no steps are remaining, it's a valid walk
    
    if (n, row, col) in memo:
        return memo[(n, row, col)]
    
    count = 0

    # Iterate over the six possible moves
    moves = [(0, 1), (-1, 0), (-1, -1), (0, -1), (1, 0), (1, 1)]
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 2 * n and 0 <= new_col <= new_row:
            count += count_walks(n - 1, new_row, new_col, memo)

    memo[(n, row, col)] = count
    return count

def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Number of steps
        memo = {}  # Memoization dictionary
        result = count_walks(n, n, n, memo)
        print(result)

if __name__ == "__main__":
    main()
