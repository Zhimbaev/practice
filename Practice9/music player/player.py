import pygame

class MusicPlayer:
    def __init__(self):
        self.tracks = [
            "/Users/zamirzimbaev/Desktop/practice/Practice9/music player/music/elciasnascimento-eterna-cancao-wav-12569.wav",
            "/Users/zamirzimbaev/Desktop/practice/Practice9/music player/music/memphis-trap-memphis-trap-wav-349366.wav"
        ]
        self.current = 0

    def play(self):
        pygame.mixer.music.load(self.tracks[self.current])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.current += 1
        if self.current >= len(self.tracks):
            self.current = 0
        self.play()

    def prev(self):
        self.current -= 1
        if self.current < 0:
            self.current = len(self.tracks) - 1
        self.play()