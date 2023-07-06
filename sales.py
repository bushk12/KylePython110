

# main function to store total sales and print them out
def main():
    # make a list of all the sales inputted by the user
    daily_sale = []
    inputday = []
    # creates a variable to control the loop
    again = 'y' or 'Y'

    # creating sales numbers
    while again == 'y':
        day = input('Enter a Day:')
        sale = input('Enter Sales Amount:')

        # append the item to the list
        daily_sale.append(sale)
        inputday.append(day)

        # adding another day

        print('Do you want to add another day?')
        again = input('y = yes, anything else = no:')
        # Total sale of all the sales numbers

    # combine both lists into one list with appropriate inputs
    print('Here are your sales for each day: ')
    zipped = zip(inputday, daily_sale)
    total = zip(zipped)
    print(list(total))





main()
