def main():
    print("Programming Exercise 10\n")
    # creation of the user string
    string = input("Please enter a sentence: ")

    # in order for the count variable to work, it needs to all be lowercase or uppercase.....
    lowercase = string.lower()

    # looking for most frequent letter by importing the counter class in collections (like I did last week)
    import collections

    # using the .Counter and .most_common to find the most common letter
    common = (collections.Counter(lowercase).most_common(1)[0])
    print(f"The most common letter was: \n{common}")
    print()
    # using the .Counter and .most_common to find the three most common letters
    count = (collections.Counter(lowercase).most_common(3))
    print(f'The top three most common letters were: \n{count}')


if __name__ == '__main__':
    main()
