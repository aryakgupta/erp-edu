# -*- coding: utf-8 -*-
# Part of ERP. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website Gengo Translator',
    'category': 'Website',
    'version': '1.0',
    'description': """
Website Gengo Translator
========================

Translate you website in one click
""",
    'depends': [
        'website',
        'base_gengo'
    ],
    'data': [
        'views/website_gengo.xml',
    ],
    'qweb': [],
    'installable': True,
}
