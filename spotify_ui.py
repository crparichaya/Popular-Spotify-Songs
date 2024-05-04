import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from file_data import FileData
df = FileData()


class SpotifyUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Spotify Songs")
        self.init_components()

    def init_components(self):
        self.pages = ttk.Notebook(self)
        self.pages.pack(pady=10, padx=10, expand=True)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Black.TNotebook', background='black')

        # Add pages
        home_page = ttk.Frame(self.pages, style='Black.TNotebook')
        self.home_page(home_page)

        data_story_page = ttk.Frame(self.pages, style='Black.TNotebook')

        descriptive_page = ttk.Frame(self.pages, style='Black.TNotebook')
        self.descriptive_page(descriptive_page)

        distribution_page = ttk.Frame(self.pages, style='Black.TNotebook')
        self.distribution_page(distribution_page)

        other_page = ttk.Frame(self.pages, style='Black.TNotebook')
        self.other_graph_page(other_page)

        self.pages.add(home_page, text="Home Page")
        self.pages.add(data_story_page, text="Data Storytelling")
        self.pages.add(descriptive_page, text="Descriptive Graph")
        self.pages.add(distribution_page, text="Distribution Graph")
        self.pages.add(other_page, text="Other Graphs")
        self.pages.pack(fill=BOTH, expand=1)

    def home_page(self, pages):
        home_frame = ttk.Frame(pages)
        home_frame.pack(fill='both', expand=True)

        home_frame.rowconfigure(0, weight=1)
        home_frame.rowconfigure(1, weight=1)
        home_frame.rowconfigure(2, weight=1)
        home_frame.rowconfigure(3, weight=1)
        home_frame.rowconfigure(4, weight=1)
        home_frame.columnconfigure(0, weight=1)
        home_frame.columnconfigure(1, weight=1)

        style = ttk.Style()
        style.configure("Black.TFrame", background="black")

        home_frame.config(style="Black.TFrame")
        bg_label = tk.Label(home_frame, background='black')
        bg_label.grid(row=0, column=0, sticky='nsew')

        # Load the image
        img_path = 'Spotify_Logo.png'
        img = PhotoImage(file=img_path)

        # Create a label to display the image
        img_label = tk.Label(home_frame, image=img, bg='black')
        img_label.image = img
        img_label.pack_propagate(False)

        # Position the image
        img_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        text_label = ttk.Label(home_frame, text="What is Spotify", background='black', foreground='white',
                               font=('Arial', 20))
        text_label.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        # Text below the image
        text_label_1 = ttk.Label(home_frame,
                                 text="Spotify is a digital music streaming service. It gives you instant access to "
                                      "its "
                                      "vast online library of music and podcasts, allowing you to listen to any "
                                      "content "
                                      "of your choice at any time.",
                                 background='black', foreground='white', font=('Arial', 12), wraplength=400,
                                 justify='center')
        text_label_1.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

        text_label_2 = ttk.Label(home_frame,
                                 text="Welcome to Popular Spotify Songs!",
                                 background='black', foreground='white', font=('Arial', 16))
        text_label_2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        # Navigate to data storytelling page button
        data_story_button = tk.Button(home_frame, text="Data Storytelling",
                                      command=lambda: self.show_page("Data Storytelling"),
                                      width=20, height=2)
        data_story_button.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

        # Navigate to descriptive graph page button
        descriptive_button = tk.Button(home_frame, text="Descriptive Graph",
                                       command=lambda: self.show_page("Descriptive Graph"),
                                       width=20, height=4)
        descriptive_button.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

        # Navigate to distribution graph page button
        distribution_button = tk.Button(home_frame, text="Distribution Graph",
                                        command=lambda: self.show_page("Distribution Graph"),
                                        width=20, height=2)
        distribution_button.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')

        # Navigate to other graphs page button
        other_graphs_button = tk.Button(home_frame, text="Other Graphs",
                                        command=lambda: self.show_page("Other Graphs"),
                                        width=20, height=4)
        other_graphs_button.grid(row=4, column=1, padx=10, pady=10, sticky='nsew')

    def show_page(self, page_name):
        # switch pages
        if page_name == "Descriptive Graph":
            # Index of the descriptive_page tab
            self.pages.select(2)
        elif page_name == "Distribution Graph":
            # Index of the distribution_page tab
            self.pages.select(3)
        elif page_name == "Data Storytelling":
            # Index of the data_story_page tab
            self.pages.select(1)
        elif page_name == "Other Graphs":
            # Index of the other_page tab
            self.pages.select(4)

    def data_story_telling_page(self, pages):
        data_frame = ttk.Frame(pages)
        data_frame.pack(fill='both', expand=True)

    def descriptive_page(self, pages):
        frame = ttk.Frame(pages)
        frame.pack(fill='both', expand=True)

        bg_label = tk.Label(frame, background='black')
        bg_label.place(relwidth=1, relheight=1)

        # label
        label = ttk.Label(frame, text="Click to see the Graph", background='black', foreground='white',
                          font=('Arial', 25))
        label.pack(pady=20)

        # Load the image
        img_path = 'descriptive_page.png'
        img = PhotoImage(file=img_path)

        # Create a label to display the image
        img_label = tk.Label(pages, image=img, bg='black')
        img_label.image = img
        img_label.pack_propagate(False)

        # Center the image
        img_label.place(relx=0.5, rely=0.5, anchor='center')

        # add button
        Button = tk.Button(pages, text='danceability_%, and bpm scatter plot', width=40, command=self.descriptive_graph,
                           height=3)
        Button.pack(pady=20)

    def descriptive_graph(self):
        other = tk.Toplevel()
        other.geometry("500x400")
        self.plot_descriptive_graph(other)

    def plot_descriptive_graph(self, frame):
        # distribution graph
        plot_frame = tk.Frame(frame)
        plot_frame.pack(fill='both', expand=True)

        # Create a figure and an axis
        fig, ax = plt.subplots(figsize=(10, 6))

        # scatter plot
        sns.scatterplot(x='danceability_%', y='bpm', data=df.data, alpha=0.5, ax=ax)
        ax.set_title('Scatter Plot of Danceability Percentage vs. BPM')
        ax.set_xlabel('Danceability Percentage')
        ax.set_ylabel('BPM')
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def distribution_page(self, pages):
        frame = ttk.Frame(pages)
        frame.pack(fill='both', expand=True)

        bg_label = tk.Label(frame, background='black')
        bg_label.place(relwidth=1, relheight=1)

        # label
        label = ttk.Label(frame, text="Click to see the Graph", background='black', foreground='white',
                          font=('Arial', 25))
        label.pack(pady=20)

        # Load the image
        img_path = 'distribution_pic.png'
        img = PhotoImage(file=img_path)

        # Create a label to display the image
        img_label = tk.Label(pages, image=img, bg='black')
        img_label.image = img
        img_label.pack_propagate(False)

        img_label.place(relx=0.5, rely=0.5, anchor='center')

        # add button
        Button = tk.Button(pages, text='Energy%', width=25, command=self.distribution_graph,
                           height=3)
        Button.pack(pady=20)

    def distribution_graph(self):
        other = tk.Toplevel()
        other.geometry("500x400")
        self.plot_distribution_graph(other)

    def plot_distribution_graph(self, frame):
        # distribution graph
        plot_frame = tk.Frame(frame)
        plot_frame.pack(fill='both', expand=True)

        # distribution graph
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(df.data['energy_%'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
        ax.set_title('Distribution of Energy Percentage')
        ax.set_xlabel('Energy Percentage')
        ax.set_ylabel('Frequency')
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def other_graph_page(self, pages):
        other_frame = ttk.Frame(pages)
        other_frame.pack(fill='both', expand=True)

        bg_label = tk.Label(other_frame, background='black')
        bg_label.place(relwidth=1, relheight=1)

        # Create a label for the combobox
        label = ttk.Label(other_frame, text="Choose Graph Type:", background='black', foreground='white',
                          font=('Arial', 25))
        label.pack(pady=20)

        # Create a Combobox
        graph_types = ["Bar Graph", "Line Graph"]
        self.graph_type_combobox = ttk.Combobox(other_frame, values=graph_types, state="readonly")
        self.graph_type_combobox.pack(pady=20)

        # Create a frame to hold the graph
        self.graph_frame = ttk.Frame(other_frame)
        self.graph_frame.pack(padx=100, pady=20, expand=True)

        # Function to handle selection change
        def on_select(event):
            selected_graph_type = self.graph_type_combobox.get()
            if selected_graph_type == "Bar Graph":
                self.plot_high_danceability_bar()
            elif selected_graph_type == "Line Graph":
                self.plot_playlist_counts_line()

        # Bind the selection event
        self.graph_type_combobox.bind("<<ComboboxSelected>>", on_select)

    def plot_high_danceability_bar(self):
        high_danceability_threshold = 0.8  # Define your threshold

        # Filter the DataFrame to get high danceability songs
        high_danceability_songs = df.data[df.data['danceability_%'] >= high_danceability_threshold]

        # Calculate the counts
        high_danceability_count = high_danceability_songs.shape[0]
        total_songs = df.data.shape[0]

        # Clear previous graph
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        # Plot new graph
        fig, ax = plt.subplots(figsize=(6, 4), facecolor='white')  # Adjust the size as needed
        ax.bar(['Total Songs', 'High Danceability Songs'], [total_songs, high_danceability_count],
               color=['lightblue', 'salmon'])
        ax.set_title('Percentage of High Danceability Songs')
        ax.set_ylabel('Number of Songs')
        plt.tight_layout()

        # matplotlib figure into Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def plot_playlist_counts_line(self):
        filtered_df = df.data[(df.data['released_year'] >= 2013) & (df.data['released_year'] <= 2023)]
        playlist_counts = filtered_df.groupby('released_year')['in_spotify_playlists'].sum()

        # Clear previous graph
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        # Plot new graph
        fig, ax = plt.subplots(figsize=(8, 4), facecolor='white')  # Adjust the size as needed
        ax.plot(playlist_counts.index, playlist_counts.values, marker='o', linestyle='-')
        ax.set_title('Number of Songs Released and Included in Spotify Playlists (2013-2023)')
        ax.set_xlabel('Year')
        ax.set_ylabel('Number of Songs')
        ax.grid(True)
        ax.set_xticks(range(2013, 2024))
        ax.tick_params(axis='x', rotation=45)
        plt.tight_layout()

        # matplotlib figure into Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
