# -*- coding: utf-8 -*-
# Author : Hanif Nashrullah
# Date : 04-01-2019

from odoo import models, fields, api

class employeeGolongan(models.Model):
    _inherit = 'hr.employee'
    golongan = fields.Char(string='Golongan', size=32)
    darah = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O')
    ],string='Golongan Darah')

    status_p = fields.Selection([
        ('tetap', 'Tetap'),
        ('pensiun', 'Pensiun'),
        ('phk', 'PHK')
    ],string='Status Pegawai')

    gaji_p = fields.Integer(string='Gaji Pokok')

    email = fields.Char('Email')
    phone = fields.Char('No. Telp')

    tgl_masuk = fields.Date(string='Tanggal Masuk')
    tgl_pensi = fields.Date(string='Tanggal Pensiun')
    tgl_angkat = fields.Date(string='Tanggal Pengangkatan')
    jabatan_a = fields.Char('Jabatan awal masuk')
    gol_a = fields.Char('Golongan awal masuk')
    gol_b = fields.Char('Golongan saat ini')
    agama = fields.Char('Agama')
    nokk = fields.Char('No KK')
    anakke = fields.Integer('Anak Ke')
    suku = fields.Char('Suku Bangsa')
    tinggi = fields.Integer('Tinggi Badan')
    berat = fields.Integer('Berat Badan')
    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100