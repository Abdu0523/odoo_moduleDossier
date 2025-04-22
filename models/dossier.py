from odoo import models, fields

class Dossier(models.Model):
    _name = 'somasic.dossier'
    _description = 'Dossier Client'

    name = fields.Char(string='Nom du dossier', required=True)
    partner_id = fields.Many2one('res.partner', string='Client')
    date_ouverture = fields.Date(string='Date ouverture', default=fields.Date.today)
    state = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('valide', 'Validé'),
        ('cloture', 'Clôturé')
    ], default='brouillon')