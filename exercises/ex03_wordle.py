"""A more structured 6-guess limit wordle using functions."""
__author__ = "730456646"


def contains_char(guess: str, letter: str):
    """Searches through guessed word to see if the word contains the letter."""
    assert len(letter) == 1
    i: int = 0
    while i < len(guess):
        if guess[i] == letter:
            return True
        else:
            i += 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Will create emojified string based on which letters are correct, contained, or not present in word."""
    assert len(guess_word) == len(secret_word)
    white: str = "\U00002B1C"
    green: str = "\U0001F7E9"
    yellow: str = "\U0001F7E8"
    i: int = 0
    emojified_string: str = ""
    while i < len(guess_word):
        """green box added if correct"""
        if guess_word[i] == secret_word[i]:
            emojified_string += green
            i += 1
        elif contains_char(secret_word, guess_word[i]):
            """yellow box added if in word but not in the right place"""
            emojified_string += yellow
            i += 1
        else:
            """white box otherwise"""
            emojified_string += white
            i += 1
    return emojified_string


def input_guess(word_length: int) -> str:
    """Will return guess of inputed length and reject other guesses of wrong length."""
    new_guess: str = input(f"Enter a {word_length} character word: ")
    while len(new_guess) != word_length:
        new_guess = input(f"That wasn't {word_length} chars! Try again: ")
    return new_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret: str = "codes"
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess_main: str = input_guess(len(secret))
        print(emojified(guess_main, secret))
        if guess_main == secret:
            print(f"You won in {turn}/6 turns!")
            exit()
        else:
            turn += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()