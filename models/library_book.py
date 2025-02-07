from odoo import models, fields, api
from odoo.exceptions import ValidationError



_logger = logging.getLogger(__name__)

class LibraryBook(models.Model):
    """Library Book Module to manage book information."""
    _name = "library.book"
    _description = "Library Book Management"

    name  = fields.Char(string="Book Title", required=True)
    author = fields.Char(string="Author", required=True)
    isbn = fields.Char(string="ISBN", required=True, help="isbn is the unqiue number for the book")
    publication_date = fields.Date(string="Publication Date")
    category = fields.Selection(
        [('fiction', 'Fiction'), ('non_fiction', 'Non-fiction'), ('sci_fi', 'Science Fiction'), ('biography', 'Biography')],
        string="Category"
    )
    description = fields.Text(string="Description")
    available_copies = fields.Integer(string="Available Copies", default=0)
    book_id = fields.Many2one('book.domain', 'book_domain')

    def write(self, vals):
        """ write method to ensure available copies are non-negative."""
        if 'available_copies' in vals and vals['available_copies'] < 0:
            raise ValidationError("Available copies cannot be negative.")
        return super(LibraryBook, self).write(vals)

    def create(self, vals):
        """Override create method to ensure unique ISBN during book creation."""
        if "isbn" in vals:
            existing_book = self.env['library.book'].search([("isbn", "=", vals["isbn"])])
            if existing_book:
                raise ValidationError("A book with this ISBN already exists.")
        return super(LibraryBook, self).create(vals)
