from odoo import models, fields, api

class ProductCert(models.Model):
    _name = 'product.cert'
    _description = 'Product certification'

    name = fields.Char(
        string='Certification',
        size=50,
    )
    type = fields.Char(
        string='Product Type',
        size=50,
    )
    sample_size = fields.Char(
        string='Sample size',
        size=50,
    )
    scan_plan = fields.Char(
        string='Scan plan',
        size=50,
    )