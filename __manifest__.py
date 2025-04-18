{
    'name': 'somasic_dossier',
    'version': '1.0',
    'summary': 'Gestion des dossiers clients',
    'author': 'Abdou Ndour Ndiaye',
    'category': 'Gestion',
    'depends': ['base', 'contacts', 'mail', 'sale', 'account'],
    'data': [
        'security/dossier_security.xml',
        'security/ir.model.access.csv',
        'views/dossier_views.xml',
        'views/dossier_menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
