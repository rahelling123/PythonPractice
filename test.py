




#this kata works but takes too long when doing large numbers, (200**2, 200**3)
# def last_digit(n1, n2):
#     if n1==0 and n2==0:
#         return 0
#     else:
#         answer = n1**n2
#         answer_list = list(str(answer))
#
#         return answer_list[len(answer_list)-1]
#
#
# result = last_digit(2**200,2**300)
# print(result)





# a = 2342
# b = list(str(a))
#
# def test_yield(a):
#     a = 2342
#     b = list(str(a))
#     for i in b:
#         yield i
#
# value = test_yield(12345)
# print(value)
# for i in value:
#     print(i)