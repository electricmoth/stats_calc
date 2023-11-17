#!/usr/bin/python3

# calculate standard error for a sample proportion

import math

def main():
    std_dev = input("std deviation known? (y/N): ").lower().strip()
    if std_dev != "y":
        # calculate std_err when std deviation not known
        n = float(input("sample size (n): "))
        p̂ = float(input("sample proportion of success (p̂): ")) / n
        print(f"p̂: {round(p̂, 3)}")
        q_hat = 1 - p̂
        std_err = math.sqrt( p̂ * q_hat / n )
    else:
        # calculate std_err when std_dev is known
        std_dev = float(input("enter std deviation: "))
        p = std_dev
        q = 1 - p
        std_err = math.sqrt( p * q / n )

    print(f"standard err: {round(std_err, 3)}")



if __name__ == "__main__":
    main()
