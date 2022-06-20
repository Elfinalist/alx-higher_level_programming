def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for i in my_list:
            if num < x:
                print(f'{i}')
                num += i
        print(' ')
        return num
    except SyntaxError:
        print("Error Syntax")
