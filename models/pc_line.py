from odoo import models, fields

class pcline(models.Model):
    _name = "somasic.pc_line"
    _description = "List sur l'onglet proposition commerciale"

    dossier_id =fields.Many2one(
        'somasic.dossier',
        string ="Dossier",
        required = True,
        ondelete = 'cascade'
    )
   #### table de reference [onglet]
    ref = fields.Char(string = "Référence")
    du_ = fields.Date(string = "Du")