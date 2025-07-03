import random
words = ["apple", "house", "python", "chair", "flower","College","india","mountain","humans","monkey","elephant","dog","mental","cat","java",]
word_to_guess = random.choice(words)
guessed_letters = []
tries = 6

print("🎮 Welcome to Hangman!")
print("_ " * len(word_to_guess))

while tries > 0:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess! ✅")
    else:
        tries -= 1
        print(f"Wrong guess! ❌ You have {tries} tries left.")
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\n" + display_word.strip())
    if all(letter in guessed_letters for letter in word_to_guess):
        print("\n🎉 Congratulations! You guessed the word correctly!")
        break
else:
    print(f"\n💀 Game Over! The word was '{word_to_guess}'. Better luck next time!")
