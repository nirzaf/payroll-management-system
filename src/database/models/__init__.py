from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: str = Field(default_factory=str)
    first_name: str
    last_name: str
    email: str
    hire_date: datetime
    department: str
    position: str
    salary: float
    is_active: bool = True

class Attendance(BaseModel):
    id: str = Field(default_factory=str)
    employee_id: str
    date: datetime
    check_in: datetime
    check_out: Optional[datetime]
    status: str  # present, absent, leave

class Payroll(BaseModel):
    id: str = Field(default_factory=str)
    employee_id: str
    period_start: datetime
    period_end: datetime
    basic_salary: float
    overtime_pay: float = 0
    deductions: float = 0
    net_salary: float
    status: str  # draft, processed, paid
    payment_date: Optional[datetime]

class Benefit(BaseModel):
    id: str = Field(default_factory=str)
    employee_id: str
    benefit_type: str  # health, dental, life_insurance, etc.
    coverage_start: datetime
    coverage_end: Optional[datetime]
    amount: float
    status: str  # active, inactive

class TicketEntitlement(BaseModel):
    id: str = Field(default_factory=str)
    employee_id: str
    cycle_start: datetime
    cycle_end: datetime
    ticket_value: float
    status: str  # available, claimed, expired
    claim_date: Optional[datetime]
    cost_share_employee: float = 0
    cost_share_company: float

# Import document models
from .documents import (
    EmployeeDocument,
    PayrollDocument,
    AttendanceDocument,
    BenefitDocument,
    TicketEntitlementDocument
)