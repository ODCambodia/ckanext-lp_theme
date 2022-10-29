"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.lp_theme.logic import validators


def test_lp_theme_reauired_with_valid_value():
    assert validators.lp_theme_required("value") == "value"


def test_lp_theme_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.lp_theme_required(None)
