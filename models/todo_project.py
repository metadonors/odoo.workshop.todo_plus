# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoProject(models.Model):
    _name = "todo.project"

    name = fields.Char('Name')
    state = fields.Selection([
        ('open', 'In corso'),
        ('closed', 'Chiuso'),
    ], string='Stato', default='open')

    todo_ids = fields.One2many('todo.task', 'project_id', string='Todos')

