from commons.structures import FunList
from multiprocessing import Pool
from commons.parallel import par_filter


def capitalize(name):
    return name[:1].upper() + name[1:]

def long_names(name):
    return len(name) > 1


def clean_names(names):

    #return ",".join(map(capitalize,filter(lambda name: len(name) > 1,names)))
    return FunList(names).filter(lambda name: len(name) > 1).map(capitalize).join(",")

def clean_names_in_parallel(names):

    return ",".join(map(capitalize,par_filter(long_names,names)))
