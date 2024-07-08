odoo.define('custom_purchase.button_confirm', function (require) {
    "use strict";

    var FormController = require('web.FormController');

    FormController.include({
        _onButtonClicked: function (event) {
            var self = this;
            if (event.data.attrs.name === 'button_confirm') {
                event.stopPropagation();
                event.preventDefault();
                this.do_warn(
                    'Confirmation',
                    'Are you sure you want to confirm this purchase order?',
                    {
                        confirm_callback: function () {
                            self._rpc({
                                model: self.modelName,
                                method: 'button_confirm',
                                args: [[self.datarecord.id]],
                            }).then(function (result) {
                                self.reload();
                            });
                        }
                    }
                );
            } else {
                this._super(event);
            }
        }
    });
});
