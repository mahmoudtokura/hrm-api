from ma import ma


class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ("_id", "employee_id", "full_name","username", "email",
                  "imageUrl", "address","phone", "department",
                  "designation", "pay", "salary", "deduction",
                  "health_insurance", "loan", "leave", "department", "employment_data",
                  "note")

        exclude = ("_id",)
