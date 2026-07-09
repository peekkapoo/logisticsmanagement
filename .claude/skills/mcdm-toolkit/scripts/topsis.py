# -*- coding: utf-8 -*-
"""TOPSIS ranking with optional weight sensitivity analysis.

Usage:
    python topsis.py decision-matrix.csv [--latex out.tex] [--sensitivity]

CSV format:
    Alternative,C1,C2,...          header
    type,benefit,cost,...          optimisation direction per criterion
    weight,0.25,0.10,...           AHP weights (will be re-normalised to sum 1)
    Laptop A,15990000,8123,...     one row per alternative

Steps (Hwang & Yoon 1981): vector normalisation -> weighting -> ideal
solutions A+/A- -> Euclidean distances -> closeness coefficient Ci -> rank.
"""
import csv
import math
import sys


def read_input(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = [r for r in csv.reader(f) if any(x.strip() for x in r)]
    header = rows[0]
    criteria = header[1:]
    types_row = next(r for r in rows if r[0].strip().lower() == "type")
    weight_row = next(r for r in rows if r[0].strip().lower() == "weight")
    types = [t.strip().lower() for t in types_row[1:]]
    weights = [float(x) for x in weight_row[1:]]
    s = sum(weights)
    weights = [w / s for w in weights]
    alts, data = [], []
    for r in rows[1:]:
        if r[0].strip().lower() in ("type", "weight"):
            continue
        alts.append(r[0].strip())
        data.append([float(x) for x in r[1:]])
    for t in types:
        if t not in ("benefit", "cost"):
            raise SystemExit(f"type must be 'benefit' or 'cost', got '{t}'")
    return criteria, types, weights, alts, data


def topsis(types, weights, data):
    m, n = len(data), len(data[0])
    norms = [math.sqrt(sum(data[i][j] ** 2 for i in range(m))) for j in range(n)]
    v = [[(data[i][j] / norms[j]) * weights[j] if norms[j] else 0.0
          for j in range(n)] for i in range(m)]
    a_pos = [max(v[i][j] for i in range(m)) if types[j] == "benefit"
             else min(v[i][j] for i in range(m)) for j in range(n)]
    a_neg = [min(v[i][j] for i in range(m)) if types[j] == "benefit"
             else max(v[i][j] for i in range(m)) for j in range(n)]
    ci = []
    for i in range(m):
        dp = math.sqrt(sum((v[i][j] - a_pos[j]) ** 2 for j in range(n)))
        dn = math.sqrt(sum((v[i][j] - a_neg[j]) ** 2 for j in range(n)))
        ci.append(dn / (dp + dn) if (dp + dn) else 0.0)
    return ci


def ranking(alts, ci):
    return sorted(zip(alts, ci), key=lambda x: x[1], reverse=True)


def latex_table(rank, path):
    lines = ["\\begin{table}[htbp]", "\\centering",
             "\\caption{TOPSIS ranking of alternatives}", "\\label{tab:topsis-ranking}",
             "\\begin{tabular}{clc}", "\\toprule",
             "Rank & Alternative & $C_i$ \\\\", "\\midrule"]
    for k, (name, c) in enumerate(rank, 1):
        safe = name.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_")
        lines.append(f"{k} & {safe} & {c:.4f} \\\\")
    lines += ["\\bottomrule", "\\end{tabular}", "\\end{table}", ""]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"LaTeX table written: {path}")


def sensitivity(criteria, types, weights, alts, data, base_top):
    print("\n### SENSITIVITY ANALYSIS (moi tieu chi +/-10%, +/-20%) ###")
    changes = 0
    for j, cname in enumerate(criteria):
        for delta in (-0.2, -0.1, 0.1, 0.2):
            w = weights[:]
            w[j] = max(w[j] * (1 + delta), 1e-9)
            s = sum(w)
            w = [x / s for x in w]
            top = ranking(alts, topsis(types, w, data))[:3]
            top_names = [t[0] for t in top]
            if top_names != base_top:
                changes += 1
                print(f"  {cname} {delta:+.0%}: top3 -> {top_names}")
    if changes == 0:
        print("  Thu hang top 3 KHONG doi trong moi kich ban -> ket qua ben vung.")
    else:
        print(f"  {changes} kich ban lam doi top 3 -> ban luan trong muc 4.5 cua bao cao.")


def main():
    args = sys.argv[1:]
    latex_out, do_sens = None, False
    if "--latex" in args:
        k = args.index("--latex")
        latex_out = args[k + 1]
        args = args[:k] + args[k + 2:]
    if "--sensitivity" in args:
        do_sens = True
        args.remove("--sensitivity")
    if len(args) != 1:
        raise SystemExit(__doc__)
    criteria, types, weights, alts, data = read_input(args[0])
    print(f"Alternatives: {len(alts)} | Criteria: {len(criteria)}")
    print("Weights (normalised):", [round(w, 4) for w in weights])
    rank = ranking(alts, topsis(types, weights, data))
    print("\n### RANKING ###")
    for k, (name, c) in enumerate(rank, 1):
        print(f"{k:>3}. {name:<40} Ci={c:.4f}")
    if latex_out:
        latex_table(rank, latex_out)
    if do_sens:
        sensitivity(criteria, types, weights, alts, data, [r[0] for r in rank[:3]])


if __name__ == "__main__":
    main()
