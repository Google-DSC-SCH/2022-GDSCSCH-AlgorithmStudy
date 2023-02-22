def day_add(day, add_month):
    y, m, d = map(int, day.split("."))
    ty, tm, td = 0, 0, 0
    if add_month >= 12:
        dy, dm = divmod(add_month, 12)
        ty += dy
        tm += dm
    else:
        tm += add_month
    d = d - 1
    y += ty
    m += tm
    if d == 0:
        m = m - 1
        d = 28

    if m > 12:
        y += 1
        m = m % 12

    return "{0}.{1}.{2}".format(y, str(m).zfill(2), str(d).zfill(2))


def solution(today, terms, privacies):
    answer = []
    term = {}
    for t in terms:
        a, b = t.split(" ")
        term[a] = b

    for p in range(len(privacies)):
        a, b = privacies[p].split(" ")
        if today > day_add(a, int(term[b])):
            answer.append(p+1)

    return answer
