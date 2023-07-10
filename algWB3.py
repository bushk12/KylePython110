def main():

    # numbers1 is the main list that will be copied to numbers2
    numbers1 = [1, 2, 3]

    # numbers 2 will get a copy of numbers1
    numbers2 = []

    # appending the elements from numbers1 into numbers2
    for item in numbers1:
        numbers2.append(item)

    # printing out lists to show the code copying
    print(numbers1)
    print(numbers2)


main()

