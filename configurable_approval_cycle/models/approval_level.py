# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ApprovalLevel(models.Model):
    _name = 'approval.level'
    _description = 'Approval Level'
    _order = 'sequence, id'

    xyz_id = fields.Many2one('x.y.z', string='XYZ', required=True)
    user_id = fields.Many2one('res.users', string='Approver', required=True, domain=lambda self: [
        ('groups_id', 'in', self.env.ref('configurable_approval_cycle.b_b_b').id)])
    sequence = fields.Integer(string='Sequence', default=1)
