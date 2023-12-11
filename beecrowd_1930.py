sum = 0
t1, t2, t3, t4 = map(int, input().split())
sum = t1 + t2 + t3 + t4
maximum_devices = sum - 3
print(maximum_devices)