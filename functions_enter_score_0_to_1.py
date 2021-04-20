score = input("Enter Score beetween 0.0 and 1.0: ")
s = float(score)
def computegrade():
    if s >= 1.0:
        print("Bad score")
    elif s >= 0.9:
        print("A")
    elif s >= 0.8:
        print("B")
    elif s >= 0.7:
        print("C")
    elif s >= 0.6:
        print("D")
    elif s > 0:
        print("F")
    else:
        print("Bad score")
computegrade()
