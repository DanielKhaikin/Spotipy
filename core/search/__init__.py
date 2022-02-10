from core.search.search import get_top_songs, get_songs_from_album, get_artist_albums_names, get_artists_names


def search(search_func, is_premium):
    results = search_func
    if is_premium or (not is_premium and len(results) > 5):

        return results

    else:

        return results[0:5]



