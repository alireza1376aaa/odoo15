# -*- coding: utf-8 -*-
{
    'name': "Food_req_fanavin",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,
    
    'application': 'true',
    'sequence': -100,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Food Request',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views_day.xml',
        'views/views_food.xml',
        'views/views_request.xml',
        'views/views_week.xml',
        'views/views.xml',
        # 'views/templates.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
    'web.assets_backend': [
        'food_req_fanavin/static/src/js/custom.js',
        'food_req_fanavin/static/src/css/style.css',

    ],
    'web.assets_qweb': [
        'food_req_fanavin/static/src/xml/custom.xml',

    ],
    },
}

