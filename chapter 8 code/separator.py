def main():
    print("Programming Exercise 11\n")
    # user input
    print("Enter a sentence below with no spaces, but every word starts with a capital letter.")
    # asking the user for a sentence
    user = input("")
    # assigning fixed to the "" variable for the "for loop"
    fixed = ""
    # assigning a, a value for the loop
    a = 0

    # for loop to add spaces and change the rest of the sentence to lower case
    for ch in user:
        if ch.isupper() and a > 0:
            # adding spaces before the uppercase letters
            fixed += " "
            # changing the rest of the uppercase letters to lowercase (except the first word)
            fixed += ch.lower()
        else:
            fixed += ch
        a += 1

    # printing the fixed sentence
    print("This is the fixed sentence: \n")
    print(fixed)


if __name__ == '__main__':
    main()
