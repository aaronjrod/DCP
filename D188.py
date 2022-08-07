#Because scope of i in your case is of make_functions, you should make a separated scope for it, here I wrap it into a function
def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(i=i):
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()


