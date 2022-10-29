"""Tests for helpers.py."""

import ckanext.lp_theme.helpers as helpers


def test_lp_theme_hello():
    assert helpers.lp_theme_hello() == "Hello, lp_theme!"
