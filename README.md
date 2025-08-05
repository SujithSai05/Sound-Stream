#  Music Player Web Application

A beautiful web-based music player built with Flask, HTML, CSS, and JavaScript.

## Features

- 🎵 Play, pause, stop, skip, and previous controls
- 📋 Dynamic playlist management
- ➕ Add and remove songs from playlist
- 🎨 Modern, responsive UI with gradient backgrounds
- 📱 Mobile-friendly design
- 🔄 Real-time status updates

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python Application.py
```

### Step 3: Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## How to Use

1. **Play Music**: Click the "▶ Play" button to start playing
2. **Pause Music**: Click the "⏸ Pause" button to pause
3. **Stop Music**: Click the "⏹ Stop" button to stop
4. **Skip Song**: Click the "⏭ Next" button to go to the next song
5. **Previous Song**: Click the "⏮ Previous" button to go to the previous song
6. **Add Song**: Type a song name in the input field and click "Add Song"
7. **Remove Song**: Click the "Remove" button next to any song in the playlist

## File Structure

```
Sound Stream/
├── Application.py          # Flask web application
├── Interface.html          # Main HTML template
└── README.md               # This file

## API Endpoints

The application provides the following API endpoints:

- `GET /api/status` - Get current player status
- `POST /api/play` - Start playing music
- `POST /api/pause` - Pause music
- `POST /api/stop` - Stop music
- `POST /api/skip` - Skip to next song
- `POST /api/previous` - Go to previous song
- `POST /api/add_song` - Add song to playlist
- `POST /api/remove_song` - Remove song from playlist

## Sample Playlist

The application starts with a sample playlist including:
- Bohemian Rhapsody - Queen
- Hotel California - Eagles
- Stairway to Heaven - Led Zeppelin
- Imagine - John Lennon
- Hey Jude - The Beatles

## Troubleshooting

1. **Port already in use**: If port 5000 is busy, the application will show an error. You can modify the port in `Application.py`.

2. **Dependencies not found**: Make sure you've installed the requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. **Browser compatibility**: The application works best with modern browsers (Chrome, Firefox, Safari, Edge).


## Development

To modify the application:

- **Backend Logic**: Edit `Application.py`
- **HTML Structure**: Edit `Interface.html`

## Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python Application.py

# Access in browser
# Open: http://localhost:5000
```

## Features in Detail

### 🎵 Music Controls
- **Play**: Starts playing the current song or first song in playlist
- **Pause**: Pauses the currently playing song
- **Stop**: Stops playback and resets to no song selected
- **Skip**: Moves to the next song in the playlist
- **Previous**: Moves to the previous song in the playlist

### 📋 Playlist Management
- **Add Songs**: Type song names and add them to your playlist
- **Remove Songs**: Click the remove button to delete songs
- **Current Song Highlighting**: The currently playing song is highlighted
- **Real-time Updates**: Playlist updates automatically

###  User Interface
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern Styling**: Beautiful gradients and animations
- **Status Indicators**: Clear visual feedback for player state
- **Smooth Animations**: Hover effects and transitions

## License

This project is open source and available under the MIT License. 