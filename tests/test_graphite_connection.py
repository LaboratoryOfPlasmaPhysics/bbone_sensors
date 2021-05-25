import unittest
from bbone_sensors.remote_db.graphite import GraphiteRemote
from bbone_sensors import Metric
from bbone_sensors.config import graphite_hostname,graphite_pickle_port
import time


class TestGraphiteConnection(unittest.TestCase):
    def setUp(self) -> None:
        self.graphite = GraphiteRemote(carbon_server=graphite_hostname.get(), carbon_server_port=int(graphite_pickle_port.get()))

    def tearDown(self) -> None:
        pass

    def test_send_one(self):
        self.graphite.send_metrics([Metric(['Tests','bbone_sensors'], "simple", 1., time.time())])

    def test_send_many(self):
        metrics = [
            Metric(['Tests', 'bbone_sensors'], "many", i, time.time()-10*i)
            for i in range(500)
        ]
        self.graphite.send_metrics(metrics)
