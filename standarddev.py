import math
import numpy as np
import statistics

# string = input("enter list:\n")
# list1 = string.split()
# list1 = [int(n) for n in list1]
# print(f"list: {list1}")

# stddev = statistics.stdev(list1)
# print(f"{stddev=}")
# mean = (sum(list1)/len(list1))
# print(f"{mean=}")


# Define the dataset
x = np.array([2,4,1,6,7])
y = np.array([4,5,3,4,9])
correl = np.corrcoef(x, y)

print(f"correlation: {correl[0]}")
print(type(correl))
