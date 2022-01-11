from odoo import models, fields, api

class ProductAlloy(models.Model):
    _name = 'product.alloy'
    _description = 'Alloy catalog'

    name = fields.Char(
        string='Alloy',
        size=50,
    )