{
    "name": "MedixCare Clinic Management System",
    "author":"Ahmed Eid Abdallah",
    "category":"",
    "version":"17.0.0.1.0",
    "depends":["base"],
    "data":[
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/base_menu.xml",
        "views/departments_view.xml",
        "views/patients_view.xml",
        "views/res_users_doctors.xml",
        "views/department_website_template.xml",
            ],

    "assets":{
        "web.assets_frontend":[
            "clinic_system/static/src/css/frontend/departments_template_style.css",
        ]
    },
    "application":True,


}