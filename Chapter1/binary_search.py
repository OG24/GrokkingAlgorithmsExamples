import random


class BinarySearch:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def arrange_borders(self, number_input, guess_input):
        if number_input < guess_input:
            self.lower_bound = int((self.lower_bound + self.upper_bound) / 2)
            print('Increase your guess')
        elif number_input > guess_input:
            self.upper_bound = int((self.lower_bound + self.upper_bound) / 2)
            print('Decrease your guess')
        else:
            print('You won the game')
            return


if __name__ == "__main__":
    bounds = 0, 1000
    binary_search = BinarySearch(bounds[0], bounds[1])
    number = random.randint(bounds[0], bounds[1])
    guess = -1
    while guess != number:
        print("My suggestion is {}".format(int((binary_search.lower_bound + binary_search.upper_bound) / 2)))
        guess = int(input('Write your guess: '))
        binary_search.arrange_borders(guess, number)
