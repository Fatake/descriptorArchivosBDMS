class Employee():
    def __init__(self,employees_id,first_name,last_name,email,phone_number,hire_date,job_id,salary,commission_pct,manager_id,department_id):
        self.employees_id   = employees_id
        self.first_name     = first_name
        self.last_name      = last_name
        self.email          = email
        self.phone_number   = phone_number
        self.hire_date      = hire_date
        self.job_id         = job_id
        self.salary         = salary
        self.commission_pct = commission_pct
        self.manager_id     = manager_id
        self.department_id  = department_id

    def employeeToList(self):
        listaCampos = []
        listaCampos.append(str(self.employees_id))
        listaCampos.append(self.first_name)
        listaCampos.append(self.last_name)
        listaCampos.append(self.email)
        listaCampos.append(self.phone_number)
        listaCampos.append(self.hire_date)
        listaCampos.append(self.job_id)
        listaCampos.append(str(self.salary))
        listaCampos.append(str(self.commission_pct))
        listaCampos.append(str(self.manager_id))
        listaCampos.append(str(self.department_id))
        return listaCampos

class Department():
    def __init__(self,department_id,department_name,manager_id,location_id):
        self.department_id = department_id
        self.department_name = department_name
        self.manager_id = manager_id
        self.location_id = location_id

    def departmentToList(self):
        listaCampos = []
        listaCampos.append(str(self.department_id))
        listaCampos.append(self.department_name)
        listaCampos.append(str(self.manager_id))
        listaCampos.append(str(self.location_id))
        return listaCampos