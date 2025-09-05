# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    manager_approval = fields.Boolean(default=False)

    def action_confirm(self):
        for order in self:
            if order.amount_total > 10000 and not order.manager_approval:
                raise UserError("manager approval true olmalı eğer sipariş 10bin tl üzeriyse")
        return super(SaleOrder, self).action_confirm()





