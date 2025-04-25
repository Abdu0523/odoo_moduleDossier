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
    onglet_ids = fields.One2many (
       'somasic.onglet',
       'dossier_id',
       string = " "
    )
#### Checkbox (onglet)
    og_email = fields.Boolean(string='Email')
    og_deposed = fields.Boolean(string = 'Déposée')
    og_sended = fields.Boolean(string = 'Dèja envoyée')
    og_tel = fields.Boolean(string = 'Téléphone')
    og_prest = fields.Boolean(string = 'Prestation demandée')
    og_date_inter = fields.Boolean(string = 'Date d'+"'"+'intervention')
    og_del_inter = fields.Boolean(string = 'Délai d'+"'"+'intervention')
    og_price = fields.Boolean(string = 'Prix')
    og_mode_pay = fields.Boolean(string = 'Mode de payement')
    og_norm_appl = fields.Boolean(string = 'Normes applicables')
    og_niv_inc = fields.Boolean(string = 'Niveau d'+"'"+'incertitude')
    og_proch_date_etalon = fields.Boolean(string = 'Prochaine date d'+"'"+'étalonnage')
    og_cap_labo = fields.Boolean(string = 'Capabilité du laboratoire')
    og_visa_client = fields.Boolean(string = 'Visa client')

    
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
