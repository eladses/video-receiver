import cv2
import numpy as np

class VideoManager:
    def __init__(self):
        pass
    def __del__(self):
        cv2.destroyAllWindows()

    def load_frame(self,frame_data):
        frame_array = np.frombuffer(frame_data, dtype=np.uint8)
        self.frame = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)

    def draw_rectangles(self,positions):
        for (x, y, w, h) in positions:
            cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    def show_video(self):
        cv2.imshow("Stream", self.frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            return 1
        else: 
            return 0
