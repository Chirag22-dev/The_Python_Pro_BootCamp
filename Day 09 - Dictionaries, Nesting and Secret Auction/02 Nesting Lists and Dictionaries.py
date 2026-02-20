# Dictionary containing states of India as keys
# Each state contains another dictionary as its value
States_of_India = {
    "Karnataka": {
        # List of cities visited in Karnataka
        "cities_visited": ["Bengaluru", "Mysore", "Coorg"],

        # Number of times Karnataka was visited
        "Num_of_times_visited": 2
    },

    "Andhra_Pradesh": {
        # List of cities visited in Andhra Pradesh
        "cities_visited": ["Hyderabad", "Tirupati"],

        # Number of times Andhra Pradesh was visited
        "Num_of_times_visited": 3
    }
}

# Accessing:
# 1. Andhra_Pradesh dictionary
# 2. cities_visited list inside it
# 3. The city at index 1 (second city)
print(States_of_India["Andhra_Pradesh"]["cities_visited"][1])
