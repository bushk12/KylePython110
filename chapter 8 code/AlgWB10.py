def main():
    print("Algorithm Workbench 10\n")
    # creation of mystring
    mystring = 'cookies>milk>fudge>cake>ice cream'

    # creating a list out of the string while removing the >
    lst = mystring.split(">")

    # printing lst
    print(lst)


# calling the main function
if __name__ == '__main__':
    main()
