# -*- coding: utf-8 -*-
import collections
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class XYZ(models.Model):
    _name = 'x.y.z'
    _description = 'XYZ'

    name = fields.Char()
    approval_level_ids = fields.One2many('approval.level', 'xyz_id', string='approval levels', ondelete='cascade')

    @api.constrains('approval_level_ids')
    def _check_approvals_sequence(self):
        for rec in self:
            if rec.approval_level_ids:
                sequences = rec.approval_level_ids.mapped('sequence')
                for item, count in collections.Counter(sequences).items():
                    print(item)
                    if count > 1:
                        raise ValidationError(
                            _('there are duplicated approvers sequences please check your list sequence'))
