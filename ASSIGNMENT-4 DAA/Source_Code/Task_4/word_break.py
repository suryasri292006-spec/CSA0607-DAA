"""Task 4 - WordBreak: faulty vs corrected. substring(Text, j, i) = characters j..i-1 (0-indexed)."""

def word_break(text, dictionary, fixed, trace=True):
    n = len(text)
    DP = [False] * (n + 1)
    DP[0] = True
    for i in range(1, n + 1):
        DP[i] = False
        for j in range(0, i):
            cond = text[j:i] in dictionary
            if fixed:
                cond = cond and DP[j]                  # THE REPAIR: prefix text[0:j] must be segmentable
            if cond:
                DP[i] = True
                break
        if trace:
            print(f"   i={i} prefix='{text[:i]}' DP[{i}]={DP[i]}")
    return DP[n]


if __name__ == "__main__":
    cases = [("FAILING CASE", "abc", {"bc"}), ("REGRESSION CASE", "applepen", {"apple", "pen"})]
    for name, t, d in cases:
        print(f"\n=== {name}: Text='{t}', Dictionary={sorted(d)} ===")
        print(" Original algorithm:")
        r1 = word_break(t, d, fixed=False)
        print(" -> returns", r1)
        print(" Corrected algorithm:")
        r2 = word_break(t, d, fixed=True)
        print(" -> returns", r2)
