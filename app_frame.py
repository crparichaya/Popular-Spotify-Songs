import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import seaborn as sns


class FileData:
    def __init__(self, file_path='Popular_Spotify_Songs.csv'):
        self.data = pd.read_csv(file_path)


class DescriptiveGraph:
    def __init__(self):
        pass

    def plot_danceability_and_bpm_graph(self):
        # Plot scatter plot of danceability_% and bpm
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='danceability_%', y='bpm', data=df.data, alpha=0.5)
        plt.suptitle('Scatter Plot of Danceability Percentage vs. BPM')
        plt.xlabel('Danceability Percentage')
        plt.ylabel('BPM')
        plt.grid(True)
        plt.show()


class DistributionGraph:
    def __init__(self):
        pass

    def plot_energy_percentage_graph(self):
        # Plotting the distribution graph
        plt.figure(figsize=(10, 6))
        plt.hist(df.data['energy_%'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
        plt.suptitle('Distribution of Energy Percentage')
        plt.xlabel('Energy Percentage')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()


class OtherGraphs:
    pass
    # Create the bar graph
    # plt.figure(figsize=(8, 6))
    # plt.bar(["High Danceability", "Other"], [percentage_high_danceability, 100 - percentage_high_danceability],
    #         color=['green', 'gray'])
    # plt.title("Percentage of High Danceability Songs")
    # plt.ylabel("Percentage")
    # plt.ylim(0, 100)
    # plt.show()


class SpotifyUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Spotify Songs")
        self.init_components()
        self.geometry('960x540')

    def init_components(self):
        pages = ttk.Notebook(self)
        pages.pack(pady=10, padx=10, expand=True)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Black.TNotebook', background='black')

        # Add pages here
        home_page = ttk.Frame(pages, style='Black.TNotebook')
        self.home_page(home_page)

        data_story_page = ttk.Frame(pages, style='Black.TNotebook')
        descriptive_page = ttk.Frame(pages, style='Black.TNotebook')
        distribution_page = ttk.Frame(pages, style='Black.TNotebook')
        other_page = ttk.Frame(pages, style='Black.TNotebook')
        self.other_graph_page(other_page)

        pages.add(home_page, text="Home Page")
        pages.add(data_story_page, text="Data Storytelling")
        pages.add(descriptive_page, text="Descriptive Graph")
        pages.add(distribution_page, text="Distribution Graph")
        pages.add(other_page, text="Other Graphs")
        pages.pack(fill=BOTH, expand=1)

    # home_page
    def home_page(self, pages):
        home_frame = ttk.Frame(pages)
        home_frame.pack(fill='both', expand=True)

        bg_label = tk.Label(home_frame, background='black')
        bg_label.place(relwidth=1, relheight=1)

        # Load the image
        img_path = 'Spotify_Logo.png'
        img = PhotoImage(file=img_path)

        # Create a label to display the image
        img_label = tk.Label(home_frame, image=img, bg='black')
        img_label.image = img
        img_label.pack_propagate(False)

        # Center the image
        img_label.place(relx=0.5, rely=0.5, anchor='center')

        # exit_button = ttk.Button(home_frame, text="Exit", command=self.destroy)
        # exit_button.pack(side='bottom', pady=20)

    def other_graph_page(self, pages):
        other_frame = ttk.Frame(pages)
        other_frame.pack(fill='both', expand=True)

        # Create a label with black background
        bg_label = tk.Label(other_frame, background='black')
        bg_label.place(relwidth=1, relheight=1)

        # Create a label for the combobox
        label = ttk.Label(other_frame, text="Choose Graph Type:", background='black', foreground='white',
                          font=('Arial', 25))
        label.pack(pady=20)

        # Create a Combobox
        graph_types = ["Bar Graph", "Line Graph"]
        graph_type_combobox = ttk.Combobox(other_frame, values=graph_types, state="readonly")
        graph_type_combobox.pack(pady=20)

        # Function to handle selection change
        def on_select(event):
            selected_graph_type = graph_type_combobox.get()
            print("Selected Graph Type:", selected_graph_type)

        # Bind the selection event
        graph_type_combobox.bind("<<ComboboxSelected>>", on_select)


if __name__ == '__main__':
    df = FileData()
    # UI = SpotifyUI()
    # UI.mainloop()
    UI = SpotifyUI()
    UI.mainloop()
