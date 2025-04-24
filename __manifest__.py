{
    'name': 'Gestion des Dossiers Clients',
    'version': '1.0',
    'summary': 'Gestion centralisée des dossiers clients',
    'description': """
        Module pour gérer les dossiers clients avec suivi des états,
        disciplines et documents associés.
    """,
    'author': 'Somasic',
    'category': 'Sales',
    'depends': ['base'],
    "data": [
        "security/ir.model.access.csv",
        "views/somasic_dossier_views.xml",
        "views/somasic_dossier_menus.xml",
        "reports/somasic_dossier_report.xml"
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    }