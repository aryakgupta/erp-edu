# -*- coding: utf-8 -*-
# Part of ERP. See LICENSE file for full copyright and licensing details.

{
    'name': 'Cancel Journal Entries',
    'version': '1.1',
    'category': 'Accounting',
    'description': """
Allows canceling accounting entries.
====================================

This module adds 'Allow Canceling Entries' field on form view of account journal.
If set to true it allows user to cancel entries & invoices.
    """,
    'website': 'https://www.erp.com/page/accounting',
    'depends' : ['account'],
    'data': ['account_cancel_view.xml' ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
