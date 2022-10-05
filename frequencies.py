"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

# Return a dictionary mapping items onto their frequencies
def frequencies(items):
    frequencies = {}
    # Iterate through all items
    for item in items:
        # Convert all items into strings
        itemStr = str(item)
        # Increment the count for each item by 1
        if itemStr in frequencies:
            frequencies[itemStr] += 1
        # Or set it to 1 if the counter has not yet been initialised
        else:
            frequencies[itemStr] = 1
    # Return the dictionary
    return frequencies
