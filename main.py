import spotify_engine2
import speechToText_engine
from spotify_engine2 import sp as sp
import datadog
import spotipy

#print([sub['id'] for sub in sp.current_user_playlists()['items'] if sub.get('name').lower()=='soup'])
#print(sp.start_playback(context_uri=[sub['uri'] for sub in sp.current_user_playlists()['items'] if sub.get('name').lower()=='soup'][0]))
#sp.start_playback(uris=[sub['uri'] for sub in sp.user_playlist(sp.current_user()['id'], playlist_id=sp.search('playlist:soup', type='playlist')['playlists']['items'][0]['id'])['tracks']['items']])
#print(sp.start_playback(uris=[sp.search('track:Party in the USA artist:Miley Cyrus', type='track')['tracks']['items'][0]['uri']]))
#print(sp.current_user_recently_played(limit=1)['items'][0]['track']['album']['images'][0]['url'])
#print(sp.currently_playing()['item']['album']['images'][0]['url'])
#sp.user_playlist_add_tracks(sp.current_user()['uri'], sp.user_playlist_create(sp.current_user()['display_name'], 'Soup Time', public='True', collaborative='False', description='')['id'], [sub['id'] for sub in sp.search('genre:pop', limit=15, type='track')['tracks']['items']])
dog = datadog.DataDog()
dog.run_stt()
while 1:
    pass
   # print("query: " + dog.stt_to_GUI.get()[0])
   # print("response: " + dog.chatGPT_to_GUI.get())

"""
uris, names, artists = spotify_engine.spotify_GetSongRecommendations()
print(uris)
print(names)
print(artists)

playlistID = spotify_engine.spotify_CreateNewPlaylist()
spotify_engine.spotify_AddSongsToPlaylist(playlistID, uris)
"""




#print(spotify_engine2.sp.current_user())
#print([sub['id'] for sub in spotify_engine2.sp.search('artist:Taylor Swift', limit=10, type='track')['tracks']['items']])
#print(spotify_engine2.sp.user_playlist_create(spotify_engine2.sp.current_user()['display_name'], 'Party Time', public='True', collaborative='False', description=''))
#sp.user_playlist_add_tracks(sp.current_user()['uri'], sp.user_playlist_create(sp.current_user()['display_name'], 'Party Time', public='True', collaborative='False', description='')['id'], [sub['id'] for sub in sp.search('artist:Taylor Swift', limit=10, type='track')['tracks']['items']])
#spotify_engine2.sp.user_playlist_add_tracks(spotify_engine2.sp.current_user()['uri'], spotify_engine2.sp.user_playlist_create(spotify_engine2.sp.current_user()['display_name'], 'Party Time', public='True', collaborative='False', description='')['id'], [sub['id'] for sub in spotify_engine2.sp.search('artist:Taylor Swift', limit=10, type='track')['tracks']['items']])

#Create a new playlist called party time, and add 10 taylor swift songs