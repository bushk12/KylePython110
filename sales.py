

# main function to store total sales and print them out
def main():
    # make a list of all the sales inputted by the user
    daily_sale = []
    total = 0
    # variables for creating the list
    mon = float(input(f'Enter Sales for Monday: '))
    tue = float(input(f'Enter Sales for Tuesday: '))
    wed = float(input(f'Enter Sales for Wednesday: '))
    thu = float(input(f'Enter Sales for Thursday: '))
    fri = float(input(f'Enter Sales for Friday: '))
    sat = float(input(f'Enter Sales for Saturday: '))
    sun = float(input(f'Enter Sales for Sunday: '))

    # append the item to the list
    daily_sale.extend([mon, tue, wed, thu, fri, sat, sun])


    # adding the values together
    for x in daily_sale:
        total = sum(daily_sale)

    print(f'The total sales for the week is ${total}.')
if __name__ == '__main__':
    main()

