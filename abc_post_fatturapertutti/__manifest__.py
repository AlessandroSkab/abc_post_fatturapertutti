# -*- coding: utf-8 -*-
{
    'name': "abc_post_fatturapertutti",

    'summary': """
        Modulo che permette di inviare i corrispettivi a Fatturapertutti, solamente dopo aver chiuso
        la sessione PoS corrente.""",

    'description': """
        Modulo che permette di inviare i corrispettivi a Fatturapertutti, solamente dopo aver chiuso
        la sessione PoS corrente.""",

    'author': "A.B.C. srl",
    'website': "https://www.abcstrategie.it/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale', 'pos_enterprise', 'pos_epson_printer', 'pos_hr', 'pos_loyalty', 'pos_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
