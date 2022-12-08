# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ApprovalLevelStatus(models.Model):
    _name = 'approval.level.status'
    _inherits = {'approval.level': 'level_id'}
    _description = 'Approval Level'
    _order = 'sequence, id'

    level_id = fields.Many2one('approval.level', required=True, ondelete='restrict', auto_join=True,
                               string='Related approval level')
    abc_id = fields.Many2one('a.b.c', string='ABC')
    state = fields.Selection(string="Status", selection=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='pending')
