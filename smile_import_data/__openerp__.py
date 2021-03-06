# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010 OpenERP s.a. (<http://openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Smile Import Data',
    'version': '0.1',
    'category': 'Tools',
    'description': """Smile Import Data
                    Manage import data :
                        Validate files before importing
                        Insert data with diferent mode:
                            By using import data method
                                or by usinf specific scripts
                        Generate logs

Suggestions & Feedback to: samir.rachedi@smile.fr
""",
    'author': 'Smile',
    'website': 'http://www.smile.fr',
    'depends': ['base'],
    'init_xml': [],
    'update_xml': ['view/import_data_view.xml'],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
