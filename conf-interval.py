#!/usr/bin/python3

# Identify the z-critical value needed for a given confidence interva

# n C% of samples, the parameter will be within z* standard errors of the sample statistic

# example:
# What value of z* should be used to construct a 95% confidence interval of a population mean?
# answer: 1.96

import scipy.stats
import math
import numpy


def mean():
    conf_interval = float(input("confidence interval (as decimal): "))
    significance_lvl = round(1 - conf_interval, 5)
    print(f"significance_level: {significance_lvl}")
    upper_lim = 1 - (significance_lvl / 2)
    print(f"{upper_lim= }")
    z = scipy.stats.norm.ppf(upper_lim)
    print(f"value of z needed: {z}")

def proportion():
    conf_interval = float(input("confidence interval % to calculate (as decimal): "))
    significance_lvl = round(1 - conf_interval, 5)
    print(f"significance_level: {significance_lvl}")
    upper_lim = 1 - (significance_lvl / 2)
    print(f"{upper_lim= }")
    z = scipy.stats.norm.ppf(upper_lim)
    print(f"value of z needed: {z}")
    n = float(input("sample size (n): "))  # 206
    p̂ = float(input("sample proportion of success (p̂): ")) / n
    print(f"{p̂=}")
    q_hat = 1 - p̂
    plus_minus = numpy.array([+1, -1])
    # s1 = sqrt((125 + 10 * sqrt(19)) / 366)
    # s2 = sqrt((125 - 10 * sqrt(19)) / 366)
    # s1, s2 = sqrt((125 + pm * 10 * sqrt(19)) / 366)
    upper_limit, lower_limit = p̂ + plus_minus * z * math.sqrt(p̂ * q_hat/ n)
    print("confidence interval:")
    print(f"{round(lower_limit, 3)=}")
    print(f"{round(upper_limit, 3)=}")

def main():
    mode = input("calculate confidence interval from population (m)ean or population (p)roportion? (p/m): ").lower().strip()
    match mode:
        case "p":
            proportion()
        case "m":
            mean()
        case _:
            print("secret 3rd option unavailable. choose m/p.")
            main()

if __name__ == "__main__":
    main()
