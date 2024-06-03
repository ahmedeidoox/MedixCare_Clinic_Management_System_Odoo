from .... import http
from ....http import request

class DepartmentsController(http.Controller):

    @http.route("/departments",auth="public",website=True)
    def GetAllDepartments(self):
        departments = request.env["clinic.department"].search([])
        return request.render("clinic_system.all_departments_template",{"departments":departments})