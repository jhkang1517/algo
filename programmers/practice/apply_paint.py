def solution(n, m, section):
    answer = 1 # 무조건 한번은 칠하고 시작함
    prev = section[0]  # 첫 번째로 페인트 칠을 시작할 지점
    for sec in section:
        if sec - prev >= m:  # 칠해야 할 구역에서 페인트 칠을 시도하였을 때, 롤러 길이보다 긴 경우,
            prev = sec # 페인트 칠 시작 지점을 현재 구역으로 바꾸고,
            answer += 1 # 페인트 칠 수행

    return answer
