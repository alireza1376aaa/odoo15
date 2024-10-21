# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class attachments_size(models.Model):
#     _name = 'attachments_size.attachments_size'
#     _description = 'attachments_size.attachments_size'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
