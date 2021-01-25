genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 장르 별로 재생된 횟수를 저장해야함
# 장르 별로 곡의 정보(인덱스, 재생횟수)를 배열로 묶어 저장한다.
def get_melon_best_album(genre_array, play_array):
    dict = {}
    genre_index_play_array = {}
    for i in range(len(genre_array)):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in dict:
            dict[genre] = play
            genre_index_play_array[genre] = [[i, play]]
        else:
            dict[genre] += play
            genre_index_play_array[genre].append([i, play])

    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    result = []
    for genre, _value in sorted_dict:
        index_play_array = genre_index_play_array[genre]
        sorted_index_play_array = sorted(index_play_array, key=lambda item:item[1], reverse=True)

        for i in range(len(sorted_index_play_array)):
            if i > 1:
                break
            result.append(sorted_index_play_array[i][0])
    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!