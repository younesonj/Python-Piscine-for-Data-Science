import sys as s

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

args = s.argv[1:]

if (len(args) == 0):
    pass
else:
    try:
        assert len(args) == 1, "more than one argument is provided"
        assert is_integer(args[0]), "argument is not an integer"
    except AssertionError as e:
        print(f"AssertionError: {e}")
    else:
        n = int(args[0])
        if n % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")