import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import FormatStrFormatter
from file_data import FileData

df = FileData()


class SpotifyView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Spotify Songs")
        self.init_components()

    def init_components(self):
        notebook_frame = ttk.Frame(self.root)
        notebook_frame.pack(fill=tk.BOTH, expand=True)

        # Add a Canvas widget
        canvas = tk.Canvas(notebook_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a Frame to the Canvas
        self.pages = ttk.Notebook(canvas)
        canvas.create_window((0, 0), window=self.pages, anchor='nw')

        style = ttk.Style()
        style.theme_use('default')
        style.configure('Black.TNotebook', background='black')

        # Add pages
        home_page = ttk.Frame(self.pages, style='Black.TNotebook')
        self.home_page(home_page)

        descriptive_page = ttk.Frame(self.pages, style='Black.TNotebook')
        self.descriptive_page(descriptive_page)

        distribution_page = ttk.Frame(self.pages, style='Black.TNotebook')
        self.distribution_page(distribution_page)

        other_page = ttk.Frame(self.pages, style='Black.TNotebook')
        self.other_graph_page(other_page)

        data_exploration_page = ttk.Frame(self.pages, style='Black.TNotebook')
        self.data_exploration_page(data_exploration_page)

        self.pages.add(home_page, text="Home Page")
        self.pages.add(descriptive_page, text="Descriptive Graph")
        self.pages.add(distribution_page, text="Distribution Graph")
        self.pages.add(other_page, text="Other Graphs")
        self.pages.add(data_exploration_page, text="Data Exploration")
        self.pages.pack(fill=tk.BOTH, expand=1)

    def home_page(self, pages):
        home_frame = ttk.Frame(pages)
        home_frame.pack(fill='both', expand=True)

        # Adjusted row and column configurations
        home_frame.grid_columnconfigure(0, weight=1)
        home_frame.grid_columnconfigure(1, weight=1)
        home_frame.grid_rowconfigure(0, weight=1)
        home_frame.grid_rowconfigure(1, weight=1)
        home_frame.grid_rowconfigure(2, weight=1)
        home_frame.grid_rowconfigure(3, weight=1)
        home_frame.grid_rowconfigure(4, weight=1)
        home_frame.grid_rowconfigure(5, weight=1)
        home_frame.grid_rowconfigure(6, weight=1)
        home_frame.grid_rowconfigure(7, weight=1)

        style = ttk.Style()
        style.configure("Black.TFrame", background="black")

        home_frame.config(style="Black.TFrame")
        bg_label = tk.Label(home_frame, background='black')
        bg_label.grid(row=0, column=0, columnspan=2, sticky='nsew')

        # Load the image
        img_path = 'Spotify_Logo.png'
        img = PhotoImage(file=img_path)

        # Create a label to display the image
        img_label = tk.Label(home_frame, image=img, bg='black')
        img_label.image = img
        img_label.pack_propagate(False)

        # Position the image
        img_label.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        text_label = ttk.Label(home_frame, text="Welcome to Popular Spotify Songs!", background='black',
                               foreground='white',
                               font=('Arial', 14))
        text_label.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        text_label_2 = ttk.Label(home_frame, text="Click to Explore the Data", background='black',
                                 foreground='white',
                                 font=('Arial', 14))
        text_label_2.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

        text_label_3 = ttk.Label(home_frame,
                                 text="Click to see Data Storytelling",
                                 background='black', foreground='white', font=('Arial', 16))
        text_label_3.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky='nsew')

        # Navigate to descriptive graph page button
        descriptive_button = tk.Button(home_frame, text="Descriptive Graph",
                                       command=lambda: self.show_page("Descriptive Graph"),
                                       width=20, height=2)
        descriptive_button.grid(row=5, column=0, padx=10, pady=10, sticky='nsew')

        # Navigate to distribution graph page button
        distribution_button = tk.Button(home_frame, text="Distribution Graph",
                                        command=lambda: self.show_page("Distribution Graph"),
                                        width=20, height=2)
        distribution_button.grid(row=6, column=0, padx=10, pady=10, sticky='nsew')

        # Navigate to other graphs page button
        other_graphs_button = tk.Button(home_frame, text="Other Graphs",
                                        command=lambda: self.show_page("Other Graphs"),
                                        width=20, height=2)
        other_graphs_button.grid(row=7, column=0, padx=10, pady=10, sticky='nsew')

        # Navigate to data exploration page button
        data_exploration_button = tk.Button(home_frame, text="Data Exploration",
                                            command=lambda: self.show_page("Data Exploration"),
                                            width=20, height=2)
        data_exploration_button.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

        # Exit button
        exit_button = tk.Button(home_frame, text="Exit", command=quit, width=3, height=1)
        exit_button.grid(row=8, column=2, padx=10, pady=10, sticky='nsew')

    def show_page(self, page_name):
        # switch pages
        if page_name == "Descriptive Graph":
            # Index of the descriptive_page tab
            self.pages.select(1)
        elif page_name == "Distribution Graph":
            # Index of the distribution_page tab
            self.pages.select(2)
        elif page_name == "Other Graphs":
            # Index of the other_page tab
            self.pages.select(3)
        elif page_name == "Data Exploration":
            # Index of the data_exploration_page tab
            self.pages.select(4)

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
                self.plot_high_danceability_playlist_counts_line()

        # Bind the selection event
        self.graph_type_combobox.bind("<<ComboboxSelected>>", on_select)

    def plot_high_danceability_bar(self):
        high_danceability_threshold = 70

        # Filter the DataFrame to get high danceability songs
        high_danceability_songs = df.data[df.data['danceability_%'] >= high_danceability_threshold]

        # Calculate the counts
        high_danceability_count = high_danceability_songs.shape[0]
        total_songs = df.data.shape[0]

        # Clear previous graph
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        # Plot new graph
        fig, ax = plt.subplots(figsize=(6, 4), facecolor='white')  # Adjust the size
        ax.bar(['Total Songs', 'High Danceability Songs'], [total_songs, high_danceability_count],
               color=['lightblue', 'salmon'])
        ax.set_title('Percentage of High Danceability Songs')
        ax.set_ylabel('Number of Songs')
        plt.tight_layout()

        # matplotlib figure into Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def plot_high_danceability_playlist_counts_line(self):
        # Filter DataFrame for high danceability songs released between 2013 and 2023
        filtered_df = df.data[
            (df.data['released_year'] >= 2013) & (df.data['released_year'] <= 2023) & (df.data['danceability_%'] > 0.7)]

        # Group by released year and sum the songs included in Spotify playlists
        playlist_counts = filtered_df.groupby('released_year')['in_spotify_playlists'].sum()

        # Clear previous graph
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        # Plot new graph
        fig, ax = plt.subplots(figsize=(8, 4), facecolor='white')  # Adjust the size
        ax.plot(playlist_counts.index, playlist_counts.values, marker='o', linestyle='-')
        ax.set_title('Number of High Danceability Songs Released and Included in Spotify Playlists (2013-2023)')
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

    def data_exploration_page(self, pages):
        frame = ttk.Frame(pages)
        frame.pack(fill='both', expand=True)

        bg_label = tk.Label(frame, background='black')
        bg_label.place(relwidth=1, relheight=1)

        # Get numerical columns excluding 'released_year'
        numerical_columns = df.data.select_dtypes(include=['int64', 'float64']).columns.tolist()
        numerical_columns.remove('released_year')  # Remove 'released_year'

        # Create labels and comboboxes for selecting features, graph type, and year range
        ttk.Label(frame, text="Select Feature:", background='black', foreground='white').grid(row=0, column=0, padx=10,
                                                                                              pady=5)

        self.feature_combobox = ttk.Combobox(frame, values=numerical_columns, state="readonly")
        self.feature_combobox.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Select Graph Type:", background='black', foreground='white').grid(row=1, column=0,
                                                                                                 padx=10, pady=5)
        self.graph_combobox = ttk.Combobox(frame, values=["Bar Graph", "Line Graph", "Scatter Plot"],
                                           state="readonly")
        self.graph_combobox.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Select Start Year:", background='black', foreground='white').grid(row=2, column=0,
                                                                                                 padx=10, pady=5)
        start_year = ttk.Combobox(frame, values=list(range(2000, 2025)), state="readonly")
        start_year.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Select End Year:", background='black', foreground='white').grid(row=3, column=0,
                                                                                               padx=10, pady=5)
        end_year = ttk.Combobox(frame, values=list(range(2000, 2025)), state="readonly")
        end_year.grid(row=3, column=1, padx=10, pady=5)

        # Button to generate graph
        generate_button = tk.Button(frame, text="Generate",
                                    command=lambda: self.generate_graph(start_year.get(), end_year.get()))
        generate_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Clear Graph button
        clear_button = tk.Button(frame, text="Clear", command=self.clear_graph)
        clear_button.grid(row=4, column=1, columnspan=2, pady=5)

        # Frame to display the generated graph
        self.graph_frame_2 = ttk.Frame(frame)
        self.graph_frame_2.grid(row=1, column=2, columnspan=2, padx=10, pady=5, sticky='nsew')

        # Function to validate selected years
        def validate_years():
            if start_year.get() and end_year.get():
                start = int(start_year.get())
                end = int(end_year.get())
                if end < start:
                    # End year must be later than start year
                    messagebox.showerror("Error", "End year must be later than start year.")
                    return False
            return True

        # Update generate_button command to include validation
        generate_button.config(
            command=lambda: self.generate_graph(start_year.get(), end_year.get()) if validate_years() else None)

    def generate_graph(self, start_year, end_year):
        selected_feature = self.feature_combobox.get()
        selected_graph_type = self.graph_combobox.get()

        if selected_feature and selected_graph_type and start_year and end_year:
            if selected_graph_type == "Bar Graph":
                self.plot_bar_graph(selected_feature, int(start_year), int(end_year))
            elif selected_graph_type == "Line Graph":
                self.plot_line_graph(selected_feature, int(start_year), int(end_year))
            elif selected_graph_type == "Scatter Plot":
                self.plot_scatter_plot(selected_feature, int(start_year), int(end_year))

    def clear_graph(self):
        # Destroy all widgets inside the graph frame
        for widget in self.graph_frame_2.winfo_children():
            widget.destroy()

    def plot_bar_graph(self, feature, start_year, end_year):
        # Clear previous graph
        for widget in self.graph_frame_2.winfo_children():
            widget.destroy()

        # Filter data based on selected year range
        filtered_data = df.data[
            (df.data['released_year'] >= start_year) & (df.data['released_year'] <= end_year)]

        # Aggregate the data by the selected feature and calculate the mean of 'energy%'
        aggregated_data = filtered_data.groupby(feature)['energy_%'].mean()

        # Plot new graph comparing the with "energy%"
        fig, ax = plt.subplots(figsize=(6, 4))
        aggregated_data.plot(kind='bar', ax=ax)
        ax.set_title(f'Bar Graph of {feature} Compared to Energy% (from {start_year} to {end_year})')
        ax.set_xlabel(feature)
        ax.set_ylabel('Mean Energy %')
        ax.grid(True)

        # matplotlib figure into Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame_2)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def plot_line_graph(self, feature, start_year, end_year):
        # Clear previous graph
        for widget in self.graph_frame_2.winfo_children():
            widget.destroy()

        # Filter data based on selected year range
        filtered_data = df.data[
            (df.data['released_year'] >= start_year) & (df.data['released_year'] <= end_year)].copy()

        # Convert 'released_year' to integers using .loc
        filtered_data.loc[:, 'released_year'] = filtered_data['released_year'].astype(int)

        # Plot new graph
        fig, ax = plt.subplots(figsize=(6, 4))  # Adjust the size
        line_plot = filtered_data.groupby('released_year')[feature].mean().plot(marker='o', linestyle='-', ax=ax)
        ax.set_title(f'Line Graph of {feature} Over Years ( from {start_year} to {end_year})')
        ax.set_xlabel('Year')
        ax.set_ylabel(feature)
        ax.grid(True)

        # Convert x-axis tick labels to integers
        ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))

        # matplotlib figure into Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame_2)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def plot_scatter_plot(self, feature, start_year, end_year):
        # Clear previous graph
        for widget in self.graph_frame_2.winfo_children():
            widget.destroy()

        # Filter data based on selected year range
        filtered_data = df.data[
            (df.data['released_year'] >= start_year) & (df.data['released_year'] <= end_year)]

        # Plot new graph
        fig, ax = plt.subplots(figsize=(6, 4))  # Adjusted size
        ax.scatter(filtered_data['danceability_%'], filtered_data[feature], alpha=0.5)
        ax.set_title(f'Scatter Plot of {feature} vs. Danceability% (from {start_year} to {end_year})')
        ax.set_xlabel('Danceability %')
        ax.set_ylabel(feature)
        ax.grid(True)

        # Set transparent background color
        fig.patch.set_facecolor('none')

        # Adjust layout to remove empty space
        plt.tight_layout(pad=0)

        # matplotlib figure into Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame_2)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)



