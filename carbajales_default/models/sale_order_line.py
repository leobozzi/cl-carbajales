# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    _description = 'sale.order.line'
    
    commission = fields.Float(
        string="Bonif.",
        default=0.0,
        readonly=True,
        compute='_compute_commission'
    )

    @api.depends('discount','price_unit')
    def _compute_commission(self):
        for rec in self:
            rec.commission = abs(rec.product_uom_qty*(rec.price_unit * rec.discount)/100)
    
    @api.model
    def write(self, vals):
        for rec in self:
            if rec.order_id.general_bonus != 0.0:
                vals['discount'] = -rec.order_id.general_bonus
        res = super(SaleOrderLine, self).write(vals)
        return res