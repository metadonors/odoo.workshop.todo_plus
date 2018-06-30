# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoTask(models.Model):
    _inherit = 'todo.task'

    state = fields.Selection([
        ('draft', 'Bozza'),
        ('progress', 'In Corso'),
        ('completed', 'Completato'),
        ('canceled', 'Annullato')
    ], string='Stato', default='draft')

    completed_date = fields.Datetime(string='Data Completamento', states={
        'completed': [('readonly', True)],
        'canceled': [('readonly', True)]
    })

    worked_hours = fields.Float(string='Ore lavorate')
    description = fields.Html(string='Descrizione')
    internal_notes = fields.Text(string='Note interne')
    project_id = fields.Many2one('todo.project', string='Progetto')
    tag_ids = fields.Many2many('todo.tag', string='Tag')

    project_state = fields.Char(string='Stato progetto', compute='_compute_project_state')

    @api.depends('project_id')
    def _compute_project_state(self):
        for todo in self:
            todo.project_state = todo.project_id.state
