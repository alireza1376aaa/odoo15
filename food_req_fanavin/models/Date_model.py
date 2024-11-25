# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from datetime import timedelta
from . import Food
from odoo.exceptions import AccessError, MissingError, ValidationError, UserError

class Week(models.Model):
    _name = 'food_req_fanavin.week'
    _description = 'food_req_fanavin.weeks'
    _rec_name = 'start_date'
    start_date = fields.Date(string=_("Start Date"),default=fields.Datetime.now,copy=False,
                             help=_('This amount of date should be selected only on Saturday and it is not possible to set our date before today'))
    end_date = fields.Date(string=_("End Date") ,compute="_date_end")

    @api.depends('start_date')
    def _date_end(self):
        for record in self:
            day = record.start_date.strftime('%A')
            obj= self.env['food_req_fanavin.week'].search([('start_date','=', record.start_date)])
            if record.start_date >= fields.Date.today() and day =='Saturday' and len(obj.ids)<=0: 
                record.end_date =  record.start_date + timedelta(days=7)
            else:
                record.end_date = None
                # raise ValidationError(_("This date has already been used or its day is not Saturday"))
            
class Day(models.Model):
    _name = 'food_req_fanavin.day'
    _description = 'food_req_fanavin.day'
    _rec_name = 'day'
    week_id = fields.Many2one("food_req_fanavin.week", string=_("Week"))
    day = fields.Date(string=_("Day"),required=True,copy=False)
    food_id = fields.Many2many('food_req_fanavin.food',string=_("Food Select"),required=True,copy=False)
    
    @api.onchange("day")
    def _change_date(self):
        for record in self:
            if record.week_id:
                List_date=[]
                next_date = record.week_id.start_date
                for i in range(0,7):
                    List_date.append(next_date)
                    next_date = next_date+timedelta(days=1)
                    obj= self.env['food_req_fanavin.day'].search([('day','=', record.day)])
                if record.day >= List_date[0] and record.day <= List_date[6] and len(obj.ids)<=0 and record.day >= fields.Date.today():
                    pass
                else:
                    raise ValidationError(_("Either this day is not in this week or the desired day is already filled"))
            else:
                record.day=None

    @api.constrains("food_id")
    def _change_food(self):
            food_box = []
            for re in self.food_id:
                food_box.append(re.type_food)
            if len(food_box)>2:
                raise ValidationError(_('Count of food bigger than 2 '))
            
            if food_box[0] == food_box[1]:
                raise ValidationError(_('Your Food cant type same'))
