# -*- coding: utf-8 -*-
# Copyright 2018 Akretion France
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    active = fields.Boolean(default=True)
