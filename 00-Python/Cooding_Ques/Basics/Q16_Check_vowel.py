print("Enter a single alphabet character: ", end="")
ch = input().strip().lower()[0]

if ch in ("a", "e", "i", "o", "u"):
    print("It's a vowel.")
else:
    print("It's a consonant.")
