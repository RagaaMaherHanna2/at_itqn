# -*- coding: utf-8 -*-

from odoo import models, fields


class ABC(models.Model):
    _name = 'a.b.c'
    _description = 'ABC'

    name = fields.Char()
    xyz_id = fields.Many2one('x.y.z', string='XYZ', required=True)
    t_f = fields.Text(string='Type Here', required=True)
    state = fields.Selection(string="Status", selection=[
        ('draft', 'Draft'),
        ('in_Progress', 'In Progress'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ])
    approval_level_ids = fields.One2many(compute='get_approval_level_ids', string='approval levels')

