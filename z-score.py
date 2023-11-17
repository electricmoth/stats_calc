# solves problems such as "If the average score is 122 with a standard deviation of 35, what percentage of students scored below 67?"
# given = 67
# mean = 122
# std_dev = 35

given = int(input("given value: "))
mean = int(input("mean: "))
std_dev = int(input("std deviation: "))

z_score = ( given - mean ) / std_dev
print(f"z_score: {z_score}.")


