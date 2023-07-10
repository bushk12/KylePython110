# main function
# I will be turning a list into a string, and a string into a list!
def main():
    # turning a list into a string
    names = ['Einstein', 'Newton', 'Copernicus', 'Kepler']

    # here I am creating a string with the list.
    string1 = 'Here are some of the greatest minds ever: {}, {}, {}, and {}.'.format(*names)

    print(string1)

    # creating a string
    string2 = 'Einstein, Newton, Copernicus, Kepler'

    # using the convert function to print out the string
    print(convert(string2))


# creating a function to convert a string of my choice into a function
def convert(string):

    # splitting the string into a list
    li = list(string.split(" "))
    return li

if __name__ == '__main__':

    main()