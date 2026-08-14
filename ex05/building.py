import sys as s

def count_characters(text):
    """Count uppercase, lowercase, punctuation, spaces, and digits in a string."""
    upper = 0
    lower = 0
    pun = 0
    spaces = 0
    digits = 0
    for ch in text:
        if (ch.isupper()):
            upper += 1
        elif (ch.islower()):
            lower += 1
        elif (ch.isdigit()):
            digits += 1
        elif (ch.isspace()):
            spaces += 1
        elif not ch.isalnum() and not ch.isspace():
            pun += 1

    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{pun} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")

def main():
    """Entry point: get text from args or prompt, validate, and display counts."""
    args = s.argv[1:]
    try:
        assert len(args) <= 1, "more than one argument is provided"
        if (len(args) == 1):
            text = args[0]
        else:
            text = input("What is the text to count? " + "\n")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    else:
        print(f"The text contains {len(text)} characters:")
        count_characters(text)

if __name__ == "__main__":
    main()