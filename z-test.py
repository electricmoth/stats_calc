#!/usr/bin/python3

"""
Approximately 10% of the population is left-handed, with a standard deviation of 3.13%. Of 100 randomly selected people, 14 claimed to be left-handed.
Find the z-test statistic for this data set.
"""

import math

#    Population proportion of successes (p)
#    Population proportion of failures (1-p = q)
#    Sample proportion of successes (p̂)
#    Sample size (n)


def main ():
    # p̂ = 0.14
    # p̂ = 0.14
    # q = 0.90
    # p = 0.10
    p = float(input("Population proportion of successes (p)\n (e.g.: An article claims that 12% of trees are... ): "))
    q = 1 - p
    p̂ = float(input("Sample proportion of successes (p̂): "))
    n = float(input("Sample size (n): "))
    z = (p̂ - p)/ math.sqrt(p * q / n)
    print(f"z-test statistic: {z}")


if __name__ == "__main__":
    main()

