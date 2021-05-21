#!/usr/bin/env python

"""Tests for `bbone_sensors` package."""


import unittest
from click.testing import CliRunner

from bbone_sensors import bbone_sensors
from bbone_sensors import cli


class TestBbone_sensors(unittest.TestCase):
    """Tests for `bbone_sensors` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'bbone_sensors.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
