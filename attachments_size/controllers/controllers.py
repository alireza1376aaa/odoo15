# -*- coding: utf-8 -*-
# from odoo import http


# class AttachmentsSize(http.Controller):
#     @http.route('/attachments_size/attachments_size', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/attachments_size/attachments_size/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('attachments_size.listing', {
#             'root': '/attachments_size/attachments_size',
#             'objects': http.request.env['attachments_size.attachments_size'].search([]),
#         })

#     @http.route('/attachments_size/attachments_size/objects/<model("attachments_size.attachments_size"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('attachments_size.object', {
#             'object': obj
#         })
