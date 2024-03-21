<<<<<<< HEAD
def even_numbers(n):
    return [x for x in range(n) if x % 2 == 0]


def print_menu():
    print("2. Even numbers")
=======
def odd_numbers(n):
    return [x for x in range(n) if x % 2 == 1]


def print_menu():
    print("1. Odd numbers")
>>>>>>> 0d38311998c231b4d53889071f30cb78871c2d88


def main():
    print_menu()
    function = int(input("Your choice: "))
    maxNum = int(input("Enter max number: "))
<<<<<<< HEAD
    if function == 2:
        print(str(even_numbers(maxNum))[1:-1])
=======
    if function == 1:
        print(str(odd_numbers(maxNum))[1:-1])
>>>>>>> 0d38311998c231b4d53889071f30cb78871c2d88
    else:
        print("Invalid choice")


if __name__ == '__main__':
    main()

