import datetime
import random
import os
from typing import List, Dict, Any, Optional
from database.models import EmployeeDocument, PayrollDocument, TicketEntitlementDocument

def load_sample_data():
    """
    Load sample data into the database if LOAD_SAMPLE_DATA is set to True in .env
    """
    if os.environ.get('LOAD_SAMPLE_DATA', 'False').lower() != 'true':
        return
    
    # Import here to avoid circular imports
    from database.models import EmployeeDocument, PayrollDocument, TicketEntitlementDocument
    
    # Check if data already exists
    if EmployeeDocument.objects.count() > 0:
        print("Sample data already exists, skipping...")
        return
    
    print("Loading sample data...")
    
    # Create sample employees
    employees = create_sample_employees()
    
    # Generate payroll data
    payrolls = generate_payroll_data(employees)
    
    # Generate ticket entitlements
    ticket_entitlements = generate_ticket_entitlements(employees)
    
    print(f"Created {len(employees)} employees")
    print(f"Created {len(payrolls)} payroll records")
    print(f"Created {len(ticket_entitlements)} ticket entitlements")

def create_sample_employees():
    """
    Create sample employee data
    """
    from database.models import EmployeeDocument
    
    employees = []
    
    # Sample departments
    departments = ['HR', 'Finance', 'IT', 'Operations', 'Sales', 'Marketing']
    
    # Sample job titles
    job_titles = {
        'HR': ['HR Manager', 'HR Specialist', 'Recruiter'],
        'Finance': ['Finance Manager', 'Accountant', 'Financial Analyst'],
        'IT': ['IT Manager', 'Software Developer', 'System Administrator', 'Network Engineer'],
        'Operations': ['Operations Manager', 'Operations Analyst', 'Quality Assurance'],
        'Sales': ['Sales Manager', 'Sales Representative', 'Account Manager'],
        'Marketing': ['Marketing Manager', 'Marketing Specialist', 'Content Creator']
    }
    
    # Sample names
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 'Lisa', 'William', 'Emma']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    
    # Create 50 sample employees
    for i in range(50):
        # Generate random employee data
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        department = random.choice(departments)
        job_title = random.choice(job_titles[department])
        
        # Generate random joining date (between 1 and 10 years ago)
        days_ago = random.randint(365, 3650)
        joining_date = datetime.datetime.now() - datetime.timedelta(days=days_ago)
        
        # Generate random salary (between 30,000 and 100,000)
        salary = random.randint(30000, 100000)
        
        # 90% of employees are active
        is_active = random.random() < 0.9
        
        # Create employee document
        employee = EmployeeDocument(
            employee_id=f'EMP{i+1:04d}',
            first_name=first_name,
            last_name=last_name,
            email=f'{first_name.lower()}.{last_name.lower()}@example.com',
            department=department,
            job_title=job_title,
            joining_date=joining_date,
            salary=salary,
            is_active=is_active
        )
        employee.save()
        employees.append(employee)
    
    return employees

def generate_payroll_data(employees: List[EmployeeDocument]) -> List[PayrollDocument]:
    """
    Generate sample payroll data for the given employees
    """
    payrolls = []
    today = datetime.datetime.now()
    
    # Generate payroll for the last 3 months
    for month in range(3):
        # Calculate period start and end dates using a safer approach
        # Start with the first day of current month
        first_day_current_month = today.replace(day=1)
        
        # Go back 'month' months from current month
        target_month = first_day_current_month.month - 1 - month  # -1 to get previous month
        target_year = first_day_current_month.year
        
        # Adjust year if we need to go back to previous year(s)
        while target_month < 1:
            target_month += 12
            target_year -= 1
            
        # Get the first day of the target month
        period_start = datetime.datetime(year=target_year, month=target_month, day=1)
        
        # Get the last day of the target month by getting the first day of next month and subtracting 1 day
        if target_month == 12:
            next_month_year = target_year + 1
            next_month = 1
        else:
            next_month_year = target_year
            next_month = target_month + 1
            
        period_end = datetime.datetime(year=next_month_year, month=next_month, day=1) - datetime.timedelta(days=1)
        
        for employee in employees:
            if not employee.is_active and random.random() > 0.7:
                continue  # Skip some inactive employees
                
            # Calculate basic salary (monthly)
            basic_salary = employee.salary / 12
            
            # Calculate overtime pay (random amount)
            overtime_hours = random.randint(0, 20)
            overtime_rate = employee.salary / (12 * 22 * 8) * 1.5  # Hourly rate * 1.5
            overtime_pay = overtime_hours * overtime_rate
            
            # Calculate deductions (tax, insurance, etc.)
            deduction_rate = 0.15 + random.random() * 0.1  # 15-25% deductions
            deductions = (basic_salary + overtime_pay) * deduction_rate
            
            # Calculate net salary
            net_salary = basic_salary + overtime_pay - deductions
            
            # Determine payment status and date
            if month == 0:  # Current month
                status = random.choice(['draft', 'processed'])
                payment_date = None
            else:  # Previous months
                status = 'paid'
                # Payment date is typically 5 days after period end
                payment_date = period_end + datetime.timedelta(days=5)
            
            payroll = PayrollDocument(
                employee_id=str(employee.id),
                period_start=period_start,
                period_end=period_end,
                basic_salary=round(basic_salary, 2),
                overtime_pay=round(overtime_pay, 2),
                deductions=round(deductions, 2),
                net_salary=round(net_salary, 2),
                status=status,
                payment_date=payment_date
            )
            payroll.save()
            payrolls.append(payroll)
    
    return payrolls

def generate_ticket_entitlements(employees: List[EmployeeDocument]) -> List[TicketEntitlementDocument]:
    """
    Generate sample ticket entitlements for the given employees
    """
    entitlements = []
    today = datetime.datetime.now()
    
    for employee in employees:
        # Skip some inactive employees
        if not employee.is_active and random.random() > 0.7:
            continue
            
        # Calculate years of service
        years_of_service = (today - employee.joining_date).days / 365.25
        
        # Determine number of ticket cycles completed
        # Assuming a ticket cycle is 2 years
        cycles_completed = int(years_of_service / 2)
        
        # Calculate next ticket date
        next_ticket_date = employee.joining_date + datetime.timedelta(days=int((cycles_completed + 1) * 2 * 365.25))
        
        # Calculate pro-rata percentage
        days_in_current_cycle = (today - (employee.joining_date + datetime.timedelta(days=int(cycles_completed * 2 * 365.25)))).days
        pro_rata_percentage = min(100, max(0, days_in_current_cycle / (2 * 365.25) * 100))
        
        # Determine if ticket was claimed early in previous cycle
        claimed_early = random.random() < 0.3
        
        # If claimed early, adjust cost sharing
        cost_sharing_employee = 0
        if claimed_early:
            # Assuming 50/50 split if claimed early
            cost_sharing_employee = 50
        
        # Create ticket entitlement document
        entitlement = TicketEntitlementDocument(
            employee_id=str(employee.id),
            next_ticket_date=next_ticket_date,
            pro_rata_percentage=round(pro_rata_percentage, 2),
            cost_sharing_employee=cost_sharing_employee,
            claimed_early=claimed_early,
            status='active' if employee.is_active else 'inactive'
        )
        entitlement.save()
        entitlements.append(entitlement)
    
    return entitlements
    """
    Generate sample payroll data for the given employees
    """
    payrolls = []
    today = datetime.datetime.now()
    
    # Generate payroll for the last 3 months
    for month in range(3):
        # Calculate period start and end dates using a safer approach
        # Start with the first day of current month
        first_day_current_month = today.replace(day=1)
        
        # Go back 'month' months from current month
        target_month = first_day_current_month.month - 1 - month  # -1 to get previous month
        target_year = first_day_current_month.year
        
        # Adjust year if we need to go back to previous year(s)
        while target_month < 1:
            target_month += 12
            target_year -= 1
            
        # Get the first day of the target month
        period_start = datetime.datetime(year=target_year, month=target_month, day=1)
        
        # Get the last day of the target month by getting the first day of next month and subtracting 1 day
        if target_month == 12:
            next_month_year = target_year + 1
            next_month = 1
        else:
            next_month_year = target_year
            next_month = target_month + 1
            
        period_end = datetime.datetime(year=next_month_year, month=next_month, day=1) - datetime.timedelta(days=1)
        
        for employee in employees:
            if not employee.is_active and random.random() > 0.7:
                continue  # Skip some inactive employees
                
            # Calculate basic salary (monthly)
            basic_salary = employee.salary / 12
            
            # Calculate overtime pay (random amount)
            overtime_hours = random.randint(0, 20)
            overtime_rate = employee.salary / (12 * 22 * 8) * 1.5  # Hourly rate * 1.5
            overtime_pay = overtime_hours * overtime_rate
            
            # Calculate deductions (tax, insurance, etc.)
            deduction_rate = 0.15 + random.random() * 0.1  # 15-25% deductions
            deductions = (basic_salary + overtime_pay) * deduction_rate
            
            # Calculate net salary
            net_salary = basic_salary + overtime_pay - deductions
            
            # Determine payment status and date
            if month == 0:  # Current month
                status = random.choice(['draft', 'processed'])
                payment_date = None
            else:  # Previous months
                status = 'paid'
                # Payment date is typically 5 days after period end
                payment_date = period_end + datetime.timedelta(days=5)
            
            payroll = PayrollDocument(
                employee_id=str(employee.id),
                period_start=period_start,
                period_end=period_end,
                basic_salary=round(basic_salary, 2),
                overtime_pay=round(overtime_pay, 2),
                deductions=round(deductions, 2),
                net_salary=round(net_salary, 2),
                status=status,
                payment_date=payment_date
            )
            payrolls.append(payroll)
    
    return payrolls