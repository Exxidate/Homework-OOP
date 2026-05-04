import math

class Vector:
    def __init__(self, components):
        if isinstance(components, Vector):
            self.components = components.components[:]
        else:
            self.components = list(map(float, components))

    def __str__(self):
        return "(" + ", ".join(map(str, self.components)) + ")"

    def dimension(self):
        return len(self.components)

    def length(self):
        return math.sqrt(sum(x**2 for x in self.components))

    def mean(self):
        return sum(self.components) / self.dimension()

    def max_component(self):
        return max(self.components)

    def min_component(self):
        return min(self.components)

def read_vectors(filename):
    vectors = []

    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                nums = list(map(float, line.split()))
                vectors.append(Vector(nums))

    return vectors

def process_vectors(vectors):
    if not vectors:
        print("Немає векторів")
        return

    max_dim = max(v.dimension() for v in vectors)
    candidates = [v for v in vectors if v.dimension() == max_dim]
    best_dim_vector = min(candidates, key=lambda v: v.length())

    max_len = max(v.length() for v in vectors)
    candidates = [v for v in vectors if abs(v.length() - max_len) < 1e-9]
    best_len_vector = min(candidates, key=lambda v: v.dimension())

    avg_length = sum(v.length() for v in vectors) / len(vectors)

    count_longer = sum(1 for v in vectors if v.length() > avg_length)

    max_comp = max(v.max_component() for v in vectors)
    candidates = [v for v in vectors if v.max_component() == max_comp]
    best_max_comp_vector = min(candidates, key=lambda v: v.min_component())

    min_comp = min(v.min_component() for v in vectors)
    candidates = [v for v in vectors if v.min_component() == min_comp]
    best_min_comp_vector = max(candidates, key=lambda v: v.max_component())

    print("Вектори:")
    for v in vectors:
        print(v)

    print("\n1) Найбільша розмірність:", best_dim_vector)
    print("2) Найбільша довжина:", best_len_vector)
    print("3) Середня довжина:", avg_length)
    print("4) Кількість довших за середню:", count_longer)
    print("5) Макс компонента:", best_max_comp_vector)
    print("6) Мін компонента:", best_min_comp_vector)



vectors = read_vectors("input02.txt")
process_vectors(vectors)