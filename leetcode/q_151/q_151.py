def reverseWords(s):
    s = s.split(' ')
    return_str=''
    for i in s[::-1]:
        if i != '':
            return_str += i + ' '
    return return_str.strip()

print(reverseWords("Alice does not even like bob"))