# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ABC(models.Model):
    _name = 'a.b.c'
    _description = 'ABC'

    name = fields.Char()
    xyz_id = fields.Many2one('x.y.z', string='XYZ', required=True)
    t_f = fields.Text(string='Type Here', required=True)
    state = fields.Selection(string="Status", selection=[
        ('draft', 'Draft'),
        ('progress', 'In Progress'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='draft')
    approval_level_status_ids = fields.One2many('approval.level.status', 'abc_id',
                                                string='approval levels Status', ondelete='cascade')
    next_approver_id = fields.Many2one('res.users', string='Next Approver', readonly=True, store=True)

    check_approve_visibility = fields.Boolean(compute='compute_check_approve_visibility')

    @api.onchange('xyz_id')
    def onchange_xyz_id(self):
        for rec in self:
            if rec.xyz_id:
                rec.approval_level_status_ids.unlink() if rec.approval_level_status_ids else None
                approval_levels = rec.xyz_id.approval_level_ids
                for line in approval_levels:
                    self.env['approval.level.status'].create({
                        'abc_id': rec.id,
                        'level_id': line.id,
                        'state': 'pending'
                    })
                rec.next_approver_id = approval_levels[0].user_id

    @api.depends('state', 'next_approver_id')
    def compute_check_approve_visibility(self):
        for rec in self:
            if rec.state in ['draft', 'progress'] and self.env.user == rec.next_approver_id:
                rec.check_approve_visibility = True
            else:
                rec.check_approve_visibility = False
    def _get_pending_approvals(self):
        return self.approval_level_status_ids.filtered(lambda x: x.state == 'pending').sorted(
            key=lambda x: x.sequence)

    def action_approve(self):
        pending_approvals = self._get_pending_approvals()
        if len(pending_approvals) > 1:
            self.state = 'progress'
            pending_approvals[0].state = 'approved'
            self.next_approver_id = pending_approvals[1].user_id
        if len(pending_approvals) == 1:
            self.state = 'approved'
            pending_approvals.state = 'approved'
            self.next_approver_id = False

    def action_reject(self):
        pending_approvals = self._get_pending_approvals()
        if len(pending_approvals) > 1:
            self.state = 'progress'
            pending_approvals[0].state = 'rejected'
            self.next_approver_id = pending_approvals[1].user_id
        if len(pending_approvals) == 1:
            self.state = 'rejected'
            pending_approvals.state = 'rejected'
            self.next_approver_id = False
