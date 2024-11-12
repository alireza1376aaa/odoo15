/** @odoo-module **/

import { qweb as QWeb } from 'web.core';
// import session  from 'web.session';
import SystrayMenu from 'web.SystrayMenu';
import Widget from 'web.Widget';
const { Component } = owl;

var SpeechMenu = Widget.extend({
    name: 'famousWord',
    template:'speech.of.famous',
    events: {
        'click .mainbox': '_getActivityData',
        'click .nexttext': '_next_text',

    },
    start: function () {
        var rpc = require('web.rpc');
    },
    _getActivityData: function () {
        var self = this;        
        self._rpc({
            model: 'famous__words.speech',
            method: 'send_speech_text',
            args: [],
            kwargs: {},
        }).then(function (data) {
            const bozorgan_text = document.getElementById('bozorgan_text');
            const auter_text = document.getElementById('auter_text');
            bozorgan_text.style.direction = 'rtl';
            bozorgan_text.textContent = data.text;      
            auter_text.textContent = data.author;  
        });
    },
    _next_text: function(event){
        var self = this;
        event.stopPropagation();
        self._getActivityData();
    }
    

});

SystrayMenu.Items.push(SpeechMenu);

export default SpeechMenu;
