odoo.define('client_act.sale_cust', function (require) {
    'use strict';
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var rpc = require('web.rpc');
    var QWeb = core.qweb;
    var SaleCustom = AbstractAction.extend({
    template: 'SaleCust',
        events: {
        },
        init: function(parent, action) {
            this._super(parent, action);
        },
        start: function() {
            var self = this;
            self.load_data();
        },
        load_data: function () {
            var self = this;
                    var self = this;
                    self._rpc({
                        model: 'food_req_fanavin.food_request',
                        method: 'food_today',
                        args: [],
                    }).then(function(datas) {

                        const salamMessage1 = document.getElementById('Food_1');
                        const salamMessage2 = document.getElementById('Food_2');
                        salamMessage1.textContent = datas[0];
                        salamMessage2.textContent = datas[1];

                    })
            },
    });
    core.action_registry.add("sale_cust", SaleCustom);
    return SaleCustom;
 });