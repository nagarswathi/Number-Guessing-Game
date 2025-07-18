import random

class Solution:
    def __init__(self):
        self.number = random.randint(1,100)
        self.difficulty = 0
        self.difficulty_hash = {'1':("Easy",10), "2":("Medium",5), "3": ("Hard", 3)}
    def welcome(self):
        print("""Welcome to the Number Guessing Game!
        I'm thinking of a number between 1 and 100.
        You have 5 chances to guess the correct number.

        Please select the difficulty level:
        1. Easy (10 chances)
        2. Medium (5 chances)
        3. Hard (3 chances)""")
        self.difficulty = input("Enter your choice: ")
        attempts = self.difficulty_hash[self.difficulty][1]
        
        print(f"""Great! You have selected the {self.difficulty_hash[self.difficulty][0]} difficulty level.\n Let's start the game!""")
        self.check_correctness(attempts)
        
    def check_correctness(self, attempts):
        for i in range(attempts):
            guess_number = int(input("Enter your guess: "))
            if guess_number == self.number:
                print(f"Congratulations! You guessed the correct number in {i} attempts.")
                break
            elif guess_number > self.number:
                print(f"Incorrect! The number is less than {guess_number}.")
            else:
                print(f"Incorrect! The number is greater than {guess_number}.")

        print(f"You've used all attempts. The correct number was {self.number}.")

if __name__ == "__main__":
    game = Solution()
    game.welcome()
