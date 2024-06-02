from .... import models,fields



class ResUsers(models.Model):
    _inherit = "res.users"

    is_doctor = fields.Boolean(string="Is Doctor",default=False)
    belonged_department = fields.Many2one("clinic.department",string="Department")
    available_days = fields.Many2many("clinic.available.day")
    experience_years = fields.Integer(default=1,required=True,string="Years Of Experience")


