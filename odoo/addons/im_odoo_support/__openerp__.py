{
    'name' : 'ERP Live Support',
    'version': '1.0',
    'summary': 'Chat with the ERP collaborators',
    'category': 'Website',
    'complexity': 'medium',
    'website': 'https://www.erp.com/',
    'description':
        """
ERP Live Support
=================

Ask your functional question directly to the ERP Operators with the livechat support.

        """,
    'data': [
        "views/im_odoo_support.xml"
    ],
    'depends' : ["web", "mail"],
    'qweb': [
        'static/src/xml/im_odoo_support.xml'
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}
