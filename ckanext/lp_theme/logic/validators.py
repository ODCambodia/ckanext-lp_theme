import ckan.plugins.toolkit as tk


def lp_theme_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "lp_theme_required": lp_theme_required,
    }
