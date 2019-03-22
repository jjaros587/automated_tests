from tests.login.LoginTest import LogInTest
from tests.navigation.MainMenuTest import MainMenuTest
from tests.employees.newEmployee.NewEmployeeTest import NewEmployeeTest
from tests.employees.personalInquiry.PersonalInquiryTest import PersonalInquiryTest
from tests.employees.employments.newEmployment.NewEmploymentTest import NewEmploymentTest
from tests.users.NewUserTest import NewUserTest
from tests.companies.newCompany.NewCompanyTest import NewCompanyTest
from tests.employees.employments.changeEmployment.ChangeEmploymentTest import ChangeEmploymentTest
from tests.employees.employments.cancelEmployment.CancelEmploymentTest import CancelEmploymentTest
from tests.employees.employments.extendEmployment.ExtendEmploymentTest import ExtendEmploymentTest
from tests.companies.permissions.PermissionsVisibilityOfEmployeesTest import PermissionsVisibilityOfEmployeesTest
from tests.companies.permissions.PermissionsVisibilityOfUnitsAndPositionsTest import PermissionsVisibilityOfUnitsAndPositionsTest
from tests.attendance.AttendanceNewShiftTest import AttendanceNewShiftTest

allTests = [
    LogInTest,
    MainMenuTest,
    NewUserTest,
    NewEmployeeTest,
    PersonalInquiryTest,
    NewEmploymentTest,
    NewCompanyTest,
    ChangeEmploymentTest,
    CancelEmploymentTest,
    ExtendEmploymentTest,
    PermissionsVisibilityOfEmployeesTest,
    PermissionsVisibilityOfUnitsAndPositionsTest,
    AttendanceNewShiftTest
]

currentSuite = [
    LogInTest,
    MainMenuTest,
    NewUserTest,
    NewEmployeeTest,
    PersonalInquiryTest,
    NewEmploymentTest,
    NewCompanyTest,
    ChangeEmploymentTest,
    CancelEmploymentTest,
    ExtendEmploymentTest,
    PermissionsVisibilityOfEmployeesTest,
    PermissionsVisibilityOfUnitsAndPositionsTest,
    AttendanceNewShiftTest
]