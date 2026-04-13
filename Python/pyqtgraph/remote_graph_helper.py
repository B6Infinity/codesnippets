import pyqtgraph as pg
import time
from multiprocessing import Process, Queue, Event
import queue # For the Empty exception

class GraphHelper:
    def __init__(self, data_queue):
        self.queue = data_queue
        self.process = None

    def update_plot(self):
        # 1. Pull all available data from the queue to stay in sync
        while True:
            try:
                val = self.queue.get_nowait()
                current_elapsed = time.time() - self.start_time
                
                self.x_data.append(current_elapsed)
                self.y_data.append(val)
            except queue.Empty:
                break # No more data to process for this frame

        # 2. Keep only the last 100 points
        if len(self.x_data) > 100:
            self.x_data = self.x_data[-100:]
            self.y_data = self.y_data[-100:]
            
        # 3. Update the line
        if self.x_data:
            self.curve.setData(self.x_data, self.y_data)

    def run_task(self):
        # Initialize GUI in the child process
        self.app = pg.mkQApp("Data Stream")
        self.win = pg.plot(title="Real-time Counter Plot")
        self.win.setBackground('w')
        self.win.setLabel('bottom', 'Time (s)')
        self.win.setLabel('left', 'Value of i')
        
        self.x_data = []
        self.y_data = []
        self.curve = self.win.plot(pen=pg.mkPen('b', width=2))
        self.start_time = time.time()

        # Timer to check the queue every 30ms
        timer = pg.QtCore.QTimer()
        timer.timeout.connect(self.update_plot)
        timer.start(30) 

        self.app.exec()

    def start_process(self):
        self.process = Process(target=self.run_task)
        self.process.daemon = True # Closes if main process exits
        self.process.start()

if __name__ == '__main__':
    # Initialize the communication channel
    data_stream = Queue()
    
    g = GraphHelper(data_stream)
    g.start_process()

    i = 0
    while i < 1000:
        print(f"Sending: {i}")
        # Send 'i' to the graph process
        data_stream.put(i)
        
        i += 1
        time.sleep(0.01) # Simulating work/delay

    print("Main loop finished. Keeping window open for 3 seconds...")
    time.sleep(3)
