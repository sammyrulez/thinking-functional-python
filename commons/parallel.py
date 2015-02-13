from multiprocessing import Pool

num_of_cores = 4


def par_filter(func, candidates):
    p = Pool(min(num_of_cores, len(candidates)))
    return [c for c, keep in zip(candidates, p.map(func, candidates)) if keep]
