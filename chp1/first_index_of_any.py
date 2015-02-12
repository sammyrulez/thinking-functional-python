from fn.iters import first

def first_index_of(string,chars):

    def lazy_index_generator():
        for pair in zip(range(0,len(string)),string):
            for c in chars:
                if c == pair[1]:
                    yield pair[0]


    return first(lazy_index_generator())

