import time
import tkinter as tk

class Timer:
    def __init__(self, root):
        # Create the root window
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x200")
        self.root.configure(bg="gray")

        # Create the time label
        self.running = False
        self.start_time = 0
        self.end_time = 0
        self.rap_time = 0
        self.split_time = 0

        # Create the buttons
        self.start_button = tk.Button(self.root, text="Start", command=self.start, bg="green", fg="white")
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop, bg="red", fg="white")
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset, bg="blue", fg="white")
        self.lap_button = tk.Button(self.root, text="Lap", command=self.lap, bg="yellow", fg="white")
        self.split_button = tk.Button(self.root, text="Split", command=self.split, bg="purple", fg="white")

    def create_buttons(self, frame, text, command, color):
        button = tk.Button(frame, text=text, command=command, bg=color, fg="white")
        button.pack(side=tk.LEFT)
        return button
    
    def update_time(self):
        if self.running:
            elapsed_time = self.end_time + (time.now() - self.start_time).total_seconds()
        else:
            elapsed_time = self.end_time
        
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        self.time_label.config(text=time_str)
        self.root.after(100, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False
            self.end_time += (time.now() - self.start_time).total_seconds()
        return self.get_time()

    def get_time(self):
        return self.end_time - self.start_time

    def reset(self):
        self.running = False
        self.start_time = 0
        self.end_time = 0
        self.update_time()

    def lap(self):
        if self.rap_time == 0:
            current_time = time.time()
            time_diff = current_time - self.start_time
            self.rap_time = current_time
        else:
            current_time = time.time()
            time_diff = current_time - self.rap_time
            self.rap_time = current_time
        return time_diff
    
    def split(self):
        self.split_time = time.time()
        return self.split_time - self.start_time
    
root = tk.Tk()
app = Timer(root)
root.mainloop()
