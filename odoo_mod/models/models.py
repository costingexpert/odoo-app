from odoo import models, fields

class CostingEstimator(models.Model):
    _name = 'costing.estimator'  # Model name

    name = fields.Char(string='Costing Estimator Name', required=True)
    description = fields.Text(string='Description')
    raw_material_cost = fields.Float(string='Raw Material Cost')
    tooling_cost = fields.Float(string='Tooling Cost')
    labor_cost = fields.Float(string='Labor Cost')
    supplier_ids = fields.Many2many('res.partner', string='Suppliers')  # Many2many relationship for suppliers
    total_cost = fields.Float(string='Total Cost', compute='_compute_total_cost')

    def _compute_total_cost(self):
        for record in self:
            # Calculate the total cost by summing raw material, tooling, and labor costs
            record.total_cost = record.raw_material_cost + record.tooling_cost + record.labor_cost
