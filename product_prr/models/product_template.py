# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.AbstractModel):
    _inherit = 'product.template'

    mold_qty = fields.Float(
        size=20,
        string='Quantity per mold',
    )
    injection_qty = fields.Float(
        size=20,
        string='Amount per injection'
    )
    welding_documents =fields.One2many(
        comodel_name='product.welding.specification.document',
        inverse_name='product_template_id',
        string='Welding documents files',
    )
    drawing_files = fields.One2many(
        comodel_name='product.issues',
        inverse_name='product_template_id',
        string='Drawing files',
    )
    alloy_id = fields.Many2one(
        'product.alloy',
        string='Alloy',
    )
    # @api.model
    # def get_prr_values(self):
    #     product_values = []
    #     for product in self:
    #         product_values.append({
    #             'name': product.name,
    #             'sequence': product.sequence,
    #             'type': product.type,
    #             'description': product.description,
    #             'image_field_name': product.image_1920,
    #             # 'currency_id': product.currency_id,
    #             # 'cost_currency_id': product.cost_currency_id,
    #         })
    #     return self.env.ref('product_prr.product_prr_report').report_action(self, data=product_values)
    #     # return {
    #     #     "report_data": product_values,
    #     # }
