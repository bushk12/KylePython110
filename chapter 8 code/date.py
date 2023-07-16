def main():
    # heading and information
    print('Please enter the date in mm/dd/yyyy format!\n')
    # asking the user for the input
    userdate = input('Enter Date: ')
    # creating a list of months to shorten up the code.
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

    # formatting the date, getting rid of all the "/" in the entire string
    lst = userdate.split("/")
    # combining the months list I created with the userdate inputted string.
    month_name = months[int(lst[0]) - 1]
    # giving the day an int value to get rid of the "0" if it is 08
    day = int(lst[1])
    # assigning the year to the last value
    year = int(lst[2])

    print()
    # combining it all to print out a result!
    print(f'Your date reformatted is: \n' + str(month_name) + " " + str(day) + ', ' + str(year))


if __name__ == '__main__':
    main()
