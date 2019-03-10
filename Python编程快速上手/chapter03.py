# QAQ1
# collatz序列
a: int = 0


def collatz(number):
    """

    :type number: object
    """

    if (number % 2) == 0:
        print("number//2:" + str(number // 2))
        return number // 2
    else:
        print("3*number+1:" + str(3 * number + 1))
        return 3 * number + 1


try:
    n = int(input())
    while a != 1:
        a = collatz(n)
        n = a
except ValueError:
    print('You must input a int')
