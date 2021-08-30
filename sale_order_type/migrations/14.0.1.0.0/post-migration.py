# Copyright 2020 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade  # pylint: disable=W7936

def migrate(cr, version):
    openupgrade.load_data(
        cr, "sale_order_type", "migrations/14.0.1.0.0/noupdate_changes.xml"
    )
