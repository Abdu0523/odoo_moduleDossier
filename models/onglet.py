from odoo import models, fields

class onglet(models.Model):
    _name = "somasic.onglet"
    _description = "Données onglets"

    dossier_id =fields.Many2one(
        'somasic.dossier',
        string ="Dossier",
        required = True,
        ondelete = 'cascade'
    )
   #### table de reference [onglet]
    ref = fields.Char(string = "Référence")
    du_ = fields.Date(string = "Du")
