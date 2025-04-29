from ga_core import run_ga

if __name__ == "__main__":
    best_chrom, (x1, x2), fit = run_ga()
    print("Kromosom Terbaik:", best_chrom)
    print("x1 =", x1, ", x2 =", x2)
    print("Fitness =", fit)
