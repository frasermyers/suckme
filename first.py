
def calc_fact(n):
    global i
    fact = 1
    for i in range(0, n):
        fact *= i + 1

    return fact


i = 5

while i > 0:
    print("calculating: " + str(i) + " fact = ", calc_fact(i))

    i -= 1

SOME_MORE_CHANGES = "Cool"
