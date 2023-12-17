def average(score, avg):
    second_score = 0
    avg = avg * 2
    second_score = avg - score
    print(second_score)

score = int(input())
avg = int(input())
if 0 <= score <= 100 and 0 <= avg <= 100:
    average(score, avg)