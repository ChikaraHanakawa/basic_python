import time
import tkinter as tk

class Timer:
    def __init__(self, root):
        # Create the root window
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("400x300")
        self.root.configure(bg="gray")

        # Create the time label
        self.running = False
        self.start_time = 0
        self.end_time = 0
        self.rap_time = 0
        self.split_time = 0

        # Create the time label
        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48), fg="#fff", bg="#333")
        self.time_label.pack(pady=20)
        button_frame = tk.Frame(root, bg="gray")
        button_frame.pack()

        # Create the buttons
        self.start_button = self.create_buttons(button_frame, "Start", self.start, "green")
        self.stop_button = self.create_buttons(button_frame, "Stop", self.stop, "red")
        self.reset_button = self.create_buttons(button_frame, "Reset", self.reset, "blue")
        self.lap_button = self.create_buttons(button_frame, "Lap", self.lap, "orange")
        self.split_button = self.create_buttons(button_frame, "Split", self.split, "purple")

        # Create the lap label
        self.lap_label = tk.Label(root, text="Lap Time: 00:00:00", font=("Helvetica", 20), fg="#fff", bg="#333")
        self.lap_label.pack(pady=20)
        button_frame = tk.Frame(root, bg="gray")
        button_frame.pack()

        # Create the split label
        self.split_label = tk.Label(root, text="Split Time: 00:00:00", font=("Helvetica", 20), fg="#fff", bg="#333")
        self.split_label.pack(pady=20)
        button_frame = tk.Frame(root, bg="gray")
        button_frame.pack()

    def create_buttons(self, frame, text, command, color):
        button = tk.Button(frame, text=text, command=command, bg=color, fg="white")
        button.pack(side=tk.LEFT)
        return button
    
    def update_time(self):
        if self.running:
            elapsed_time = int(self.end_time + (time.time() - self.start_time))
        else:
            elapsed_time = self.end_time

        if self.split_time != 0:
            time_diff = self.split_time - self.start_time
            hours = int(time_diff // 3600)
            minutes = int((time_diff % 3600) // 60)
            seconds = int(time_diff % 60)
            time_str = f"Split Time: {hours:02}:{minutes:02}:{seconds:02}"
            self.split_label.config(text=time_str)
            self.split_time = 0
        
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
            self.end_time += int((time.time() - self.start_time))
            self.update_time()

    def reset(self):
        self.running = False
        self.start_time = 0
        self.end_time = 0
        self.rap_time = 0
        self.split_time = 0
        self.update_time()
        self.lap_label.config(text="Lap Time: 00:00:00")
        self.split_label.config(text="Split Time: 00:00:00")

    def lap(self):
        if self.rap_time == 0:
            current_time = time.time()
            time_diff = current_time - self.start_time
            self.rap_time = current_time
        else:
            current_time = time.time()
            time_diff = current_time - self.rap_time
            self.rap_time = current_time
        hours = int(time_diff // 3600)
        minutes = int((time_diff % 3600) // 60)
        seconds = int(time_diff % 60)
        time_str = f"Lap Time: {hours:02}:{minutes:02}:{seconds:02}"
        self.lap_label.config(text=time_str)
    
    def split(self):
        self.split_time = time.time()
    
root = tk.Tk()
app = Timer(root)
root.mainloop()
