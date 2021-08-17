"""
Programa: 
Enunciado:
    11. Write and test a function to meet this specification.
    squareEach(nums) nums is a list of numbers. Modifies the list by squaring
    each entry.

    12. Write and test a function to meet this specification.
    sumList(nums) nums is a list of numbers. Returns the sum of the numbers
    in the list.

    13. Write and test a function to meet this specification.
    toNumbers(strList) strList is a list of strings, each ofwhich represents
    a number. Modifies each entry in the list by converting it to a number.

    14. Use the functions from the previous three problems to implement a program that computes the sum of the squares of numbers read from a file.
    Your program should prompt for a file name and print out the sum of the
    squares of the values in the file. Hint: Use readlines()
"""

def squareEach(nums):
    squared = []
    for num in nums:
        squared.append(num**2)
    return (squared)

def sumList(nums):
    return sum(nums)

def toNumbers(strList):
    return [float(item) for item in strList]

def main():
    fileName = input("Digite o caminho do arquivo: ")
    file = open(fileName)
    strList = file.readlines()
    nums = toNumbers(strList)
    squared = squareEach(nums)
    soma = sumList(squared)
    print(f"A soma dos quadrados da lista é {soma}.")


main()