
from odoo import fields, models


class HrEmployeeOrganisation(models.Model):
    _name = 'hr.employee.organisation'
    _description = 'HR Employee Organisation'

    employee_id = fields.Many2one(
        string='Employee',
        comodel_name='hr.employee',
    )
    Nama = fields.Char(
        string='Nama',
        required=True,
    )
    Periode = fields.Char(
        string='Periode',
        required=True,
    )
    Sebagai = fields.Char(
        string='Sebagai',
        required=True,
    )