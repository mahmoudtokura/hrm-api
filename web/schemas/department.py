from ma import ma


class DepartmentSchema(ma.Schema):
    class Meta:
        fields = ("_id", "name", "HOD")

        exclude = ("_id",)
