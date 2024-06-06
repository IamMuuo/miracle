import customtkinter as ctk
from tkinter import messagebox, filedialog


class FileWatcherUI:
    def __init__(self, root, api_callback, start_watching_callback):
        self.root = root
        self.api_callback = api_callback
        self.start_watching_callback = start_watching_callback
        self.root.title("Miracle Watcher")
        self.root.geometry("800x600")
        ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
        ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"
        self.path_entry_frame = ctk.CTkFrame(root)
        self.path_entry_frame.pack(pady=20)

        self.path_label = ctk.CTkLabel(
            self.path_entry_frame, text="Select Directory to Watch:"
        )
        self.path_label.pack(side=ctk.LEFT, padx=5)

        self.path_entry = ctk.CTkEntry(self.path_entry_frame, width=200)
        self.path_entry.pack(side=ctk.LEFT, padx=5)

        self.browse_button = ctk.CTkButton(
            self.path_entry_frame, text="Browse", command=self.browse_directory
        )
        self.browse_button.pack(side=ctk.LEFT, padx=5)

        self.start_button = ctk.CTkButton(
            root, text="Start Watching", command=self.start_watching
        )
        self.start_button.pack(pady=10)

        self.file_list_frame = ctk.CTkFrame(root)
        self.file_list_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

    def browse_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.path_entry.delete(0, ctk.END)
            self.path_entry.insert(0, directory_path)

    def start_watching(self):
        directory_path = self.path_entry.get()
        if directory_path:
            self.start_watching_callback(directory_path)
        else:
            messagebox.showwarning("Warning", "Please select a directory to watch.")

    def add_file_button(self, file_path):
        button_frame = ctk.CTkFrame(self.file_list_frame)
        button_frame.pack(fill=ctk.X, pady=5)
        btn = ctk.CTkButton(
            self.file_list_frame,
            text=file_path,
            command=lambda: self.api_callback(file_path, button_frame),
        )
        btn.pack(fill=ctk.X, pady=5)

    def remove_file_button(self, button_frame):
        button_frame.destroy()

    def show_message(self, title, message):
        messagebox.showinfo(title, message)
