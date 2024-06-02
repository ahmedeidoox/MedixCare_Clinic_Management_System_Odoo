from .... import models,fields,api


class ClinicPatient(models.Model):
    _name = "clinic.patient"
    _rec_name = "full_name"


    full_name = fields.Char(required= True,string="Full Name")
    phone_number = fields.Char(required = True,size=11, string="Phone Number")
    age = fields.Integer(string="Age",required=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ],string="Gender",required=True)

    medical_history = fields.Html(string="Medical History")




