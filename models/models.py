# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fadoo_license(models.Model):
    _name = "fadoo_license.license"
    _description = "fadoo_license"

    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()
