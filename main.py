from dis import code_info
from time import time

from generator import Generator
import regexp_analyser
from state_machine_analyzer import SMCAnalyzer


def timeit(f):
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, *kwargs)
        print(time() - start)
        print("correct str: {}".format(result))
    return wrapper

@timeit
def smc_test(list):
    smc_correct_count = 0
    for i in list:
        smc = SMCAnalyzer()
        correct_smc = smc.check_str(i)
        if correct_smc:
            smc_correct_count += 1
    return smc_correct_count

@timeit
def regexp_test(list):
    correct_count = 0
    for i in list:
        correct_regexp = regexp_analyser.analyze(i)
        if correct_regexp:
            correct_count += 1
    return correct_count


if __name__ == '__main__':
    g = Generator()

    list = g.generate_list(500)
    regexp_test(list)
    smc_test(list)
