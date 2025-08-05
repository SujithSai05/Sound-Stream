from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional
from dataclasses import dataclass
import time

# MARK: - Music Source Protocol
class MusicSource(ABC):
    @property
    @abstractmethod
    def songs(self) -> List[str]:
        pass
    
    @abstractmethod
    def play(self, song: str) -> None:
        pass

# MARK: - Local File Source
class LocalFileSource(MusicSource):
    def __init__(self):
        self._songs = ["local_song1.mp3", "local_song2.mp3"]
    
    @property
    def songs(self) -> List[str]:
        return self._songs

    def play(self, song: str) -> None:
        print(f"Playing local file: {song}")

# MARK: - Spotify Mock Source
class SpotifySource(MusicSource):
    def __init__(self):
        self._songs = ["spotify_song1", "spotify_song2"]
    
    @property
    def songs(self) -> List[str]:
        return self._songs

    def play(self, song: str) -> None:
        print(f"Playing Spotify track: {song}")

# MARK: - Player State Enum
class PlayerState(Enum):
    PLAYING = "playing"
    PAUSED = "paused"
    STOPPED = "stopped"

# MARK: - Music Player Singleton
class MusicPlayer:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MusicPlayer, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._music_sources: List[MusicSource] = []
            self._playlist: List[str] = []
            self._current_song: Optional[str] = None
            self._state: PlayerState = PlayerState.STOPPED
            self._state_callbacks: List[callable] = []
            self._progress_callbacks: List[callable] = []
            self._initialized = True

    def add_source(self, source: MusicSource) -> None:
        self._music_sources.append(source)

    def load_playlist(self) -> None:
        self._playlist = []
        for source in self._music_sources:
            self._playlist.extend(source.songs)
        print(f"Playlist Loaded: {self._playlist}")

    def play(self) -> None:
        if not self._current_song and self._playlist:
            self._current_song = self._playlist[0]
        
        if not self._current_song:
            print("Playlist is empty")
            return
            
        self._state = PlayerState.PLAYING
        self._notify_state_change()
        self._notify_progress()
        print(f"Playing: {self._current_song}")

    def pause(self) -> None:
        if self._state == PlayerState.PLAYING:
            self._state = PlayerState.PAUSED
            self._notify_state_change()
            print(f"Paused: {self._current_song or 'None'}")

    def stop(self) -> None:
        self._state = PlayerState.STOPPED
        self._notify_state_change()
        print("Stopped")

    def skip(self) -> None:
        if not self._current_song or self._current_song not in self._playlist:
            return
            
        current_index = self._playlist.index(self._current_song)
        next_index = (current_index + 1) % len(self._playlist)
        self._current_song = self._playlist[next_index]
        self.play()

    def previous(self) -> None:
        if not self._current_song or self._current_song not in self._playlist:
            return
            
        current_index = self._playlist.index(self._current_song)
        previous_index = (current_index - 1 + len(self._playlist)) % len(self._playlist)
        self._current_song = self._playlist[previous_index]
        self.play()

    def add_song(self, song: str) -> None:
        self._playlist.append(song)

    def remove_song(self, song: str) -> None:
        self._playlist = [s for s in self._playlist if s != song]

    def reorder_songs(self, new_order: List[str]) -> None:
        self._playlist = new_order

    def on_state_change(self, callback: callable) -> None:
        self._state_callbacks.append(callback)

    def on_progress_update(self, callback: callable) -> None:
        self._progress_callbacks.append(callback)

    def _notify_state_change(self) -> None:
        for callback in self._state_callbacks:
            callback(self._state)

    def _notify_progress(self) -> None:
        for callback in self._progress_callbacks:
            callback(self._current_song, 0)

    @property
    def playlist(self) -> List[str]:
        return self._playlist.copy()

    @property
    def current_song(self) -> Optional[str]:
        return self._current_song

    @property
    def state(self) -> PlayerState:
        return self._state

# MARK: - Example Usage
def main():
    player = MusicPlayer()
    local_source = LocalFileSource()
    spotify_source = SpotifySource()

    player.add_source(local_source)
    player.add_source(spotify_source)
    player.load_playlist()

    # State change callback
    def on_state_change(state):
        print(f"Player state changed: {state}")

    # Progress update callback
    def on_progress_update(song, time):
        print(f"Progress update - Song: {song or 'None'}, Time: {time}")

    player.on_state_change(on_state_change)
    player.on_progress_update(on_progress_update)

    # Operations
    player.play()
    player.skip()
    player.pause()
    player.previous()
    player.stop()
    player.add_song("new_song.mp3")
    player.reorder_songs(["new_song.mp3", "spotify_song1", "local_song1.mp3"])

if __name__ == "__main__":
    main()