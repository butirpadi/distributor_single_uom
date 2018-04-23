# -*- coding: utf-8 -*-
from odoo import http

# class DistributorSingleUom(http.Controller):
#     @http.route('/distributor_single_uom/distributor_single_uom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/distributor_single_uom/distributor_single_uom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('distributor_single_uom.listing', {
#             'root': '/distributor_single_uom/distributor_single_uom',
#             'objects': http.request.env['distributor_single_uom.distributor_single_uom'].search([]),
#         })

#     @http.route('/distributor_single_uom/distributor_single_uom/objects/<model("distributor_single_uom.distributor_single_uom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('distributor_single_uom.object', {
#             'object': obj
#         })