# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = 'sale.order'
    
    general_bonus = fields.Float(
        string="Bonificación General",
    )

    @api.onchange('general_bonus')
    def onchange_general_bonus(self):
        if self.general_bonus != 0.0:
            for order_line_id in self.order_line:
                order_line_id.discount = -self.general_bonus
                
    

