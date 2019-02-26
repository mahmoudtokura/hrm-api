from ma import ma


class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ("_id", "employee_id", "name","username", "email",
                  "image", "address","phone", "department",
                  "designation", "pay", "salary", "deduction",
                  "health_insurance", "loan", "leave")

        exclude = ("_id",)
