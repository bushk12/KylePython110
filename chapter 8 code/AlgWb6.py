def main():

    # defining the string to count the t's
    count = 0

    # asking the user to type a phrase
    string1 = input('Type a phrase: ')

    # creating the for loop to find the T's
    for ch in string1:
        if ch == 'T' or ch == 't':
            count += 1

    # printing the result
    print(string1)
    print(f'The letter T appears {count} times in the phrase you typed.')

if __name__ == '__main__':
    main()