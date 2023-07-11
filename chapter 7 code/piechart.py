import matplotlib.pyplot as plt


def main():
    expense = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']
    price = [990, 100, 250, 200, 145, 80]

    plt.pie(price, labels=expense)

    plt.title('Monthly Expenses')

    plt.show()


if __name__ == '__main__':
    main()
