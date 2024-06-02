from .... import models,fields,api


class ClinicDepartment(models.Model):
    _name = "clinic.department"

    name = fields.Char(string="Name",required=True)
    available_days = fields.Many2many("clinic.available.day",string="Available Days")
    ticket_price= fields.Float(required=True,default=0.0,string="Ticket Price")

    doctor_ids = fields.One2many("res.users","department_id",string="Doctors")








