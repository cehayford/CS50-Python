def func(req):
    statement = req
    split_data = statement.split(' ')
    new = '...'.join(split_data)
    print(new)

func("This is CS50")
func("This is our week on functions")
func("Let's implement a function called hello")