# -*- coding: utf-8 -*-
# from odoo import http


# class ConfigurableApprovalCycle(http.Controller):
#     @http.route('/configurable_approval_cycle/configurable_approval_cycle/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/configurable_approval_cycle/configurable_approval_cycle/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('configurable_approval_cycle.listing', {
#             'root': '/configurable_approval_cycle/configurable_approval_cycle',
#             'objects': http.request.env['configurable_approval_cycle.configurable_approval_cycle'].search([]),
#         })

#     @http.route('/configurable_approval_cycle/configurable_approval_cycle/objects/<model("configurable_approval_cycle.configurable_approval_cycle"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('configurable_approval_cycle.object', {
#             'object': obj
#         })
