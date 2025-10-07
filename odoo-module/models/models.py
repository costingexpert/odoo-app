# models/models.py
from odoo import models, fields

class CostEstimation(models.Model):
    _name = 'cost.estimation'  # Technical name for the model
    _description = 'Cost Estimation for Manufacturing'

    name = fields.Char(string='Estimation Name', required=True)
    product_id = fields.Many2one('product.product', string='Product')  # Link to Odoo product
    quantity = fields.Float(string='Quantity', default=1.0)  # Quantity of product
    unit_cost = fields.Float(string='Unit Cost', required=True)  # Cost per unit of product
    total_cost = fields.Float(string='Total Cost', compute='_compute_total_cost', store=True)  # Total cost (computed)

    # Example: Calculate total cost based on unit cost and quantity
    @api.depends('unit_cost', 'quantity')
    def _compute_total_cost(self):
        for record in self:
            record.total_cost = record.unit_cost * record.quantity
