
spindles = list(range(234, 728 + 38, 38)) + list(range(855, 1269 + 38, 38)) + list(range(1357, 1847 + 38, 38))
rod_length = 2000
cut_lengths = []

for spindle in spindles[::-1]:
    keep_trying = True
    current_index = 0
    while keep_trying:
        if current_index == len(cut_lengths):
            new_list = True
            length = []
        else:
            new_list = False
            length = cut_lengths[current_index]
        total = sum(length)
        if total + spindle < rod_length:
            length.append(spindle)
            if new_list:
                cut_lengths.append(length)
            keep_trying = False
        current_index += 1
print(len(spindles))
print(len(cut_lengths))
[print(sum(length)) for length in cut_lengths]
