
def parsing_chars(string):
    # Extract first data point between b tags
    string = string.split('<b>', 1)[1]
    string = string.split('</b>',1)
    first = string[0]
    string = string[1] # Stay with rest
    # Second
    string = string.split('<b>', 1)[1]
    string = string.split('</b>',1)
    second = string[0]
    string = string[1] # Stay with rest
    # Thrid
    string = string.split('<b>',1)[1]
    string = string.split('</b>',1)
    third = string[0]
    return first, second, third    