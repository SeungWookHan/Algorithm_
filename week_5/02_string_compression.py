input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    compression_length_array = []
    for split_size in range(1, n // 2 + 1):
        splited = []
        compressed = ""
        # for i in range(0, n, split_size):
            # splited.append(string[i: i+split_size])
            # 위 문장을 더 멋지게
        splited = [
            string[i: i + split_size] for i in range(0, n, split_size)
        ]
        # 압축할 수 있는 여부 알기
        count = 1 # 카운트의 초기값은 1이여야함 이전값과 자기값을 비교하는 것이기 때문에
        for j in range(1, len(splited)): # 1부터인 이유는 이전값이랑 지금값이랑 비교하기 위함
            prev, cur = splited[j-1], splited[j]
            if prev == cur:
                count += 1
            else:
                if count > 1: # 2개 이상부터는 압축해주는 것이 좋음
                    compressed += (str(count) + prev)
                else: # 1개라면 압축할 필요없이 추가
                    compressed += prev
                count = 1

        # 꼬다리 처리(남은 것 처리)
        if count > 1:
            compressed += (str(count) + splited[-1])
        else:
            compressed += splited[-1]
        compression_length_array.append(len(compressed))
    return min(compression_length_array)


print(string_compression(input))  # 14 가 출력되어야 합니다!