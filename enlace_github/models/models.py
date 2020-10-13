# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EnlaceGithub(models.Model):
    _inherit = 'res.users'

    enlace = fields.Char("EnlaceGit")
