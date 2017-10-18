# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2017-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Nikhil krishnan(<https://www.cybrosys.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <https://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import fields, models


class RestaurantFloor(models.Model):
    _inherit = 'restaurant.floor'

    background_color = fields.Char('Background Color', help='The background color of the floor layout, '
                                                            '(must be specified in a html-compatible format)',
                                   default='#D2D2D2')

# Depends module 'web_widget_color' not work in wizard.
# class RestaurantTable(models.Model):
#     _inherit = 'restaurant.table'
#
#     color = fields.Char('Color', help="The table's color, expressed as a valid 'background' CSS property value",
#                         default='#35d374')
