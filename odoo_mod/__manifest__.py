{
    'name': 'odoo_mod',
    'version': '16.0.1.0.0',
    'category': 'Tools',
    'summary': 'A tool for estimating manufacturing costs.',
    'description': '''This module helps estimate manufacturing costs by calculating raw material, 
                       tooling, and labor costs for different processes. It supports various suppliers 
                       and allows cost comparisons.''',
    'author': 'EstiSource Pvt Ltd',
    'website': 'https://www.estisource.com',
    'depends': ['base', 'sale', 'stock'],  # Module dependencies
    'data': [
        'views/costing_view.xml',  # Path to your XML view files
        'security/ir.model.access.csv',  # Access control file
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

