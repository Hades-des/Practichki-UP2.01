def reverse_string(input_str):
    return input_str[::-1]
def capitalize_words(input_str):
    words = input_str.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)