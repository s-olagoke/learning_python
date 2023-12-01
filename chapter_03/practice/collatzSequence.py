
# A program always return 1 as the final answer - popularly know as COLLATZ SEQUENCE

def collatz(num):
        if num == 1:
                print(num)
                return num
        elif num % 2 == 0:
                print(num)
                return collatz(num // 2)
        elif num % 2 == 1:
                print(num)
                return collatz(3 * num + 1)


print('Enter a number:')

num = int(input())

collatz(num)
