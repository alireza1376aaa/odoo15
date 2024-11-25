# -*- coding: utf-8 -*-

from odoo import models, fields, api
import markupsafe
import re

class salam(models.Model):
    _inherit = 'mail.activity'
    
    is_see = fields.Boolean(string='is_read',default=False)
    
    def salam(self):
        x=self.res_id
        y=self.res_model
        z=self.env.ref('food_req_fanavin.model_name_view_form').id
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_id': x,
            'res_model': y,
            'target': 'current',
            'view_id': z,
            'name': "Hello World",
        }
        
    @api.model
    def POP_UP(self):
    
        activities = self.env['mail.activity'].search([('is_see','=',False),('user_id','=',self.env.user.id)])or None
        activity_data = 0
        if activities is not None:
            activity_data = []
            pattern = r'<p>|<br>|</p>'

            for activity in activities:
                data = {
                    'rec_name': activity.res_name,
                    'activity_type': activity.activity_type_id.name,
                    'summary': activity.summary,
                    'date_deadline': activity.date_deadline,
                    'note': re.sub(pattern, "", activity.note),
                    'link':f'http://127.0.0.1:8017/web#id={activity.res_id}&model={activity.res_model_id.model}&view_type=form'
                }
                activity_data.append(data)
                # activity.is_see = True            
        else:
            activity_data = {'massage':'شما پیام جدیدی ندارید خیالتان راحت'} 
        
        return activity_data