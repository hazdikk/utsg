
from odoo import fields, models


class HrEmployeeCareer(models.Model):
    _name = 'hr.employee.career'
    _description = 'HR Employee Career'

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
    Gaji = fields.Integer(
        string='Gaji',
        required=True,
    )
    AlasanKeluar = fields.Char(
        string='Alasan Keluar',
        required=True,
    )