import random


class WordGame:
    """
    A class to represent a word game where players can form words from a random string.
    """

    def __init__(self, init_callback) -> None:
        self.random_string_length = 7
        self.min_word_length = 3
        self.word_count_range = [3, 5]

        self.word_list = None
        self.random_string = None
        self.formable_words_list = []
        self.formable_words_count = 0
        self.found_words_list = []
        self.score = 0

        self.init_callback = init_callback
        self.recursion_limit = 10
        self.recursions = 0

        self.init()

    def init(self) -> None:
        """Initializes the game by generating a random string and a list of formable words."""
        self.recursions += 1

        try:
            self.read_lines_from_file('./wordlist.txt')
            self.generate_random_string()
            self.generate_formable_words_list()

            are_enough = self.word_count_range[0] < self.formable_words_count
            are_not_too_many = self.formable_words_count < self.word_count_range[1]
            recursion_limit_not_exceeded = self.recursions < self.recursion_limit

            if not (are_enough and are_not_too_many) and recursion_limit_not_exceeded:
                self.init()
                return

            self.init_callback()

        except Exception as error:
            print(f"Error initializing the game: {error}")

    def submit_word(self, word) -> None:
        """Submits a word to check if it's formable from the random string."""
        is_correct = word in self.formable_words_list
        if is_correct:
            self.found_words_list.append(word)
            self.score += 1

    def generate_random_string(self) -> None:
        """Generates a random string of specified length."""
        characters = 'abcdefghijklmnopqrstuvwxyz'
        self.random_string = ''.join(random.choice(
            characters) for _ in range(self.random_string_length))

    def count_occurrences(self, s) -> dict:
        """Counts the occurrences of each character in a given string."""
        count_map = {}
        for char in s:
            count_map[char] = count_map.get(char, 0) + 1
        return count_map

    def can_form_word(self, word, random_string_count_map) -> bool:
        """Checks if a word can be formed from the random string."""
        word_count_map = self.count_occurrences(word)
        for letter, count in word_count_map.items():
            if random_string_count_map.get(letter, 0) < count:
                return False
        return True

    def generate_formable_words_list(self) -> None:
        """Generates a list of words that can be formed from the random string."""
        random_string_count_map = self.count_occurrences(
            self.random_string or "")
        if self.word_list:
            self.formable_words_list = [
                word for word in self.word_list
                if len(word) >= self.min_word_length and self.can_form_word(word, random_string_count_map)
            ]
            self.formable_words_count = len(self.formable_words_list)

    def read_lines_from_file(self, file_path) -> None:
        """Reads lines from a file and stores them in the word list."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.word_list = file.read().splitlines()
        except Exception as err:
            print(f"Error reading file: {err}")
            raise err


if __name__ == "__main__":
    def init_game_callback() -> None:
        print("Game initialized successfully.")

    word_game = WordGame(init_callback=init_game_callback)
