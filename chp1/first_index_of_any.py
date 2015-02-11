from fn.iters import first

def first_index_of(string,chars):
    indexed = zip(range(0,len(string)),string)

    def lazy_index_generator():
        for pair in indexed:
            for c in chars:
                if c == pair[1]:
                    yield pair[0]


    return first(lazy_index_generator())

