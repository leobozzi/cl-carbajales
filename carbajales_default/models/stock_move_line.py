# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _

from datetime import datetime

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"
    _description = 'stock.move.line'

    def write(self, vals):
        for rec in self:
            sale_order_line_ids = rec.env['sale.order.line'].search([
                ('order_id.name','=',rec.origin),
                ('product_id','!=',False)
                ])
            for sale_order_line_id in sale_order_line_ids:
                sale_order_line_id.name = sale_order_line_id.product_id.name + " (%s)" %(sale_order_line_id.order_id.lr_number) + " (%s)"%(rec.picking_id.route_id.name) + " [%s]"%(datetime.strftime(rec.picking_id.scheduled_date, '%d/%m/%Y'))

        res = super(StockMoveLine, self).write(vals)
        return res