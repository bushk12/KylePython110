# Creating a magic 8-ball program where the user inserts a question and the program responds with a random response
import random
import time
def main():
    # asking the question, allowing the user to immediately quit if they want
    question = input("Ask the magic 8-ball a question (or press enter to quit).")
    while question:
        if question == "quit":
            break
        # adding a random time for suspense
        print("I am thinking....")
        for i in range(random.randrange(1, 12)):
            print(". ", end='')
            time.sleep(1)
        print("\n")
        # grabbing one of the answers from the text file randomly
        print((random.choice(open("8_ball_responses.txt","r").read().splitlines())) + " .")
        # going back to the initial question to see if the user wants to ask again, or quit
        question = input("Ask the magic 8-ball a question (or press enter to quit): ")

main()