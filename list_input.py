def access_index(names):
    first_value = names[0] # using the normal index to get the first value of the element
    last_value = names[-1]  # using slicing to get the last element of the array
    print(first_value , last_value)

    return names



print( access_index([1,349,43]))