def main():
    # heading and information
    print('Please enter the date in mm/dd/yyyy format!\n')
    # asking the user for the input
    userdate = input('Enter Date: ')

    # formatting the date, getting rid of all the "/" in the entire
    lst = userdate.split("/")

    # getting rid of the 0s and "/" in lst2 (the day)
    lst2 = userdate.split("0" and "/")[1]
    print("")

    # creating if statement to print out the correct format.
    if lst[0] == '01':                                      # taking element 0 from lst. which would be the month
        print('January' + " " + lst2[1] + ', ' + lst[2])    # taking lst2[1] element which would be the day & the year from lst, which is the last element
    if lst[0] == '02':
        print('February' + " " + lst2[1] + ', ' + lst[2])
    if lst[0] == '03':
        print('March' + " " + lst2[1] + ', ' + lst[2])
    if lst[0] == '04':
        print('April' + " " + lst2[1] + ', ' + lst[2])
    if lst[0] == '05':
        print('May' + " " + lst2[1] + ', ' + lst[2])
    if lst[0] == '06':
        print('June' + " " + lst2[1] + ', ' + lst[2])
    if lst[0] == '07':
        print('July' + " " + lst2[1] + ', ' + lst[2])
    if lst[0] == '08':
        print('August' + " " + lst2[1] + ', ' + lst[2])
    if lst[0] == '09':
        print('September' + " " + lst2[1] + ', ' + lst[2])
    if lst[0] == '10':
        print('October' + " " + lst2[1] + ', ' + lst[2])
    if lst[0] == '11':
        print('November' + " " + lst2[1] + ', ' + lst[2])
    if lst[0] == '12':
        print('December' + " " + lst2[1] + ', ' + lst[2])


if __name__ == '__main__':
    main()
