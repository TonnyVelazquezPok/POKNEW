# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductIssues(models.Model):
    _name = 'product.issues'
    _description = 'Container of the UIDs to work'

    product_template_id = fields.Many2one(
        comodel_name='product.template',
        string='Product'
    )
    drawing_type = fields.Char(
        size=50,
        string='Drawing type',
    )
    drawing_owner = fields.Many2one(
        comodel_name='res.partner',
        string='Drawing owner',
    )
    drawing_number = fields.Char(
        size=50,
        string='Drawing number',
    )
    drawing_review = fields.Char(
        size=50,
        string='Drawing review',
    )
    drawing_date_revision = fields.Datetime(
        size=50,
        string='Drawing date revision',
    )
    drawing_file = fields.Many2many(
        'ir.attachment',
        string="Attachment",
        help='You can attach the copy of your Letter'
    )

    # category_code = fields.Char(
    #     string='Alloy',
    #     size=50,
    # )
    # mold_qty = fields.Float(
    #     size=20,
    #     string='Quantity per mold',
    # )
    # injection_qty = fields.Float(
    #     size=20,
    #     string='Amount per injection'
    # )