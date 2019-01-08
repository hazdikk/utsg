
from odoo import fields, models, api

from datetime import datetime
from dateutil.relativedelta import relativedelta

class HrEmployeeOrganisation(models.Model):
    _name = 'hr.employee.promotion'
    _description = 'HR Employee Promotion Mutation and Rotation'

    employee_id = fields.Many2one(
        string='Employee',
        comodel_name='hr.employee',
    )
    No_SK = fields.Char(
        string='No. SK',
        required=True,
    )
    Mulai = fields.Date(
        string='Mulai',
        required=True,
    )
    Kode_Unit = fields.Char(
        string='Kode Unit',
        required=True,
    )
    Nama_Unit = fields.Char(
        string='Nama Unit',
        required=True,
    )
    Eselon = fields.Char(
        string='Eselon',
        required=True,
    )    
    Level = fields.Many2one(
        'hr.employee.promotion.level',
        string='Level',
    )
    Kd_Atasan_Lgs = fields.Char(
        string='Kode Atasan Langsung',
        required=True,
    )
    Kd_Atasan_Tdklgs = fields.Char(
        string='Kode Atasan Langsung',
        required=True,
    )
    Kd_Posisi = fields.Char(
        string='Kode Posisi',
        required=True,
    )

    @api.depends('Mulai')
    def _compute_age(self):
        for record in self:
            start = relativedelta(datetime.now(), record.Mulai)