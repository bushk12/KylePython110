def main():
    # creation of the user string
    string = input("Please enter a sentence: ")

    # in order for the count variable to work, it needs to all be lowercase or uppercase.....
    lowercase = string.lower()

    # looking for most frequent letter by importing the counter class in collections (like I did last week)
    import collections


    common = (collections.Counter(lowercase).most_common(1)[0])
    print(f"The most common letter was: \n{common}")
    print()
    count = (collections.Counter(lowercase).most_common(3))
    print(f'The top three most common letters were: \n{count}')



if __name__ == '__main__':
    main()
