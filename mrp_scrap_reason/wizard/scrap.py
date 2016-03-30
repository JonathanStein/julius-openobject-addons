# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-Today Julius Network Solutions SARL <contact@julius.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import fields, models, api, _


class stock_move_scrap(models.TransientModel):
    _inherit = 'stock.move.scrap'

    @api.model
    def _scrap_reason_get(self):
        reasons = self.env['stock.move.scrap.reason'].search([])
        result = []
        for reason in reasons:
            result.append((reason.id, reason.name))
        result.append((-1, _('Other...')))
        return result

    reason = fields.Selection(_scrap_reason_get, help="Reason for scraping.")
    notes = fields.Text('Notes')

    def move_scrap(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        for data in self.browse(cr, uid, ids, context=context):
            reason = data.reason
            try:
                reason = int(data.reason)
            except:
                reason = False
            notes = reason and data.notes or False
            context.update({
                            'reason': reason,
                            'notes_reason': notes,
                            })
        return super(stock_move_scrap, self).\
            move_scrap(cr, uid, ids, context=context)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
