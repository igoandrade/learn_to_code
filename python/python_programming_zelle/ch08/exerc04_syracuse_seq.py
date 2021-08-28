"""
The Syracuse (also called "Collatz" or "Hailstone") sequence is generated
by starting with a natural number and repeatedly applying the following
function until reaching 1 :

                x/2     if x is even
    syr(x) =
                3x+1    if x in odd

For example, the Syracuse sequence starting with 5 is: 5, 16, 8, 4, 2, 1. It is
an open question in mathematics whether this sequence will always go to
1 for every possible starting value.

Write a program that gets a starting value from the user and then prints
the Syracuse sequence for that starting value.
"""

def syr(x):
    """
    The Syracuse (also called "Collatz" or "Hailstone") sequence is generated
    by starting with a natural number and repeatedly applying the following
    function until reaching 1 :

                    x/2     if x is even
        syr(x) =
                    3x+1    if x in odd

    For example, the Syracuse sequence starting with 5 is: 5, 16, 8, 4, 2, 1. It is
    an open question in mathematics whether this sequence will always go to
    1 for every possible starting value.
    """
    if x % 2 == 0:
        return int(x/2)
    else:
        return int(3 * x + 1)

def main():
    x = int(input("\nInforme o valor inicial da sequência: "))
    n = 1
    print(61 * "=")
    print(f"{x:>6d}", end="")
    while x != 1:
        x = syr(x)
        n += 1
        if (n % 10 != 0):
            print(f"{x:>6d}", end="")
        else:
            print(f"{x:>6d}")
    print("\n" + 61 * "=")
            




if __name__=="__main__":
    main()