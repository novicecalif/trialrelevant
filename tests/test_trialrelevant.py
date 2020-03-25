#!/usr/bin/env python

"""Tests for `trialrelevant` package."""


import unittest

from trialrelevant import trialrelevant


class TestTrialrelevant(unittest.TestCase):
    """Tests for `trialrelevant` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.ind_message = 'ind method'
        self.checkit_message = 'i am in checkit'

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_indmethod_something(self):
        """Test something."""
        output = trialrelevant.indmethod()
        assert(output == self.ind_message)

    def test_checkit_method(self):
        """Test something."""
        output = trialrelevant.TrialRelevant().checkit()
        assert(output == self.checkit_message)
