# -*- coding: utf-8 -*-
"""Likert survey descriptive analysis and criteria screening.

Usage:
    python likert.py survey.csv [--threshold 3.5] [--cols "C1,C2"] [--latex out.tex]

Auto-detects criteria columns (all numeric values in 1..5) unless --cols given.
Drops respondents missing more than 20% of criteria answers. Reports
straight-liners (same answer everywhere) without dropping them.
"""
import csv
import math
import sys


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    header = rows[0]
    data = [r + [""] * (len(header) - len(r)) for r in rows[1:] if any(x.strip() for x in r)]
    return header, data


def is_likert(vals):
    seen = False
    for v in vals:
        v = v.strip()
        if v == "":
            continue
        try:
            x = float(v)
        except ValueError:
            return False
        if x not in (1, 2, 3, 4, 5):
            return False
        seen = True
    return seen


def mean_sd(xs):
    n = len(xs)
    if n == 0:
        return 0.0, 0.0
    m = sum(xs) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1)) if n > 1 else 0.0
    return m, sd


def main():
    args = sys.argv[1:]
    threshold, cols_arg, latex_out = 3.5, None, None
    for flag in ("--threshold", "--cols", "--latex"):
        if flag in args:
            k = args.index(flag)
            val = args[k + 1]
            args = args[:k] + args[k + 2:]
            if flag == "--threshold":
                threshold = float(val)
            elif flag == "--cols":
                cols_arg = [c.strip() for c in val.split(",")]
            else:
                latex_out = val
    if len(args) != 1:
        raise SystemExit(__doc__)
    header, data = read_csv(args[0])

    if cols_arg:
        idx = [header.index(c) for c in cols_arg]
    else:
        idx = [j for j in range(len(header)) if is_likert([r[j] for r in data])]
    names = [header[j] for j in idx]
    if not idx:
        raise SystemExit("Khong tim thay cot Likert nao (gia tri 1-5). Dung --cols de chi dinh.")

    # clean respondents
    kept, dropped, straight = [], 0, 0
    for r in data:
        vals = [r[j].strip() for j in idx]
        missing = sum(1 for v in vals if v == "")
        if missing > 0.2 * len(idx):
            dropped += 1
            continue
        nums = [float(v) for v in vals if v != ""]
        if len(set(nums)) == 1 and len(nums) == len(idx):
            straight += 1
        kept.append(r)

    print(f"Phan hoi: {len(data)} thu ve | {len(kept)} hop le | {dropped} loai (thieu >20%) | {straight} straight-lining (bao de nhom quyet)")
    print(f"Nguong giu: mean >= {threshold} (nguong phai co trich dan trong bao cao)\n")
    print(f"{'Cot':<20}{'N':>5}{'Mean':>8}{'SD':>7}  {'1':>4}{'2':>4}{'3':>4}{'4':>4}{'5':>4}  KetLuan")

    results = []
    for j, name in zip(idx, names):
        xs = [float(r[j]) for r in kept if r[j].strip() != ""]
        m, sd = mean_sd(xs)
        freq = [sum(1 for x in xs if x == v) for v in (1, 2, 3, 4, 5)]
        verdict = "GIU" if m >= threshold else "LOAI"
        results.append((name, len(xs), m, sd, freq, verdict))
        print(f"{name:<20}{len(xs):>5}{m:>8.2f}{sd:>7.2f}  " +
              "".join(f"{f:>4}" for f in freq) + f"  {verdict}")

    if latex_out:
        lines = ["\\begin{table}[htbp]", "\\centering",
                 "\\caption{Survey results and criteria screening " +
                 f"(threshold $\\bar{{x}} \\geq {threshold}$)}}",
                 "\\label{tab:survey-results}",
                 "\\begin{tabular}{lcccc}", "\\toprule",
                 "Criterion & $N$ & Mean & SD & Decision \\\\", "\\midrule"]
        for name, n, m, sd, _, verdict in results:
            safe = name.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_")
            dec = "Retain" if verdict == "GIU" else "Remove"
            lines.append(f"{safe} & {n} & {m:.2f} & {sd:.2f} & {dec} \\\\")
        lines += ["\\bottomrule", "\\end{tabular}", "\\end{table}", ""]
        with open(latex_out, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"\nLaTeX table written: {latex_out}")


if __name__ == "__main__":
    main()
