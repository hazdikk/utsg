# Copyright (C) 2018 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployeePromotionLevel(models.Model):
    _name = 'hr.employee.promotion.level'
    _description = 'HR Employee Level'

    name = fields.Char(
        string='Level',
        required=True,
        translate=True
    )
