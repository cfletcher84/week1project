from flask import Flask, request, jsonify
from songlist import Playlist, Song

app = Flask(__name__)

playlists = {}

def get_playlist(id):
    for i in playlists:
        if i['id'] == id:
            return i
    return None

def get_song(playlist, song):
    for i in playlist['songs']:
        if i['title'] == song:
            return song
    return None

@app.route('/')
def index():
    return 'Welcome to the playlist manager!'
        
@app.route('/playlist/create', methods=['POST'])
def add_playlist():
    data = request.json
    if data:
        playlists.append(data)
        return jsonify({"Message": "Playlist created!"}), 201
    else:
        return jsonify({"Message": "There is an error with your data"}), 400
    
@app.route('/playlist/<id>/add_song', methods=['POST'])
def add_song(id):
    data = request.json
    playlist = get_playlist(id)
    if not playlist:
        return jsonify({"Message": "No playlist found!"}), 404
    else:
        return jsonify({"Message": "Sucesfully added song!"})

@app.route('/playlist/<id>', methods=['GET'])
def get_playlist(id):
    playlist = get_playlist(id)
    if playlist:
        return jsonify(playlist)
    else:
        return jsonify({"Message": "No playlist found!"}), 404
    
@app.route('/playlist/search', methods=['GET'])
def search_song(title):
    pass
    
@app.route('/playlist/update/<id>', methods=['PUT'])
def update_playlist(id):
    playlist = get_playlist(id)
    if not playlist:
        return jsonify({"Message" "No playlist found."}), 404
    else:
        data = request.json
        playlist.update(data)
        return jsonify({"Message": "Playlist updated!"}), 201

@app.route('/playlist/delete/<id>', methods=['DELETE'])
def delete_playlist(id):
    playlist = get_playlist(id)
    if not playlist:
        return jsonify({"Message": "Playlist not found!"}), 404
    else:
        playlists.remove(playlist)
        return jsonify({"Message": "Playlist succesfully removed."}), 201

@app.route('/playlist/<id>/remove_song/<song_id>', methods=['DELETE'])
def remove_song(id, song_id):
    playlist = get_playlist(id)
    if not playlist:
        return jsonify({"Message": "No playlist with that ID"}), 404
    else:
        return jsonify({"Message": "Song deleted!"})




# I know half of this stuff isnt working and imcomplete but i am at the end and i have to turn in what i have! I got way behind here!! 



if __name__ == '__main__':
    app.run(debug=True)