import time

class Timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.rap_time = 0
        self.split_time = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        return self.get_time()

    def get_time(self):
        return self.end_time - self.start_time

    def reset(self):
        self.start_time = 0
        self.end_time = 0

    def rap(self):
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