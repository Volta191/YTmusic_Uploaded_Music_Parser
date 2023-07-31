from ytmusicapi import YTMusic

yt = YTMusic("oauth.json")

songs = yt.get_library_upload_songs(limit=3000, order="a_to_z")

# Process the data and remove the "id" key from the "artists" dictionary
for song in songs:
    if "artists" in song and isinstance(song["artists"], list):
        for artist in song["artists"]:
            if isinstance(artist, dict) and "id" in artist:
                artist.pop("id", None)

# Now, write the modified song data to the "tracklist.txt" file
with open("tracklist.txt", "w", encoding="utf-8") as file:
    if songs:
        file.write("List of Uploaded Songs:\n")
        for song in songs:
            if "artists" in song and isinstance(song["artists"], list):
                artist_names = ", ".join(artist["name"] for artist in song["artists"] if isinstance(artist, dict))
            else:
                artist_names = "(No artist information)"

            album_name = song['album']['name'] if song.get('album') else "(No album information)"

            track_info = f"{artist_names} - {song['title']}\n"
            file.write(track_info)
    else:
        file.write("No uploaded songs found.\n")