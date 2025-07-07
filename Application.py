import json
import random

class Application:
    def __init__(self):
        self.data = []
        self.words_data = []
        self.running = True
        self.score = 0
        self.attempts = 0

        self._read_json_file()

    def _read_json_file(self):
        with open('words/words.json', 'r') as file:
            data = json.load(file)
        self.data = data['application']
        self.choose_type()


    def restart(self):
        self.score = 0
        self.attempts = 0
        self.choose_type()

    def choose_type(self):
        for d in self.data:
            print(f"Type: {d}")
        type_choose = input("Choose your type: ")
        try:
            self.words_data = self.data[type_choose]
        except KeyError:
            self.running = False
            print("Key error")


    def run(self):
        while self.running:
            if not self.words_data:
                ans = input("Words list is empty (reset, exit)->")
                if ans == 'reset':
                    self.restart()
                if ans == 'exit' or not ans:
                    self.running = False
                    break
            random_number = random.randint(0, len(self.words_data) - 1)
            random_pair = self.words_data[random_number]
            self.words_data.pop(random_number)
            random_number = random.randint(0, 1)
            word = random_pair[random_number]
            answer = input(f"Enter your answer ({word})->")
            self.attempts += 1

            if random_number == 0:
                if answer == random_pair[1]:
                    print("Correct!")
                    self.score += 1
                else:
                    print("Wrong answer!")

            if random_number == 1:
                if answer == random_pair[0]:
                    print("Correct!")
                    self.score += 1
                else:
                    print("Wrong answer!")

            print(f"Your score is now {self.score}/{self.attempts}")
            if answer == "exit":
                self.running = False

            if answer == "reset":
                self.restart()


