{
    'name': 'Dossier',
    'version': '1.0',
    'summary': 'Gestion des dossiers clients',
    'author': 'Abdou Ndour Ndiaye',
    'category': 'Gestion',
    'depends': ['base', 'contacts', 'mail', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/dossier_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
