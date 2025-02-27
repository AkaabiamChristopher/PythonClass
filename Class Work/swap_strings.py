def swap_strings(str1, str2):

     new_str1 = str2[:2] + str1[2:]
     new_str2 = str1[:2] + str2[2:]

     result = new_str1 + ' ' + new_str2
     return result

str1 = 'abc'
str2 = 'xyz'

result = swap_strings(str1, str2)