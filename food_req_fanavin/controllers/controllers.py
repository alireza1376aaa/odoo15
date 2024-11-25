# -*- coding: utf-8 -*-
# from odoo import http


# class FoodReqFanavin(http.Controller):
#     @http.route('/food_req_fanavin/food_req_fanavin', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/food_req_fanavin/food_req_fanavin/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('food_req_fanavin.listing', {
#             'root': '/food_req_fanavin/food_req_fanavin',
#             'objects': http.request.env['food_req_fanavin.food_req_fanavin'].search([]),
#         })

#     @http.route('/food_req_fanavin/food_req_fanavin/objects/<model("food_req_fanavin.food_req_fanavin"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('food_req_fanavin.object', {
#             'object': obj
#         })

