# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions

import logging
log = logging.getLogger(__name__)

class TodoWizard(models.TransientModel):
    _name = 'todo.wizard'
    _desctiption = 'Todo Wizard per assegnazioni massive'

    todo_ids = fields.Many2many('todo.task', string='Tasks')
    new_deadline_date = fields.Date(string='Nuova deadline')
    new_user_id = fields.Many2one('res.users', string='Nuovo Responsabile')

    @api.multi
    def do_mass_update(self):
        self.ensure_one()

        if not self.new_user_id:
            raise exceptions.ValidationError("E' necessario specificare un utente")
        
        log.debug("Mass update on todos %s" % self.todo_ids.ids)

        vals = {}

        if self.new_deadline_date:
            vals['deadline_date'] = self.new_deadline_date
        
        vals['user_id'] = self.new_user_id.id

        self.todo_ids.write(vals)

    @api.multi
    def do_count_todos(self):
        count = self.env['todo.task'].search_count([('is_done', '=', False)])
        raise exceptions.Warning("Ci sono %d todo ancora aperti" % count)


    @api.multi
    def _reopen_wizard(self):
        self.ensure_one()

        # restituiamo un dizionario rappresentate l'action che riaprira' questo wizard
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name, # questo modello
            'res_id': self.id, # l'id del wizard corrente
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new'
        }

    @api.multi
    def do_select_all(self):
        self.ensure_one()

        open_todos = self.env['todo.task'].search([
            ('is_done', '=', False)
        ])

        self.todo_ids = open_todos

        return self._reopen_wizard()
