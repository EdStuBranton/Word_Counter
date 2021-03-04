import re
import os


filepath = r'add filepath'

def collect_filenames(path):
    list_of_filenames = []
    for filename in os.listdir(path):
        list_of_filenames.append(filename)
    return list_of_filenames

def open_file(filename):
    with open(r'add filepath' + '\\' + filename) as f:
        content = f.read()
    return content

def unwanted_char_check(filecontent):
    pattern = "[^'a-zA-Z0-9 ]"
    clean_content = re.sub(pattern, " ", filecontent)
    return clean_content

def split_into_list(string):
    split_content = string.split(' ')
    return split_content

def words_counter(array):
    word_dictionary = {}
    for word in array:
        if isinstance(word, str):
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary[word] = 1
    return word_dictionary

for filename in collect_filenames(filepath):
    content_of_file = open_file(filename)
    cleaned_up_content = unwanted_char_check(content_of_file)
    split_content_array = split_into_list(cleaned_up_content)
    result = words_counter(split_content_array)
    print(result)
