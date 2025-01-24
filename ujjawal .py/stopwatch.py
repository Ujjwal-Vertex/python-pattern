import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.is_running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.time_display = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.time_display.pack()

        self.start_button = tk.Button(root, text="Start", font=("Helvetica", 14), command=self.start)
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(root, text="Stop", font=("Helvetica", 14), command=self.stop)
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(root, text="Reset", font=("Helvetica", 14), command=self.reset)
        self.reset_button.pack(side="left", padx=10)

    def update_time(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            time_str = self.format_time(self.elapsed_time)
            self.time_display.config(text=time_str)
            self.root.after(100, self.update_time)

    def format_time(self, elapsed):
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed * 100) % 100)
        return f"{minutes:02}:{seconds:02}:{milliseconds:02}"

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_time()
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")

    def reset(self):
        self.is_running = False
        self.elapsed_time = 0
        self.time_display.config(text="00:00:00")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
