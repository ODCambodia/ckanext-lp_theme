from flask import Blueprint


lp_theme = Blueprint(
    "lp_theme", __name__)


def page():
    return "Hello, lp_theme!"


lp_theme.add_url_rule(
    "/lp_theme/page", view_func=page)


def get_blueprints():
    return [lp_theme]
