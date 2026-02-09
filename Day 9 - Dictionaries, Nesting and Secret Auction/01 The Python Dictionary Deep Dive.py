# Creating a dictionary with key-value pairs
dict = {
    "God": "The Almighty, Supreme.",
    "Animal": "The creature"
}

# Printing the entire dictionary
print(dict)

# Printing the value associated with the key "God"
print(dict["God"])

# Adding a new key-value pair to the dictionary
dict["Human"] = "The intelligent creature"

# Printing the updated dictionary
print(dict)

# Looping through each key in the dictionary
for key in dict:
    # Printing the current key
    print(key)

    # Printing the value corresponding to the current key
    print(dict[key])

# Reassigning the dictionary to an empty dictionary
dict = {}

# Printing the empty dictionary
print(dict)
