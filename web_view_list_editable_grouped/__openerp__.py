# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016-Today Julius Network Solutions SARL <contact@julius.fr>
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

{
    "name": "Web list editable even when grouped",
    "version": "1.0",
    "author": "Julius Network Solutions",
    "contributors": "Mathieu Vatel <mathieu@julius.fr>",
    "website": "http://julius.fr",
    "category": "Hidden",
    "depends": [
                "web",
                ],
    "description": """
Allow to edit lines in the tree view when grouped
=================================================

""",
    "demo": [],
    "data": [
             'views/web_tree.xml',
             ],
    'installable': True,
    'active': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: