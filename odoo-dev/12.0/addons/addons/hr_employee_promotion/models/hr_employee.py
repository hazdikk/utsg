from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    history_ids = fields.One2many(
        string='Riwayat Mutasi, Rotasi dan Promosi',
        comodel_name='hr.employee.promotion',
        inverse_name='employee_id',
        groups='hr.group_hr_user',
    )