from core.search.search import get_top_songs, get_songs_from_album, get_artist_albums_names, get_artists_names


def search(search_func, is_premium):
    results = search_func
    if is_premium:
        [print(result) for result in results]

    else:
        [print(results[i]) for i in range(5) if len(results) > i]

