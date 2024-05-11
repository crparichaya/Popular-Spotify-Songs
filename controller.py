from spotify_ui import SpotifyView


class SpotifyController:
    def __init__(self):
        self.view = SpotifyView(self)

    def run(self):
        self.view.root.mainloop()
