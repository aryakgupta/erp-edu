# -*- coding: utf-8 -*-
# Part of ERP. See LICENSE file for full copyright and licensing details.
{
    'name': 'Turkey - Accounting',
    'version': '1.0',
    'category': 'Localization',
    'description': """
Türkiye için Tek düzen hesap planı şablonu OpenERP Modülü.
==========================================================

Bu modül kurulduktan sonra, Muhasebe yapılandırma sihirbazı çalışır
    * Sihirbaz sizden hesap planı şablonu, planın kurulacağı şirket, banka hesap
      bilgileriniz, ilgili para birimi gibi bilgiler isteyecek.
    """,
    'author': 'Ahmet Altınışık',
    'maintainer':'https://launchpad.net/~openerp-turkey',
    'website':'https://launchpad.net/openerp-turkey',
    'depends': [
        'account',
        'base_vat',
    ],
    'data': [
        'account_tdhp_turkey.xml',
        'account_tax_template.xml',
        'account_chart_template.yml',
    ],
    'demo': [],
    'installable': True,
}
