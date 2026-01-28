def suggest_songs(n, songs, x, y, k):
    preferred_genre_songs = []
    other_genre_songs = []
    current_genre = None

    for song in songs:
        song_id, genre, popularity = song
        if song_id == x:
            current_genre = genre
            break

    for song in songs:
        song_id, genre, popularity = song
        if genre == y:
            preferred_genre_songs.append(song)
        elif genre != current_genre:
            other_genre_songs.append(song)

    preferred_genre_songs.sort(key=lambda x: (x[2], x[0]))
    other_genre_songs.sort(key=lambda x: (x[2], x[0]))

    result = []
    for song in preferred_genre_songs:
        if len(result) < k:
            result.append(song[0])

    if len(result) < k:
        for song in other_genre_songs:
            if len(result) < k:
                result.append(song[0])
            else:
                break

    # This will cause issues if x is not in the songs list

    if not result:
        return -1

    return result