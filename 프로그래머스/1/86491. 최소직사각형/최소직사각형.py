def solution(sizes):
    max_width, max_height = 0, 0
    for size in sizes:
        temp_size = sorted(size)
        if max_width < temp_size[0]:
            max_width = temp_size[0]
        if max_height < temp_size[1]:
            max_height = temp_size[1]
            
    answer = max_width * max_height
    return answer