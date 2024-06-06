# main.py
import customtkinter as ctk
from api import send_file_to_api
from ui import FileWatcherUI
from watcher import FileWatcher


def start_watching(directory_path):
    file_watcher = FileWatcher(directory_path, on_new_file_detected)
    import threading

    watcher_thread = threading.Thread(target=file_watcher.run)
    watcher_thread.daemon = True
    watcher_thread.start()
    app.start_button.configure(state=ctk.DISABLED)


def on_new_file_detected(file_path):
    app.add_file_button(file_path)


def on_button_click(file_path, button_frame):
    try:
        response = send_file_to_api(file_path)
        if response.status_code == 201:
            app.show_message("Success", f"File {file_path} sent successfully!")
            print(response.status_code)
            __import__("pprint").pprint(response.content)
            app.remove_file_button(button_frame)
        else:
            app.show_message("Error", f"Failed to send file {file_path}.")
    except Exception as e:
        app.show_message("Exception", e.__str__())


if __name__ == "__main__":
    root = ctk.CTk()
    app = FileWatcherUI(root, on_button_click, start_watching)
    root.mainloop()
