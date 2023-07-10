def main():

    print("Rainfall Calculator")
    print('')

    total = 0

    # defining rainfall for month
    rainfall = []

    # defining the months

    jan = float(input(f'January: '))
    feb = float(input(f'February: '))
    mar = float(input(f'March: '))
    apr = float(input(f'April: '))
    may = float(input(f'May: '))
    jun = float(input(f'June: '))
    jul = float(input(f'July: '))
    aug = float(input(f'August: '))
    sep = float(input(f'September: '))
    octo = float(input(f'October: '))
    nov = float(input(f'November: '))
    dec = float(input(f'December: '))

    # appending the months to the list
    rainfall.extend([jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec])
    print('')

    # declaring the months
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # taking the total
    for value in rainfall:
        total += value

    print('')

    # printing out the sum of the list
    print(f'The TOTAL amount of rainfall for the year is: {total} inches')

    # creating average
    average = total / 12

    print('')
    # printing out the average
    print(f'The AVERAGE amount of rainfall each month for the year is: {average} inches/month')

    print('')

    # creating a dictionary to display top results
    from collections import Counter

    # zip the lists together, so they're paired properly before finding the top three
    my_dict = dict(zip(months, rainfall))
    k = Counter(my_dict)

    # this will take the three highest numbers in the dictionary
    high = k.most_common(3)
    print("Rainfall Per Month: ")

    # showing the dictionary ordered
    print(my_dict, "\n")

    print("Top Three Months For Rainfall: ")
    print("Month: Amount")

    # for loop to print out the correct numbers from high on line 59
    for i in high:
        print(i[0], " :", i[1], " ")

    print('')
    print("Lowest Three Months For Rainfall: ")
    print("Month: Amount")

    # Here I am reverse sorting the dictionary I created above. Issues with formatting the output but it works!
    sorted_dict = sorted(my_dict.items(), key=lambda kv: kv[1])

    # taking the reverse sorted dictionary and doing the same thing as earlier
    h = Counter(sorted_dict)
    low = h.most_common(3)

    # same for loop as line 69
    for k in low:
        print(k[0])

    print(' ')
if __name__ == '__main__':
    main()
