# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError


class AccountAgedPayable(models.Model):
    _inherit = "account.aged.payable"
    _description = 'account.aged.payable'

    tax_tag_ids = fields.Many2many(
        string="Etiquetas",
        related="account_id.tag_ids"
    )