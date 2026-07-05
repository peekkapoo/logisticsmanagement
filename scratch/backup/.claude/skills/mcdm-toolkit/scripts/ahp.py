# -*- coding: utf-8 -*-
"""AHP weight calculator with consistency check.

Usage:
    python ahp.py matrix1.csv [matrix2.csv ...] [--latex out.tex]

Each CSV: square pairwise-comparison matrix, numbers only, comma-separated.
Reciprocal entries may be written as decimals (0.2) or fractions (1/5).
Multiple matrices are aggregated element-wise by geometric mean, then the
final weights are computed on the aggregated matrix.

Outputs per matrix: weights (geometric-mean method AND eigenvector via power
iteration), lambda_max, CI, CR. Flags CR > 0.1 and prints the 3 entries that
contribute most to inconsistency.
"""
import csv
import math
import sys

RI = {1: 0.0, 2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32,
      8: 1.41, 9: 1.45, 10: 1.49, 11: 1.51, 12: 1.48, 13: 1.56, 14: 1.57, 15: 1.59}


def parse_value(s):
    s = s.strip()
    if "/" in s:
        a, b = s.split("/")
        return float(a) / float(b)
    return float(s)


def read_matrix(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = [[parse_value(x) for x in row if x.strip() != ""]
                for row in csv.reader(f) if any(x.strip() for x in row)]
    n = len(rows)
    for r in rows:
        if len(r) != n:
            raise SystemExit(f"{path}: matrix is not square ({n} rows, row has {len(r)} cols)")
    return rows


def geo_mean_weights(m):
    n = len(m)
    gm = [math.prod(m[i]) ** (1.0 / n) for i in range(n)]
    s = sum(gm)
    return [g / s for g in gm]


def eigen_weights(m, iters=200, tol=1e-12):
    n = len(m)
    w = [1.0 / n] * n
    for _ in range(iters):
        nw = [sum(m[i][j] * w[j] for j in range(n)) for i in range(n)]
        s = sum(nw)
        nw = [x / s for x in nw]
        if max(abs(nw[i] - w[i]) for i in range(n)) < tol:
            w = nw
            break
        w = nw
    return w


def consistency(m, w):
    n = len(m)
    aw = [sum(m[i][j] * w[j] for j in range(n)) for i in range(n)]
    lam = sum(aw[i] / w[i] for i in range(n)) / n
    ci = (lam - n) / (n - 1) if n > 1 else 0.0
    cr = ci / RI[n] if RI.get(n, 0) > 0 else 0.0
    return lam, ci, cr


def worst_entries(m, w, top=3):
    """Entries whose value deviates most from the consistent ratio w_i/w_j."""
    n = len(m)
    devs = []
    for i in range(n):
        for j in range(i + 1, n):
            ideal = w[i] / w[j]
            dev = abs(math.log(m[i][j] / ideal))
            devs.append((dev, i, j, m[i][j], ideal))
    devs.sort(reverse=True)
    return devs[:top]


def aggregate(mats):
    n = len(mats[0])
    k = len(mats)
    return [[math.prod(mm[i][j] for mm in mats) ** (1.0 / k) for j in range(n)]
            for i in range(n)]


def latex_table(w, path):
    lines = ["\\begin{table}[htbp]", "\\centering",
             "\\caption{Criteria weights obtained by AHP}", "\\label{tab:ahp-weights}",
             "\\begin{tabular}{lc}", "\\toprule",
             "Criterion & Weight \\\\", "\\midrule"]
    for i, wi in enumerate(w, 1):
        lines.append(f"C{i} & {wi:.4f} \\\\")
    lines += ["\\bottomrule", "\\end{tabular}", "\\end{table}", ""]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"LaTeX table written: {path}")


def report(name, m):
    w = geo_mean_weights(m)
    we = eigen_weights(m)
    lam, ci, cr = consistency(m, we)
    print(f"\n=== {name} (n={len(m)}) ===")
    print("weights (geometric mean):", [round(x, 4) for x in w])
    print("weights (eigenvector)   :", [round(x, 4) for x in we])
    print(f"lambda_max={lam:.4f}  CI={ci:.4f}  CR={cr:.4f}", end="  ")
    if cr > 0.1:
        print("-> KHONG HOP LE (CR > 0.1)")
        print("3 cap gay bat nhat lon nhat (i,j | gia tri dien | gia tri nhat quan):")
        for dev, i, j, val, ideal in worst_entries(m, we):
            print(f"  C{i+1} vs C{j+1}: dien {val:.3f} | nen ~{ideal:.3f}")
    else:
        print("-> DAT")
    return we, cr


def main():
    args = sys.argv[1:]
    latex_out = None
    if "--latex" in args:
        k = args.index("--latex")
        latex_out = args[k + 1]
        args = args[:k] + args[k + 2:]
    if not args:
        raise SystemExit(__doc__)
    mats = [read_matrix(p) for p in args]
    valid = []
    for path, m in zip(args, mats):
        w, cr = report(path, m)
        if cr <= 0.1:
            valid.append(m)
    if len(mats) > 1:
        if not valid:
            raise SystemExit("\nKhong co ma tran nao dat CR <= 0.1 — dung lai, gui lai cho nguoi dien.")
        agg = aggregate(valid)
        print(f"\n### TONG HOP {len(valid)}/{len(mats)} ma tran hop le (geometric mean) ###")
        w, cr = report("TONG HOP", agg)
    else:
        w = eigen_weights(mats[0])
    if latex_out:
        latex_table(w, latex_out)


if __name__ == "__main__":
    main()
