def func(req):
    if req.lower().strip() == '42' or req.lower().strip() == 'forty two' or req.lower().strip() == 'forty-two':
        return 'Yes'
    else:
        return 'No'



data = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
f = func(data)
print(f)


# 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