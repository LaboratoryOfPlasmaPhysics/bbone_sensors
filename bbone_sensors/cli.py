"""Console script for bbone_sensors."""
import sys
import click
from .bbone_sensors import measurement_loop
from .config import graphite_hostname, graphite_pickle_port
from .remote_db.graphite import GraphiteRemote


@click.command()
def main(args=None):
    measurement_loop(
        GraphiteRemote(carbon_server=graphite_hostname.get(), carbon_server_port=int(graphite_pickle_port.get())))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
