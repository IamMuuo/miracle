import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class FileWatcher:
    def __init__(self, path_to_watch: str, callback) -> None:
        self.observer = Observer()
        self.path_to_watch = path_to_watch
        self.callback = callback

    def run(self):
        event_handler = Handler(self.callback)
        self.observer.schedule(
            event_handler=event_handler,
            path=self.path_to_watch,
            recursive=True,
        )
        self.observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        except Exception as e:
            raise e


class Handler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".MIR"):
            self.callback(event.src_path)
