# Copyright (C) 2018 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployeeHealthConditionType(models.Model):
    _name = 'hr.employee.health.condition.type'
    _description = 'Jenis Penyakit'

    name = fields.Char(
        string='Jenis',
        required=True,
        translate=True
    )
