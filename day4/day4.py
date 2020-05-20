def has_duplicate_digits(number):
    string_number = str(number)
    freq = [0] * 10
    pair = False
    duplicates = False
    for i in range(len(string_number)):
        freq[int(string_number[i])] += 1
    for f in freq:
        if f == 2:
            pair = True
            duplicates = True
        if f > 2:
            duplicates = True
    return pair and duplicates

def is_non_decreasing(number):
    string_number = str(number)
    for idx, digit in enumerate(string_number):
        if idx > 0 and digit < string_number[idx - 1]:
            return False
    return True

def num_passes(low, high):
    total_passwords = 0
    for i in range(low, high + 1):
        # test for duplicate numbers
        if has_duplicate_digits(i) and is_non_decreasing(i):
            total_passwords += 1
        # test for increasing sequence
    return total_passwords

print(num_passes(128392, 643281))