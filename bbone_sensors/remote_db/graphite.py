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
        self.sock = socket.socket()
        self.__connected = False
        self.connect()

    def connect(self):
        try:
            self.sock.connect((self.carbon_server, self.carbon_server_port))
            self.__connected = True
        except OSError:
            self.__connected = False

    def close(self):
        self.sock.close()

    def is_connected(self):
        return self.__connected

    def send_metrics(self, metrics: List[Metric]):
        if self.__connected:
            payload = pickle.dumps([
                ('/'.join(metric.path) + '/' + metric.name, (metric.time, metric.value))
                for metric in metrics], protocol=2)
            header = struct.pack("!L", len(payload))
            message = header + payload
            try:
                self.sock.sendall(message)
            except OSError:
                self.__connected = False
