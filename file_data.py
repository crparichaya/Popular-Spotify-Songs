# model
import pandas as pd


class FileData:
    def __init__(self, file_path='Popular_Spotify_Songs.csv'):
        self.data = pd.read_csv(file_path)
