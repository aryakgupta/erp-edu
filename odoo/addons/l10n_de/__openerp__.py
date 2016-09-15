# -*- coding: utf-8 -*-
# Part of ERP. See LICENSE file for full copyright and licensing details.


{
    'name': 'Deutschland - Accounting',
    'version': '1.0',
    'author': 'openbig.org',
    'website': 'http://www.openbig.org',
    'category': 'Localization',
    'description': """
Dieses  Modul beinhaltet einen deutschen Kontenrahmen basierend auf dem SKR03.
==============================================================================

German accounting chart and localization.
    """,
    'depends': ['account', 'base_iban', 'base_vat'],
    'demo': [],
    'data': [
        'account_account_types.xml',
        'account_account_tags.xml',
        'menuitem.xml',
    ],
    'installable': True,
}
