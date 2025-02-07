from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestLibraryBook(TransactionCase):

    def setUp(self):
        super(TestLibraryBook, self).setUp()
        self.library_book = self.env['library.book'].create({
            'name': 'Test Book',
            'author': 'Test Author',
            'isbn': '1234567890',
            'publication_date': '2023-01-01',
            'category': 'fiction',
            'description': 'A test book description',
            'available_copies': 5,
        })

    def test_unique_isbn(self):
        with self.assertRaises(ValidationError):
            self.env['library.book'].create({
                'name': 'Duplicate ISBN Book',
                'author': 'Another Author',
                'isbn': '1234567890',
            })

    def test_non_negative_available_copies(self):
        with self.assertRaises(ValidationError):
            self.library_book.write({'available_copies': -1})

    def test_successful_update(self):
        self.library_book.write({'available_copies': 3})
        self.assertEqual(self.library_book.available_copies, 3)
