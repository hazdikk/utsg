from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    career_ids = fields.One2many(
        string='Pengalaman Kerja',
        comodel_name='hr.employee.career',
        inverse_name='employee_id',
        groups='hr.group_hr_user',
    )
    organisation_ids = fields.One2many(
        string='Pengalaman Organisasi',
        comodel_name='hr.employee.organisation',
        inverse_name='employee_id',
        groups='hr.group_hr_user',
    )