# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='ckanext-lp_theme',
    version='0.0.2',
    entry_points='''
        [ckan.plugins]
        lp_theme=ckanext.lp_theme.plugin:LpThemePlugin
    ''',
    # If you are changing from the default layout of your extension, you may
    # have to change the message extractors, you can read more about babel
    # message extraction at
    # http://babel.pocoo.org/docs/messages/#extraction-method-mapping-and-configuration
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
