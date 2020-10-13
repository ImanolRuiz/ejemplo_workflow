{
    'name': 'group_validation',
    'summary': 'Creation of a group that gives the users permits to create an opportunity',
    'author': 'Imanol Ruiz, SDi Soluciones Informáticas',
    'website': 'https://sdi.es/odoo/',
    'category': 'Uncategorized',
    'version': '12.0.1.0.0',
    'depends': [
        'base',
        'crm',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/iniciativa_security.xml',
    ],
}
