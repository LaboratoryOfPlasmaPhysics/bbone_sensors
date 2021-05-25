import os, io
import socket
import time
import pickle
import struct
from typing import List
from .. import Metric


class GraphiteRemote:
    def __init__(self, carbon_server, carbon_server_port):
        self.carbon_server = carbon_server
        self.carbon_server_port = carbon_server_port

    def send_metrics(self, metrics: List[Metric]):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.carbon_server, self.carbon_server_port))
            payload = pickle.dumps([
                ('/'.join(metric.path) + '/' + metric.name, (int(metric.time), metric.value))
                for metric in metrics], protocol=2)
            header = struct.pack("!L", len(payload))
            message = header + payload
            try:
                sock.sendall(message)
            except OSError:
                print("Can't send data to graphite")
