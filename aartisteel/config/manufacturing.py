from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			'label': _('Custom Reports'),
			'items': [
				{ 'type': 'report', 'name': 'Mill Production Report', 'onboard': 1, 'route': 'query-report/Mill Production Report' }
			]
		},
    ]