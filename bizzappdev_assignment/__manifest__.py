# -*- coding: utf-8 -*-
{
    'name': 'BizzAppDev Assignment (Jasmin Hirani)',
    'version': '18.0.1.0.0',
    'summary': 'Technical Assignment for BizzAppDev Odoo Developer role.',
    'description': """
        Technical Assignment Module for BizzAppDev Systems Pvt. Ltd.
        Developed by: Jasmin Hirani

        Features:
        - Partner search/display includes Ref field. (Points 4, 5)
        - Copies Sale Order tags to Delivery Orders. (Point 6)
        - Allows searching on tags in Delivery Orders. (Point 7)
        - Conditional visibility for tags in Delivery Orders. (Point 8)
        - Prevents changing confirmed MO quantity if linked to SO. (Point 9)
        - Splits POs generated from procurements by Product Category. (Point 10)
        - Automated email to salesperson on DO delivery. (Point 11)
        - Enforces unique Product Category names. (Point 12)
        - Adds a 'Copy to Clipboard' widget for Char fields. (Point 13)
        - Changes default SO filter to 'Confirmed/Done'. (Point 14)
    """,
    'author': 'Jasmin Hirani',
    'category': 'Customizations',
    'depends': [
        'base',
        'sale_management',
        'stock',
        'mrp',
        'purchase_stock',
        'crm',
        'mail',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
        'views/sale_order_views.xml',
        'static/src/xml/copy_to_clipboard_widget_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'bizzappdev_assignment/static/src/js/copy_to_clipboard_widget.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
