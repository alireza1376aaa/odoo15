# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests


class larg_speak(models.Model):
    _name='famous__words.speech'
    _description = 'famous__words.speech.make_text'
    
    @api.model
    def send_speech_text(self):
        value={}
        try:
            text = requests.get('https://one-api.ir/sokhan/?token=589323:67305561442cc&action=random').json()
            value = text['result']
        except:
            value = {'text':'اینترنت خود را برسی کنید','author':''}
        return value