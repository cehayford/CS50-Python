import emoji

inp = str(input('Input: '))
outp = emoji.emojize(inp, language='alias')
print('Output: {0}'.format(outp))

# v