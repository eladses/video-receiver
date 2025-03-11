import socket
import cv2, struct
import numpy as np
import pickle

HOST = "192.168.68.84"  # Listen on localhost
PORT = 5006         # Port to listen on

OP_FRAME=0x06
OP_WAIT=0x07

OP_CONTINUE=0x08
OP_END=0x09
OP_ERROR=0x00

class CommunicationManager:
    def __init__(self):
        self.ip = HOST
        self.port = PORT
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("finding server")
        self.sock.connect((HOST, PORT))
        print("found server")

    def __del__(self):
        self.sock.close()

    def listen(self):
        msg_op=b''
        while len(msg_op)==0:
            msg_op = self.sock.recv(2)
        msg_op = int.from_bytes(msg_op, byteorder='big', signed=False)
        if msg_op==OP_FRAME:
            return 1,self._listen_for_frame()
        elif msg_op==OP_END:
            return 0,
        elif msg_op==OP_ERROR:
            return -1,
        elif msg_op==OP_WAIT:
            pass
            return 0,
        else: 
            return 0,

    def send_end(self):
        self.sock.sendall(struct.pack("!H", OP_END))

    def send_continue(self):
        self.sock.sendall(struct.pack("!H", OP_CONTINUE))


    def _listen_for_frame(self):
        img_size_data = self.sock.recv(4)
        img_size = struct.unpack("!I", img_size_data)[0]

        img_data = b""
        while len(img_data) < img_size:
            img_data += self.sock.recv(min(img_size - len(img_data),4096))
        return img_data

if __name__=="__main__":
    message = "Hello, UDP Server!"
    cm = CommunicationManager()
    while True:
        positions = cm.listen()
        print(positions)
