


def main():
    print("Rainfall Calculator")
    print('')

    total = 0

    # defining rainfall for month
    rainfall = [0]

    # defining the months

    jan = float(input(f'Rainfall for January: '))
    feb = float(input(f'Rainfall for February: '))
    mar = float(input(f'Rainfall for March: '))
    apr = float(input(f'Rainfall for April: '))
    may = float(input(f'Rainfall for May: '))
    jun = float(input(f'Rainfall for June: '))
    jul = float(input(f'Rainfall for July: '))
    aug = float(input(f'Rainfall for August: '))
    sep = float(input(f'Rainfall for September: '))
    octo = float(input(f'Rainfall for October: '))
    nov = float(input(f'Rainfall for November: '))
    dec = float(input(f'Rainfall for December: '))

    # appending the months to the list

    rainfall.append(jan)
    rainfall.append(feb)
    rainfall.append(mar)
    rainfall.append(apr)
    rainfall.append(may)
    rainfall.append(jun)
    rainfall.append(jul)
    rainfall.append(aug)
    rainfall.append(sep)
    rainfall.append(octo)
    rainfall.append(nov)
    rainfall.append(dec)

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
    # finding the month with the most rainfall

    if jan == max(rainfall):
        print("January had the most rain with: ")
    elif feb == max(rainfall):
        print("February had the most rain with: ")
    elif mar == max(rainfall):
        print("March had the most rain with: ")
    elif apr == max(rainfall):
        print("April had the most rain with: ")
    elif may == max(rainfall):
        print("May had the most rain with: ")
    elif jun == max(rainfall):
        print("June had the most rain with: ")
    elif jul == max(rainfall):
        print("July had the most rain with: ")
    elif aug == max(rainfall):
        print("August had the most rain with: ")
    elif sep == max(rainfall):
        print("September had the most rain with: ")
    elif octo == max(rainfall):
        print("October had the most rain with: ")
    elif nov == max(rainfall):
        print("November had the most rain with: ")
    elif dec == max(rainfall):
        print("December had the most rain with: ")
    else:
        print("Cant Compute")

    print(max(rainfall))

    print('')

    print(min(rainfall))


main()


