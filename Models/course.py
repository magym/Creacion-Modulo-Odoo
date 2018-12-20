from odoo import models , field

class Course(models.Model):
	_name = 'PrimerModulo.course'
	
	name = field.Char(
		required=True,
		string='Title',
		)
		description = fields.Text(
		)
