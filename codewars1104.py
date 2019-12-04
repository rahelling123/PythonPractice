
def done_or_not(board):
    for i in range(1,10):
        if i in board[i-1]:
            continue
        else:
            return 'Try again!'

    for i in range(0,9):
        column = get_column(i, board)
        for int in range(1,10):
            if int in column:
                continue
            else:
                return 'Try again!'

    return 'Finished!'


def get_column(i, board):
    column = []
    for c in range(0,9):
        column.append(board[c][i])
    return column

def check_section(board):

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list_total = []

    values = []
    for x in range(0,3):
        for y in range(0,3):
            list1.append([x, y])
            list2.append([x, y+3])
            list3.append([x, y+6])
            list4.append([x+3, y])
            list5.append([x+3, y+3])
            list6.append([x + 3, y + 6])
            list7.append([x+6, y])
            list8.append([x+6, y+3])
            list9.append([x + 6, y + 6])

    list_total = (list1, list2, list3, list4, list5, list6, list7, list8, list9)

    numbers = []
    for x in range(0,9):
        for y in range(0,9):
            numbers.append(board[x][y])
            for i in range(0,9):
                if i in numbers:
                    continue
                else:
                    return 'Try again!'
        return "Finished!"


result = done_or_not(([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 9]]))

print(result)









# learning about multiplying strings
# def triple_double(num1, num2):
#     values1 = list(str(num1))
#     values2 = list(str(num2))
#     num1_triple = 0
#     num2_double = 0
#     same_num = 0
#
#     for i in range(0, (len(values1) - 3)):
#         if values1[i] == values1[i + 1] == values1[i + 2]:
#             same_num = str(values1[i])
#             num1_triple = 1
#         # return num1_triple
#
#     for i in range(0, (len(values2) - 1)):
#         if values2[i] == values2[i + 1] and values2[i] == same_num:
#             num2_double = 1
#         # return num2_double
#
#     if num1_triple and num2_double == 1:
#         return 1
#     else:
#         return 0
#
# answer = triple_double(451999277, 41177722899)
# print(answer)




# UNIQUE - PASSED
# def unique_in_order(iterable):
#     values = list(iterable)
#     unique = []
#     old_value = '!'
#     for value in values:
#         if value == old_value:
#             continue
#         else:
#             unique.append(value)
#         old_value = value
#     print(unique)
#     return unique
#
#
# unique = unique_in_order([1,2,2,3,3])
# print(unique)


#ALPHABET CODE - PASSED
# import string
#
#
# def alphabet_position(text):
#     characters = list(text)
#     locations = ''
#
#     for char in characters:
#         if char.isalpha():
#             char = char.lower()
#             new_location = string.ascii_lowercase.index(char) + 1
#             locations = locations + ' ' + str(new_location)
#         else:
#             pass
#     return locations.lstrip()
#
#
# position = alphabet_position('The sunset sets at twelve o clock.')
# print(position)


