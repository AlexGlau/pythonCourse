def string_comparison(string1, string2):
    if type(string1) != str or type(string2) != str:
        return '0'

    if string1 == string2:
        return 1

    if string1 != string2 and len(string1) > len(string2):
        return 2

    if string1 != string2 and string2 == 'learn':
        return 3

output1 = string_comparison(0, 1)
print(output1)
output2 = string_comparison('aaa', 'aaa')
print(output2)
output3 = string_comparison('aaaa', 'sss')
print(output3)
output4 = string_comparison('aaaaa', 'learn')
print(output4)

