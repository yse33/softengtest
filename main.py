def even_numbers(n):
    return [x for x in range(n) if x % 2 == 0]


def print_menu():
    print("2. Even numbers")


def main():
    print_menu()
    function = int(input("Your choice: "))
    maxNum = int(input("Enter max number: "))
    if function == 2:
        print(str(even_numbers(maxNum))[1:-1])
    else:
        print("Invalid choice")


if __name__ == '__main__':
    main()

