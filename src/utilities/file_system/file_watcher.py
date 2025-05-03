import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"File created: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"File deleted: {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}")

    def on_moved(self, event):
        if not event.is_directory:
            print(f"File moved from {event.src_path} to {event.dest_path}")

def watch_directory(path: str, event_handler: FileSystemEventHandler = FileChangeHandler(), recursive: bool = False) -> Observer:
    """Watches a directory for file system events."""
    observer = Observer()
    observer.schedule(event_handler, path, recursive=recursive)
    observer.start()
    return observer

# Example usage:
# if __name__ == "__main__":
#     path_to_watch = "."
#     event_handler = FileChangeHandler()
#     observer = watch_directory(path_to_watch, event_handler, recursive=True)
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()