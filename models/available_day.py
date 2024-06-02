from .... import models,fields,api
from ....exceptions import UserError


class ClinicAvailableDay(models.Model):
    _name = "clinic.available.day"


    name=fields.Char(string="Available days",required=True)














