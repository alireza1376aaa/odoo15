// /** @odoo-module **/

import ActivityMenu from '@mail/js/systray/systray_activity_menu';
import Dialog from 'web.Dialog';
import core from 'web.core';
var QWeb = core.qweb;
import { useService } from "@web/core/utils/hooks";

ActivityMenu.include({
    start: function () {
        this._super.apply(this, arguments);
        var rpc = require('web.rpc');
        this.checkLoginAndShowPopup();
    },

    myCustomFunction: function() {
        console.log("دکمه سفارشی کلیک شد");

    },

    checkLoginAndShowPopup: function () {
        var isUserLoggedIn = sessionStorage.getItem('user_logged_in');
        if (isUserLoggedIn === null || true) { 
            this._PopUp_Activity();
            sessionStorage.setItem('user_logged_in', 'true');
        }
    },

    _PopUp_Activity: function () {
        var self = this; 

        self._rpc({
            model: 'mail.activity',
            method: 'POP_UP',
            args: [],
            kwargs: {},
        }).then(function (res) {
            var content = QWeb.render('PopUpTemplate', {  
                message: res,
            });
            var dialog = new Dialog(self, {
                title: 'نمایش فعالیت ها',
                size: 'larg',
                $content: $(content),
                buttons: [
                    { text: 'بستن', close: true }
                ]
            });
        
            
            dialog.open();

        });
    },


    /**
     * @override
     */
    _getViewsList(model) {
        return [[false, 'list'], [false, 'form'],[false, 'kanban']];
    },

});

