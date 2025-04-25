from odoo import models, fields, api
from datetime import datetime

class Dossier(models.Model):
    _name = 'somasic.dossier'
    _description = 'Dossier Client'
    _order = 'num_dossier desc'

#### vue List et Forms
    num_dossier = fields.Char(string='N. dossier', readonly=True, copy=False)
    partner_id = fields.Many2one('res.partner', string='Client', required=True)
    interlocuteur_id = fields.Many2one(
        'res.partner', 
        string='Interlocuteur',
        domain="[('parent_id','=',partner_id)]"
    )
    designation = fields.Char(string='Designation', required=True)
    date_ouverture = fields.Date(string='Date ouverture', default=fields.Date.today, required=True)
    disciplines = fields.Char(string='Disciplines')
    state = fields.Selection([
        ('open', 'Ouvert'),
        ('in_progress', 'En cours'),
        ('done', 'Terminé'),
        ('cancelled', 'Annulé')
    ], string='Status', default='open')

#### Proposition commerciale : lignes dynamiques
    pc_line_ids = fields.One2many (
       'somasic.pc_line',
       'dossier_id',
       string = " "
    )
#### Checkbox (onglet Proposition Commercial)
    pc_email = fields.Boolean(string='Email')
    pc_deposed = fields.Boolean(string = 'Déposée')
    pc_sended = fields.Boolean(string = 'Dèja envoyée')

    
### Géneration automatique du numero de dossier 
    @api.model_create_multi
    def create(self, vals_list):
     for vals in vals_list:
        if not vals.get('num_dossier'):
            current_year = datetime.now().year
            year_suffix = str(current_year)[-2:]
            last_dossier = self.search(
                [('num_dossier', 'ilike', f'D{year_suffix}-%')],
                order='num_dossier desc',
                limit=1
            )
            if last_dossier and last_dossier.num_dossier:
                last_number = int(last_dossier.num_dossier.split('-')[-1])
            else:
                last_number = 0

            new_number = str(last_number + 1).zfill(3)
            vals['num_dossier'] = f'D{year_suffix}-{new_number}'

        return super().create(vals_list)
