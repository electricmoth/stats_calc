#!/usr/bin/python3

# Find a P-Value from a Z-Test Statistic
# example:
# Kristy randomly samples the out-of-state tuition and fees for 25 public universities and found a mean of $20,876 with a standard deviation of $2,494.
# Using the alternative hypothesis that µ < $21,706, Kristy found a z test statistic of -1.66.
# Given the data provided, what is the p-value of the z-test statistic?

import math
from scipy.stats import norm


class info:
    def __init__(self):
        self.p_value = None
        self.z_score = input("z-score given? (y/n): ").lower().strip()

    def left(self):
        if self.z_score != "n":
            self.z_score = float(input("enter z-score: "))
        else:
            p̂ = float(input("sample proportion of success (p̂): ")) / 1000
            p = float(input("population proportion of success (p̂) (% as decimal): "))
            q = 1 - p
            n = float(input("sample size (n): "))
            self.z_score = (p̂ - p) / math.sqrt(p*q / n)
            print(f"z-score: {self.z_score}")
        self.p_value = norm.cdf(self.z_score)
        print(f"p_value for left-tail test: {self.p_value} or {self.p_value * 100}%.")


    def right(self):
        x̅ = float(input("sample mean (x̅): "))
        μ = float(input("population mean (μ): "))
        σ = float(input("sample std dev (σ): "))
        n = float(input("sample size (n): "))
        self.z_score = (x̅ - μ) / (σ / math.sqrt(n))
        print(f"z-score: {self.z_score}")
        self.p_value = 1 - norm.cdf(self.z_score)
        print(f"p_value for right-tail test: {self.p_value} or {self.p_value * 100}%.")
        print(f"p_value: {self.p_value}")

    def two_tail(self):
        x̅ = float(input("sample mean (x̅): "))
        μ = float(input("population mean (μ): "))
        σ = float(input("sample std dev (σ): "))
        n = float(input("sample size (n): "))
        self.z_score = (x̅ - μ) / (σ / math.sqrt(n))
        print(f"z-score: {self.z_score}")
        # times 2 because two-tailed test
        self.p_value = norm.cdf(self.z_score) * 2
        print(f"p_value for two-tail test: {self.p_value} or {self.p_value * 100}%.")


def main():
    print("- (r)ight tail (HA > μ) \n- (l)eft tail (HA < p)\n- (t)wo-tail (HA != μ)\n")
    mode = input("\nmode (r/l/t): ")
    print(f"mode: {mode}\n")
    i = info()

    match mode:
        case "r":
            i.right()
        case "l":
            i.left()
        case "t":
            i.two_tail()

        case _:
            print("invalid choice")
            main()


if __name__ == "__main__":
    main()

