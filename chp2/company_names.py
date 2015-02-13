def clean_names(names):
    def capitalize(name): return  name[:1].upper() + name[1:]

    return ",".join(map(capitalize,filter(lambda name: len(name) > 1,names)))

