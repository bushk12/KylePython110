def main():
    # printing program title
    print("Algorithm Workbench 6\n")

    # asking the user to type a phrase using lowercase t's
    string = input("Create a string using lowercase t's: ")

    # replacing the lowercase "t" with uppercase "t"
    replaced = string.replace("t", "T")

    # printing the result
    print(replaced)


# calling main function
if __name__ == '__main__':
    main()
