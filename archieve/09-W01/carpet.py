def solution(brown, yellow):
    m_yellow = yellow
    answer = []
    n = 1

    while True:
        yllw = n * yellow

        if yllw == m_yellow:
            brwn = ((yellow + 2) * 2) + (n * 2)

            if brwn == brown:
                answer.append((yellow + 2))
                answer.append((n + 2))
                return answer

            else:
                pass

        n += 1
        yellow = m_yellow // n