#counts the number of words in the book
def count_words(book_contents):
    return len(book_contents.split())

#counts the number of each character in the book and returns a dictionary of each character and their quantity
def char_count(book_contents):
    char_dict = {}
    contents_lower = book_contents.lower()
    for char in contents_lower:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict

#sort key function
def sort_on(dict):
    return dict["count"]

#takes a dictionary of characters and their counts and returns a sorted list of dictionaries
def sorted_list_char_dict(unsorted_char_dict):
    sorted_char_list_of_dicts = []
    char_list = list(unsorted_char_dict)
    for char in char_list:
        char_dict = {}
        if char.isalpha() == True:
            char_dict["char"] = char
            char_dict["count"] = unsorted_char_dict[char]
            sorted_char_list_of_dicts.append(char_dict)

    sorted_char_list_of_dicts.sort(reverse=True, key=sort_on)
            
    return sorted_char_list_of_dicts
    