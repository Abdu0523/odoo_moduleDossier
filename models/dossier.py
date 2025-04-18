from odoo import models, fields

class Dossier(models.Model):
    _name = 'somasic.dossier'
    _description = 'Dossier Client'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Désignation", required=True)
    partner_id = fields.Many2one('res.partner', string="Client")
    interlocuteur_id = fields.Many2one('res.partner', string="Interlocuteur")
    date_ouverture = fields.Date(string="Date d’ouverture")
    disciplines = fields.Char(string="Disciplines")
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('in_progress', 'En cours'),
        ('done', 'Clôturé'),
    ], string="État", default='draft', tracking=True)
    attachment_ids = fields.Many2many('ir.attachment', string="Pièces jointes")
