import sys as s
from ft_filter import ft_filter


def clean_word(word):
    """Strip punctuation characters from a word."""
    return "".join(ch for ch in word if ch.isalnum())


def main():
    """Entry point: parse args, filter words longer than N, print result."""
    args = s.argv[1:]

    try:
        assert len(args) == 2, "the arguments are bad"
        text = args[0]
        n = int(args[1])
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
    else:
        words = [clean_word(w) for w in text.split()]
        result = ft_filter(lambda word: len(word) > n, words)
        print(result)


if __name__ == "__main__":
    main()
