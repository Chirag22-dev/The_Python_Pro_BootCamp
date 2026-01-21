# Create a list of friends' names
friends = ["Ratan", "Sajin", "Poorna"]

# Print the element at index 1 (second item in the list)
print(friends[1])

# Print the last element of the list using negative indexing
print(friends[-1])

# Update the name at index 1
friends[1] = "Saajin"
print(friends[1])

# Add one new friend to the end of the list
friends.append("Shreyas")
print(friends)

# Add multiple new friends to the list
friends.extend(["Gagan", "Navaneeth"])
print(friends)
