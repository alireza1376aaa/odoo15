# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from . import Food,Date_model
from datetime import timedelta
from odoo.exceptions import ValidationError

class food_request(models.Model):
    _name = 'food_req_fanavin.food_request'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'food_req_fanavin.food_request'
    _rec_name = 'food_id'
    
    week_id = fields.Many2one('food_req_fanavin.week',string=_("Week"))
    user_id = fields.Many2one("res.users", string=_("User"),default=lambda self: self.env.user,readonly=True)
    day = fields.Date(string=_("Day"),default=fields.Date.context_today,copy=False,tracking=True)
    food_id = fields.Many2one('food_req_fanavin.food',string=_("Select Food"),
                              required=True,copy=False,tracking=True)
    alireza = fields.Char(related='food_id.name')
    
    # def _compute_food_domain(self):
    #     domain = [('day_ids.day', '=', self.day)]
    #     return domain
    
    
    @api.onchange("day")
    def _change_date(self):
        for record in self:
            if record.week_id:
                List_date=[]
                next_date = record.week_id.start_date
                for i in range(0,7):
                    List_date.append(next_date)
                    next_date = next_date+timedelta(days=1)
                    x=record.user_id.id
                    obj= self.env['food_req_fanavin.food_request'].search([('day','=', record.day),('user_id','=',record.user_id.id)])
                if record.day >= List_date[0] and record.day <= List_date[6] and len(obj.ids)<=0:
                    pass
                else:
                    raise ValidationError(_("Either this day is not in this week or the desired day is already filled"))
            else:
                record.day = None
    @api.model
    def food_today(self):
            obj= self.env['food_req_fanavin.food_request'].search([('day','=', fields.Date.today())])
            food_list = []
            for doof in obj:
                food_list.append(doof.display_name)
                
            massage = []
            for element in set(food_list):
                count = food_list.count(element)
                massage.append(f"{count} : {element}")
                
            return massage
                
            
    # def food_today(self):
    #     today_food= self.env['food_req_fanavin.food'].search([('day_ids.day','=', fields.Date.today())])
    #     for food in today_food:
    #         print(food.name)
            
    #     print('ssd')
    #     print('ssd')
    #     print('ssd')

