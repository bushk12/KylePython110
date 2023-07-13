def main():
    # asking the user to input their full namne
    name = input("Please enter your full name: ")

    # creating a list from the string
    initials = name.split()

    # taking the initials list list this => [element][first letter from element] and printing
    print(initials[0][0] + '.' + initials[1][0] + '.' + initials[2][0])


# calling main function to run the program
if __name__ == '__main__':
    main()
