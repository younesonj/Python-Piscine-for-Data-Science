import sys as s


def main():
    """Entry point: validate one string argument, print its Morse encoding."""
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
        "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
        "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
        "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
        "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
        "Y": "-.--",  "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",
    }
    args = s.argv[1:]

    try:
        assert len(args) == 1, "the arguments are bad"
        text = args[0]
        assert all(
            ch.isalnum() or ch == " " for ch in text
        ), "the arguments are bad"
    except AssertionError:
        print("AssertionError: the arguments are bad")
    else:
        result = " ".join(NESTED_MORSE.get(ch.upper(), "") for ch in text)
        print(result)


if __name__ == "__main__":
    main()
