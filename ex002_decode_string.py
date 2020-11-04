# write a function that given a string
# like '' 5 [a] 0 [c] 1 [e] returns
# the content inside the [] multiplied by
# number to its left
# aaaaae': five a, zero c and one e


def decode_string(string):
    result = ''
    string_to_repeat = ''
    multiplier = 0
    for char in string:

        if char.isnumeric():
            multiplier *= 10
            multiplier += int(char)
            continue

        if char == ']':
            result += string_to_repeat * multiplier
            string_to_repeat = ''
            multiplier = 0
            continue

        if char != '[':
            string_to_repeat += char

    return result


if __name__ == "__main__":
    print(decode_string('5[a]0[c]1[e])'))
    print(decode_string('3[ac]5[c]0[d]4[etg]'))
    # print(decode_string())
