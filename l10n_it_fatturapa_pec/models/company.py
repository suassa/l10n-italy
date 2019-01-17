# -*- coding: utf-8 -*-

from openerp import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'
    e_invoice_user_id = fields.Many2one(
        "res.users", "E-invoice creator",
        help="This user will be used at supplier e-invoice creation.",
        default=lambda self: self.env.user
    )


class AccountConfigSettings(models.TransientModel):
    _inherit = 'account.config.settings'
    e_invoice_user_id = fields.Many2one(
        related='company_id.e_invoice_user_id',
        string="Supplier e-invoice creator",
        help="This user will be used at supplier e-invoice creation. "
             "This setting is relevant in multi-company environments"
        )
