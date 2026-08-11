ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# LIST :
#No fixed type. A list can hold mixed types in the same container
ft_list[1] = "World!"

# TUPLE :
#ft_tuple[1] = "World!" # This will raise an error because tuples are immutable
ft_tuple = (ft_tuple[0], "Morocco!") # This is how you can create a new tuple with the desired value

# SET :
#Sets are unordered collections of unique elements. You can add or remove elements from a set.
ft_set.remove("tutu!")
ft_set.add("Casablanca!")

# DICTIONARY :
#Dictionaries are mutable and can hold key-value pairs. You can add, remove, or modify elements in a dictionary.
ft_dict["Hello"] = "1337Benguerir!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)