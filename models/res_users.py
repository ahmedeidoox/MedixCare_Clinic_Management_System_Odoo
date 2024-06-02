from .... import models,fields



class ResUsers(models.Model):
    _inherit = "res.users"

    is_doctor = fields.Boolean(string="Is Doctor",default=False)
    department_id = fields.Many2one("clinic.department",string="Department")
    available_days = fields.Many2many("clinic.available.day")



