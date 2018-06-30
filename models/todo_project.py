# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoProject(models.Model):
    _name = "todo.project"

    name = fields.Char('Name')
    todo_ids = fields.One2many('todo.task', 'project_id', string='Todos')
    todo_counter = fields.Integer(string='Totale Todo', compute='_compute_total_todos')

    @api.depends('todo_ids')
    def _compute_total_todos(self):
        for project in self:
            project.todo_counter = len(project.todo_ids)