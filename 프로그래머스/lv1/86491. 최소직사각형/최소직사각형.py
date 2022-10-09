def solution(sizes):
    answer = 0
    result_w = []
    result_h = []
    for i in range(len(sizes)):
        sizes[i].sort()
        result_w.append(sizes[i][0])
        result_h.append(sizes[i][1])
    return max(result_w) * max(result_h)