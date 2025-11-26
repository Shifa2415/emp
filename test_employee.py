#testemployee.py
import pytest
from employeedetails import get_ED
def test_get_ED():
    #sample data
    name="Alice Smith"
    emp_id="E194"
    dep="BCA"
    salary=60000
    #Expected result
    expected_output =(
        "Employee Name:Alice Smith,\n"
        "Employee ID:E194,\n"
        "Department:BCA,\n"
        "Salary:60000.00"
    )
    #Assertion
    assert get_ED(name, emp_id, dep, salary)==expected_output