"""one shot worldle, a continuation of ex01."""
__author__ = "730456646"

secret: str = "python"
length: int = len(secret)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
emoji_result: str = ""

guess: str = input(f"What is your {length}-letter guess? ")
while len(guess) != length: 
    guess = input(f"That was not {length} letters! Try again: ")

while i < len(secret):
    # if letter matches, green emoji
    if guess[i] == secret[i]:
        emoji_result = emoji_result + GREEN_BOX
        i = i + 1
    else:
        # loop changes bool value contained_in_word if indexed value is found in other part of secret word
        contained_in_word: bool = False 
        i_two: int = 0
        while i_two < len(secret) and contained_in_word is False:
            if secret[i_two] == guess[i]:
                contained_in_word = True
            else:
                i_two = i_two + 1

        if contained_in_word is True:
            emoji_result = emoji_result + YELLOW_BOX
            i = i + 1
        else:
            emoji_result = emoji_result + WHITE_BOX
            i = i + 1

if guess == secret:
    print(emoji_result)
    print("Woo! You got it!")
else:
    print(emoji_result)
    print("Not quite. Play again soon!")