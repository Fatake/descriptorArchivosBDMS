class empleado():
    def __init__(self,employees_id,first_name,last_name,email,phone_number ,hire_date,job_id,salary,commission_pct,manager_id,department_id):
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

    def __str__(self):
        aux = ""+self.employees_id+" "+self.first_name+" "+self.last_name+" "+self.email+" "+self.phone_number+" "+self.hire_date
        aux2 = " "+self.job_id+" "+self.salary+" "+self.commission_pct+" "+self.manager_id+" "+self.department_id
        return aux+aux2