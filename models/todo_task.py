# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoTask(models.Model):
    _inherit = 'todo.task'

