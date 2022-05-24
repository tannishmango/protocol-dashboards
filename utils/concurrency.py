from multiprocessing import Process
import concurrent.futures

def run_concurrency(fns):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        data = [result for result in executor.map(lambda x: x(), fns)]
    return data

def run_in_parallel(*fns):
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()