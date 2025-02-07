{
    'name': 'library.book',
    'version': '1.0',
    'summary': 'Manage Details of library books',
    'description': 'A module to manage library books',
    'author': 'codetrade',
    'website': 'https://codetrade.io',
    'category': 'library',
    'depends': ['base'],
    'data': [
        'data/library_data.xml',
        'security/ir.model.access.csv',
        'security/library_groups.xml',
        'views/library_book_views.xml',
    ],

    'installable': True,
    'application': True,
    'license':'LGPL-3',
}