def NULL_not_found(object: any) -> int:
    if (object is None):
        print(f"Nothing: {object} {type(object)}")
    elif type(object) is float and object != object:  # Check for NaN : In Python, NaN stands for "Not a Number" and is a special floating-point value defined by the IEEE 754 standard to represent missing, undefined, or unrepresentable numerical data.
        print(f"Cheese: {object} {type(object)}")
    elif type(object) is int and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif type(object) is str and object == "":
        print(f"Empty: {type(object)}")
    elif type(object) is bool and object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0