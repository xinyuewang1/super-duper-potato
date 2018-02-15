#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `systeminfo_cookiecutter` package."""


import unittest
from click.testing import CliRunner

from systeminfo_cookiecutter import systeminfo_cookiecutter
from systeminfo_cookiecutter import cli


class TestSysteminfo_cookiecutter(unittest.TestCase):
    """Tests for `systeminfo_cookiecutter` package."""

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
        assert 'systeminfo_cookiecutter.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
