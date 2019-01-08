# Copyright (C) 2018 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployeeHealthConditionSeverity(models.Model):
    _name = 'hr.employee.health.condition.periode'
    _description = 'Periode/Tahun'

    name = fields.Char(
        string='Periode',
        required=True,
        translate=True
    )
