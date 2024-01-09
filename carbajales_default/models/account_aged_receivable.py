# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError


class AccountAgedReceivable(models.Model):
    _inherit = "account.aged.receivable"
    _description = 'account.aged.receivable'

    tax_tag_ids = fields.Many2many(
        string="Etiquetas",
        related="account_id.tag_ids"
    )