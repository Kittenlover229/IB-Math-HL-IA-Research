A = [
    (-35,-15),
    (-13.5,-2.5),
    (-7.1,-2.5),
    (10,-10)
]

n = len(A)

def to_str(x: int) -> str:
    if x < 0:
        return f"({x})"
    else:
        return str(x)

def make_lagrange_thing() -> str:
    summated = []
    for i in range(n):
        y_i = A[i][1]
        numer = []
        denom = []
        for j in range(n):
            if i == j:
                continue
            numer.append(f"(x - {to_str(A[j][0])})")
            denom.append(f"({to_str(A[i][0])} - {to_str(A[j][0])})")
        summated.append(str(y_i) + "* (" + "*".join(numer) + "/(" + "*".join(denom) + "))")
    return " + ".join(summated)

def calc_at(x: int):
    thing = make_lagrange_thing()
    return eval(thing)

print(make_lagrange_thing())

for i in range(-50, 51):
    print(i, calc_at(i))
