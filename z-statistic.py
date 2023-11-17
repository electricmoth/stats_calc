#!/usr/bin/python3

# Calculate z-statistic of a population mean.

# example:
# Spencer sampled 50 students of a private school who were questioned about their scores in Mathematics. Spencer wants to test the hypothesis that the private school students score better than the general public which has an average of 62 marks with a population standard deviation of 7 marks.
# z equals fraction numerator x with bar on top minus mu over denominator begin display style fraction numerator sigma over denominator square root of n end fraction end style end fraction
# If the sample mean is 65 marks, what is the z-score?

import math


formula = """
formula:

z = x̅ - μ
   -------
      σ
      --
      √n

"""

def main ():
    print("~~~ z-test for population means calculator ~~~\n\n")
    print(formula)
    population_mean = float(input("Population mean (μ): "))
    population_std_dev = float(input("Population standard deviation (σ): "))
    sample_mean = float(input("Sample mean (x̅): "))
    sample_size = float(input("Sample size (n): "))
    z_score = (sample_mean - population_mean)/(population_std_dev/math.sqrt(sample_size))

    print(f"\nzscore: {z_score}\n")
    x̅ = 34
    μ = 3
    print(f"\n{x̅ - μ}\n")


if __name__ == "__main__":
    main()
