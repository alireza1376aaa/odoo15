# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from . import Date_model
type_f = [('ir',_('Rice')),('en',_('No Rice'))]

class Food(models.Model):
    _name = 'food_req_fanavin.food'
    _description = 'food_req_fanavin.food'
    _rec_name = 'name'
    
    day_ids = fields.Many2many('food_req_fanavin.day',string=_("select day"),copy=False)
    name = fields.Char(string=_("Name Food"))
    type_food = fields.Selection(selection=type_f,string=_("Select Type Food"))