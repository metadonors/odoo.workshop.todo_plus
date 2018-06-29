# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoTag(models.Model):
    _name = "todo.tag"

    name = fields.Char('Name')