from flask import Flask, render_template, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# Global variables to store music player state
current_state = 'stopped'
current_song = None
playlist = []
current_index = -1

# Sample playlist to start with
sample_songs = [
    "spotify_song1", 
    "spotify_song2",
    "local_song1.mp3", 
    "local_song2.mp3"
]

# Initialize playlist with sample songs
playlist = sample_songs.copy()

@app.route('/')
def index():
    """Serve the main music player interface"""
    return render_template('Interface.html')

@app.route('/api/status')
def get_status():
    """Get current player status"""
    return jsonify({
        'state': current_state,
        'current_song': current_song,
        'playlist': playlist,
        'current_index': current_index
    })

@app.route('/api/play', methods=['POST'])
def play():
    """Start playing music"""
    global current_state, current_song, current_index
    
    if not playlist:
        return jsonify({'status': 'error', 'message': 'No songs in playlist'})
    
    if current_index == -1:
        current_index = 0
    
    current_song = playlist[current_index]
    current_state = 'playing'
    
    return jsonify({'status': 'success', 'message': f'Now playing: {current_song}'})

@app.route('/api/pause', methods=['POST'])
def pause():
    """Pause music"""
    global current_state
    
    if current_state == 'playing':
        current_state = 'paused'
        return jsonify({'status': 'success', 'message': 'Music paused'})
    else:
        return jsonify({'status': 'error', 'message': 'No music playing'})

@app.route('/api/stop', methods=['POST'])
def stop():
    """Stop music"""
    global current_state, current_song, current_index
    
    current_state = 'stopped'
    current_song = None
    current_index = -1
    
    return jsonify({'status': 'success', 'message': 'Music stopped'})

@app.route('/api/skip', methods=['POST'])
def skip():
    """Skip to next song"""
    global current_index, current_song
    
    if not playlist:
        return jsonify({'status': 'error', 'message': 'No songs in playlist'})
    
    if current_index < len(playlist) - 1:
        current_index += 1
    else:
        current_index = 0  # Loop back to first song
    
    current_song = playlist[current_index]
    
    if current_state == 'playing':
        return jsonify({'status': 'success', 'message': f'Skipped to: {current_song}'})
    else:
        return jsonify({'status': 'success', 'message': f'Selected: {current_song}'})

@app.route('/api/previous', methods=['POST'])
def previous():
    """Go to previous song"""
    global current_index, current_song
    
    if not playlist:
        return jsonify({'status': 'error', 'message': 'No songs in playlist'})
    
    if current_index > 0:
        current_index -= 1
    else:
        current_index = len(playlist) - 1  # Loop to last song
    
    current_song = playlist[current_index]
    
    if current_state == 'playing':
        return jsonify({'status': 'success', 'message': f'Previous song: {current_song}'})
    else:
        return jsonify({'status': 'success', 'message': f'Selected: {current_song}'})

@app.route('/api/add_song', methods=['POST'])
def add_song():
    """Add a new song to playlist"""
    global playlist
    
    data = request.get_json()
    song = data.get('song', '').strip()
    
    if not song:
        return jsonify({'status': 'error', 'message': 'Song name cannot be empty'})
    
    if song in playlist:
        return jsonify({'status': 'error', 'message': 'Song already in playlist'})
    
    playlist.append(song)
    
    return jsonify({'status': 'success', 'message': f'Added: {song}'})

@app.route('/api/remove_song', methods=['POST'])
def remove_song():
    """Remove a song from playlist"""
    global playlist, current_index, current_song
    
    data = request.get_json()
    song = data.get('song', '').strip()
    
    if song not in playlist:
        return jsonify({'status': 'error', 'message': 'Song not found in playlist'})
    
    # Remove the song
    playlist.remove(song)
    
    # Adjust current index if necessary
    if current_song == song:
        current_song = None
        current_index = -1
    elif current_index >= len(playlist):
        current_index = len(playlist) - 1
        if current_index >= 0:
            current_song = playlist[current_index]
    
    return jsonify({'status': 'success', 'message': f'Removed: {song}'})

@app.route('/api/playlist')
def get_playlist():
    """Get current playlist"""
    return jsonify({
        'playlist': playlist,
        'current_song': current_song,
        'current_index': current_index
    })

@app.route('/api/current_song')
def get_current_song():
    """Get current song info"""
    return jsonify({
        'current_song': current_song,
        'state': current_state
    })

if __name__ == '__main__':
    print("🎵 Music Player Web Application Starting...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Move Interface.html to templates folder
    if os.path.exists('Interface.html'):
        import shutil
        shutil.move('Interface.html', 'templates/Interface.html')
    
    app.run(debug=True, host='0.0.0.0', port=5000)

