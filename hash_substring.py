# python3
# Kristiāns Šneiders, 221RDB042, 11.grupa
def read_input():
    userInput = input()
    if "I" in userInput:
        pattern = input()
        text = input()
    elif "F" in userInput:
        with open("./tests/06", mode = "r") as file:
            pattern = file.readline()
            text = file.readline()
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p_hash = hash(pattern)
    pattern_len = len(pattern)
    t_hash = hash(text[:pattern_len])
    text_len = len(text)
    positions = []
    
    i = 0
    
    while i <= text_len - pattern_len:
        if text[i:i+pattern_len] == pattern:
            positions.append(i)
        else:
            t_hash = hash(text[i+1:i+pattern_len+1])
        
        if t_hash == p_hash and text[i:i+pattern_len+1] != pattern:
            t_hash = hash(text[i+1:i+pattern_len+1])
        i += 1
    
    return positions


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

