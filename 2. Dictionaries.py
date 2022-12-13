# ////////////////////////
# //    Dictionaries    //
# ////////////////////////
dictionary = {
    "name": "tristan",
    "age": 16
}
print(dictionary)


# // Accessing Dictionaries
dictionary_name = dictionary["name"]
print(dictionary_name)


# // Setting key in dictionary
dictionary["name"] = "daniel"
print(dictionary)


# // Delete a key from a dictionary
del dictionary["name"]
print(dictionary)


# // Get length of a dictionary
dictionary_length = len(dictionary)


# // Use the .items() to iterate over a dictionary
for key, value in dictionary.items():
  print(f"{key}:{value}")
