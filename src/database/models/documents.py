from mongoengine import Document, StringField, DateTimeField, FloatField, BooleanField, ReferenceField
from datetime import datetime
from typing import Optional

class EmployeeDocument(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True, unique=True)
    hire_date = DateTimeField(required=True)
    department = StringField(required=True)
    position = StringField(required=True)
    salary = FloatField(required=True)
    is_active = BooleanField(default=True)
    
    meta = {
        'collection': 'employees',
        'indexes': [
            'email',
            'department'
        ]
    }
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'hire_date': self.hire_date,
            'department': self.department,
            'position': self.position,
            'salary': self.salary,
            'is_active': self.is_active
        }

class PayrollDocument(Document):
    employee = ReferenceField('EmployeeDocument', required=True)
    period_start = DateTimeField(required=True)
    period_end = DateTimeField(required=True)
    basic_salary = FloatField(required=True)
    overtime_pay = FloatField(default=0)
    deductions = FloatField(default=0)
    net_salary = FloatField(required=True)
    status = StringField(required=True, choices=['draft', 'processed', 'paid'])
    payment_date = DateTimeField()
    
    meta = {
        'collection': 'payrolls',
        'indexes': [
            'employee',
            'period_start',
            'period_end',
            'status'
        ]
    }
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'employee_id': str(self.employee.id),
            'period_start': self.period_start,
            'period_end': self.period_end,
            'basic_salary': self.basic_salary,
            'overtime_pay': self.overtime_pay,
            'deductions': self.deductions,
            'net_salary': self.net_salary,
            'status': self.status,
            'payment_date': self.payment_date
        }

class AttendanceDocument(Document):
    employee = ReferenceField('EmployeeDocument', required=True)
    date = DateTimeField(required=True)
    check_in = DateTimeField(required=True)
    check_out = DateTimeField()
    status = StringField(required=True, choices=['present', 'absent', 'leave'])
    
    meta = {
        'collection': 'attendance',
        'indexes': [
            'employee',
            'date',
            'status'
        ]
    }
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'employee_id': str(self.employee.id),
            'date': self.date,
            'check_in': self.check_in,
            'check_out': self.check_out,
            'status': self.status
        }

class BenefitDocument(Document):
    employee = ReferenceField('EmployeeDocument', required=True)
    benefit_type = StringField(required=True)
    coverage_start = DateTimeField(required=True)
    coverage_end = DateTimeField()
    amount = FloatField(required=True)
    status = StringField(required=True, choices=['active', 'inactive'])
    
    meta = {
        'collection': 'benefits',
        'indexes': [
            'employee',
            'benefit_type',
            'status'
        ]
    }
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'employee_id': str(self.employee.id),
            'benefit_type': self.benefit_type,
            'coverage_start': self.coverage_start,
            'coverage_end': self.coverage_end,
            'amount': self.amount,
            'status': self.status
        }

class TicketEntitlementDocument(Document):
    employee = ReferenceField('EmployeeDocument', required=True)
    cycle_start = DateTimeField(required=True)
    cycle_end = DateTimeField(required=True)
    ticket_value = FloatField(required=True)
    status = StringField(required=True, choices=['available', 'claimed', 'expired'])
    
    meta = {
        'collection': 'ticket_entitlements',
        'indexes': [
            'employee',
            'cycle_start',
            'cycle_end',
            'status'
        ]
    }
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'employee_id': str(self.employee.id),
            'cycle_start': self.cycle_start,
            'cycle_end': self.cycle_end,
            'ticket_value': self.ticket_value,
            'status': self.status
        }