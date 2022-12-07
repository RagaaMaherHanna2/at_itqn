# -*- coding: utf-8 -*-

from odoo import models, fields, api


class XYZ(models.Model):
    _name = 'x.y.z'
    _description = 'XYZ'

    name = fields.Char()
    approval_level_ids = fields.One2many('approval.level', 'xyz_id', string='approval levels')
