# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoProject(models.Model):
    _name = "todo.project"

    name = fields.Char('Name')