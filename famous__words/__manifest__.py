# -*- coding: utf-8 -*-
{
    'name': "Famous_Words",

    'summary': """
       این ماژول برای این طراحی شده که هنگام کار چند ثانیه ای به تفکر در باب جملات مهم انسان های مشهور بپردازید""",

    'description': """
        در این ماژول جملات و سخنان اندیشمندان و بزرگان جهان (نویسندگان، اشخاص سیاسی و هنرمندان) را در مورد کتاب، مطالعه و کتاب خوانی آماده کرده ایم.
    """,
    
    'application': 'true',
    'author': "Alireza Qomi",
    # 'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Widget',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'assets': {

        'web.assets_qweb': [
            'famous__words/static/src/xml/speech.xml',

    	],

        'web.assets_backend': [
            'famous__words/static/src/js/speech.js',

        ],

    }

}
