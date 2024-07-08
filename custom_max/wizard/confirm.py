from odoo import fields, models, api


class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'

    # Define the fields you need in the wizard
    name = fields.Char(string="Name", required=True)
    property_id = fields.Many2one('real.estate.property', string='Property')
    address = fields.Char(string='Address', required=True)
    email_id = fields.Char(string='Email', required=True, translate=True)
    contacts = fields.Many2one("res.partner", string="Contacts")

    def button_confirm(self):
        # Do something here to confirm the order
        # For example, confirm the purchase order
        purchase_order_id = self.env.context.get('active_id')
        if purchase_order_id:
            purchase_order = self.env['purchase.order'].browse(purchase_order_id)
            purchase_order.button_confirm()
        return {'type': 'ir.actions.act_window_close'}


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_confirm_order_wizard(self):
        return {
            'name': 'Create Appointment',
            'type': 'ir.actions.act_window',
            'res_model': 'create.appointment.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_order_id': self.id},
        }
