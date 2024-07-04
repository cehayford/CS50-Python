# def switch(greetings):
#     if greetings == 'Hello':
#         return '$0'
#     if greetings == 'Hello, Newman':
#         return '$0'
#     if greetings == 'How you doing?':
#         return '$20'
#     if greetings == 'Hello':
#         return '$100'

# inp = input()
# print(switch(inp))

inp = input("Response? ")
answer = inp.lower().strip()

if 'hello' in answer:
    print('$0')
elif 'h' == answer[0]:
    print('$20')
else:
    print('$100')


