# -*- coding: utf-8 -*-
{
    'name': "pop_up_odoo15",

    'summary': """
        برنامه ای برای نمایش فعالیت هایی که در غیاب شما چیده شده
        """,

    'description': """
        
    """,

    'author': "Alireza",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Widget',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'views/search.xml',

    ],
    'assets': {
        'web.assets_qweb': [
        	  'pop_up_odoo15/static/src/xml/pop_up.xml',
    	],
        'web.assets_backend': [
            'pop_up_odoo15/static/src/js/pop_up.js',

        ],
    
    },
}
