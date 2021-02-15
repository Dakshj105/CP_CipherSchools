def TwoPeopleMeetEachOther(x1, x2 , v1, v2):
    if (x1 > x2 and v1 >= v2) or (x2 > x1 and v2 >= v1) or (x1 == x2 and v1 != v2):
        print("No")

    else:
        if v1 > v2:
            v = v1 - v2

        else:
            v = v2 - v1

        if v:
            print(abs(x2 - x1) % v == 0)
        else:
            print(True)



x1 = int(input("Enter Position of 1st person:- "))
x2 = int(input("Enter Position of 2st person:- "))
v1 = int(input("Enter speed of 1st person:- "))
v2 = int(input("Enter spped of 2nd person:- "))

TwoPeopleMeetEachOther(x1, x2, v1, v2)
