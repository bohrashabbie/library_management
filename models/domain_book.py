from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BookDomain(models.Model):
    _name = "book.domain"
    _description = "This is the class to store the domain of the books"

    book_domain = fields.Selection(
        [('fiction', 'Fiction'), ('non_fiction', 'Non-fiction'), ('sci_fi', 'Science Fiction'), ('biography', 'Biography')],
        string="Category"
    )
    