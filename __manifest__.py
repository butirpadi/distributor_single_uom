# -*- coding: utf-8 -*-
{
    'name': "Aplikasi Distributor Single UOM",

    'summary': """
        Aplikasi Distributor dengan Single UOM
        """,

    'description': """
        Aplikasi Distributor dengan Single UOM
        <br/>Purchase
        <br/>Sale
        <br/>Inventory
        <br/>Account
    """,

    'author': "Tepat Guna Karya",
    'website': "http://www.tepatguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sale',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/group_invisible_menu.xml',
        'views/menu.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}