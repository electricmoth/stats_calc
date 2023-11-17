#!/usr/bin/python3

# Determine the z-critical value

import scipy.stats


def right(lvl):
     z = scipy.stats.norm.ppf(1-lvl)
     print(f"z: {z}")


def left(lvl):
     z = scipy.stats.norm.ppf(lvl)
     print(f"z: {z}")


def two_tail(lvl):
    z = scipy.stats.norm.ppf(1-lvl/2)
    print(f"z: {z}")


def main():
    print("- (r)ight tail\n- (l)eft tail\n- (t)wo-tail\n")
    mode = input("mode (r/l/t): ")
    print(f"mode: {mode}")
    lvl = float(input("significance level: "))

    match mode:
        case "r":
            right(lvl)
        case "l":
            left(lvl)
        case "t":
            two_tail(lvl)

        case _:
            print("invalid choice")
            main()



if __name__ == "__main__":
    main()
