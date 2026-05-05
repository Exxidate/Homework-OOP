from MainClass import *

def parse_figure(line):
    parts = line.split()
    name = parts[0]
    nums = list(map(float, parts[1:]))

    if name == "Triangle":
        return Triangle(*nums)
    elif name == "Rectangle":
        return Rectangle(*nums)
    elif name == "Circle":
        return Circle(*nums)
    elif name == "Ball":
        return Ball(*nums)
    elif name == "Cone":
        return Cone(*nums)

    return None


def find_max_figure(filename):
    max_fig = None
    max_val = -1

    with open(filename) as f:
        for line in f:
            try:
                fig = parse_figure(line)
            except ValueError as e:
                print("Пропущено рядок:", line.strip())
                print("Причина:", e)

            if fig:
                val = fig.volume()
                if val > max_val:
                    max_val = val
                    max_fig = fig

    return max_fig, max_val

print(find_max_figure("input01.txt"))