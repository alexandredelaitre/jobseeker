inputs = [[1, 1], [1, 0], [1, -1], [10, 11]]
outputs = [2, 1, 0, 21]


def check_function(func, inputs, outputs):
    for n in range(len(inputs)):
        i = inputs[n]
        out = func(*i)
        if outputs[n] != out:
            return False
    return True


def parse_and_check_function(func_str, inputs, outputs):
    for n in range(len(inputs)):
        i = inputs[n]
        ex_locals = {}
        exec(func_str + '\n' +
             'zzzzzzzzzzzzzzzzzzzzzzz = ((main(' + ",".join(str(a) for a in i) + ')) ==' + str(
            outputs[n]) + ')', None, ex_locals)

        if not bool(ex_locals['zzzzzzzzzzzzzzzzzzzzzzz']):
            return False
    return True


print(parse_and_check_function("""
def main(a, b):
    return a + b
""", inputs, outputs))

print(parse_and_check_function("""
def main(a, b):
    return a * b
""", inputs, outputs))
