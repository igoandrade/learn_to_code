"""
The National Weather Service computes the windchill index using the following formula:

    35.74 + 0.6215*T - 35.75*(V**0.16) +0.4275*T(V**0.16)

Where T is the temperature in degrees Fahrenheit, and V is the wind speed
in miles per hour.

Write a program that prints a nicely formatted table of windchill values. Rows should represent wind speed for 0 to 50 in 5-mph increments,
and the columns represent temperatures from -20 to +60 in 10-degree increments. Note: The formula only applies for wind speeds in excess of 3 miles per hour.
"""

def windchill_index(T, V):
    """
    The National Weather Service computes the windchill index using the following formula:

        35.74 + 0.6215*T - 35.75*(V**0·16) +0.4275*T(V**0·16)

    Where T is the temperature in degrees Fahrenheit, and V is the wind speed
    in miles per hour.

    Note: The formula only applies for wind speeds in excess of 3 miles per hour.
    """
    if V < 3:
        return None
    else:
        windchill = 35.74 + 0.6215*T - 35.75*(V**0.16) +0.4275*T*(V**0.16)
        return windchill

def main():
    V = list(range(5, 55, 5))
    T = list(range(-20, 70, 10))
    cab1 = " Temperature "
    cab2 = "Wind Speed (mph)".center(71)
    n1 = len(cab1)
    n2 = len(cab2)

    cab = cab1 + '|' + cab2
    n = len(cab)

    print(n * "=")
    print(cab)
    print("(°F)".center(n1) + '|' + n2 * "-")
    linha0 = " "*n1 + '|'
    for v in V:
        linha0 += f"{v:>7d}"
    print(linha0)
    print(n * "-")
    for t in T:
        linha = f"{t:>3d}".center(n1) + '|'
        for v in V:
            w = windchill_index(t, v)
            linha += f"{w:>7.1f}"
        print(linha)
            
            

    print(n * "=")

if __name__=="__main__":
    main()