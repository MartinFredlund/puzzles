import sys

input_data = sys.stdin.read().split()
iterator = iter(input_data)

length = int(next(iterator))
cost = int(next(iterator))
students = [int(x) for x in iterator]

max_val = 0
temp_val = 0

for i in range(length):
    temp_val += students[i] - cost
    if temp_val < 0:
        temp_val = 0
    max_val = max(temp_val, max_val)
print(max_val)
