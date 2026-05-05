def determinant(n):
    det_2, det_1 = 1, 2
    yield det_1

    for i in range(2, n + 1):
        det = 2 * det_1 - 3 * det_2
        yield det
        det_2, det_1 = det_1, det

