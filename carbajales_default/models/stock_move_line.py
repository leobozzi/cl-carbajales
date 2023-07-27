# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"
    _description = 'stock.move.line'

    def write(self, vals):
        for rec in self:
            sale_order_line_ids = self.env['sale.order.line'].search([('order_id.name','=',rec.origin)])
            for sale_order_line_id in sale_order_line_ids:
                if rec.picking_id.route_id:
                    sale_order_line_id.name = sale_order_line_id.product_id.name + " (%s)"%(rec.picking_id.route_id.name)
           