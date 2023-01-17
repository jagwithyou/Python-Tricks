
# Write a Python program to get a new string from a given string where Is has been added to the front. If the given string already begins with Is then return the string unchanged

def add_string(input_string):
    if input_string.startswith("is"):
        return input_string
    else:
        return "is "+input_string

def alternate_add_string(input_string):
    return input_string if input_string.startswith("is") else "is "+input_string

if __name__ == "__main__":
    res = add_string("is he playing")
    print(res)
