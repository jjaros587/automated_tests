from selenium.webdriver.common.by import By


class OtherLocators:
    link_employee_card = (By.XPATH, "//*[text()='Pokračovat na kartu zaměstnance']/..")
    button_approve_or_send_to_approval = (By.ID, "form_approve_or_send_to_approval")
    button_create_employment = (By.ID, "form_create_employment")
    link_login_as_employee = (By.XPATH, "//*[text()='Přihlásit se jako tento uživatel']")


class LoginPageLocators:
    field_username = (By.XPATH, "//input[@name='_username']")
    field_password = (By.XPATH, "//input[@name='_password']")
    button_login = (By.TAG_NAME, "button")
    alert = (By.CLASS_NAME, 'alert')


class MenuEmployeesPageLocators:
    main = (By.XPATH, "//ul[@class='m-main__list']/li//*[text()[contains(.,'%s')]]/..")
    link_employees = (By.XPATH, "//a[text()[contains(.,'%s')]]/.")
    link_document_definitions = (By.XPATH, "//a[text()[contains(.,'%s')]]/.")
    link_changes = (By.XPATH, "//a[text()[contains(.,'%s')]]/.")
    link_changes_new = (By.XPATH, "//a[text()[contains(.,'%s')]]/.")
    link_documents_overview = (By.XPATH, "//a[text()[contains(.,'%s')]]/.")


class MenuAttendancePageLocators:
    main = (By.XPATH, "//ul[@class='m-main__list']/li//span[text()[contains(.,'%s')]]/..")
    link_plan = (By.XPATH, "//a[text()[contains(.,'%s')]]/.")
    link_closing = (By.XPATH, "//a[text()[contains(.,'%s')]]/.")


class MenuRequestsPageLocators:
    main = (By.XPATH, "//ul[@class='m-main__list']/li//span[text()[contains(.,'%s')]]/..")


class MenuSystemPageLocators:
    main = (By.XPATH, "//ul[@class='m-main__list']/li//span[text()[contains(.,'%s')]]/..")
    link_users = (By.XPATH, "//a[text()[contains(.,'%s')]]/.")
    link_roles = (By.XPATH, "//a[text()[contains(.,'%s')]]/.")
    link_companies = (By.XPATH, "//a[text()[contains(.,'%s')]]/.")
    link_system_settings = (By.XPATH, "//a[text()[contains(.,'%s')]]/.")
    link_licence = (By.XPATH, "//a[text()[contains(.,'%s')]]/.")


class EmployeesPageLocators:
    button_new_employee = (By.XPATH, "//*[text()[contains(.,'Nový zaměstnanec')]]/.")
    select_employment = (By.ID, "employ-filter-employment")
    select_group = (By.ID, "employ-filter-group")
    select_company = (By.ID, "employ-filter-company")
    select_unit = (By.ID, "employ-filter-unit")
    link_employee = (By.XPATH, "//td[@data-before='Jméno']//a[@href[contains(.,'%s')]]")


class NewEmployeePageLoators:
    field_name = (By.ID, "user_form_name")
    field_surname = (By.ID, "user_form_surname")
    field_email = (By.ID, "user_form_email")
    field_phone = (By.ID, "user_form_phone")
    '''
    dropdown_jazyk = (By.XPATH, "//a[text()[contains(.,'Nastavení aplikace')]]/.")
    '''
    dropdown_accessible_for_unit_ids = (By.ID, "user_form_accessible_for_unit_ids")
    dropdown_default_approver_id = (By.XPATH, "//*[@id='user_form_default_approver_id']")
    checkbox_agreement = (By.XPATH, "//input[@id='user_form_agreement']/..")
    button_save = (By.ID, "user_form_save")


class NewUserPageLocators:
    field_name = (By.ID, "user_form_name")
    field_surname = (By.ID, "user_form_surname")
    field_email = (By.ID, "user_form_email")
    field_phone = (By.ID, "user_form_phone")
    checkbox_user_roles = (By.NAME, "user_form[user_roles][]")
    checkbox_agreement = (By.XPATH, "//input[@id='user_form_agreement']/..")
    button_save = (By.ID, "user_form_save")


class PersonalInquiry1PageLocators:
    field_birth_number = (By.ID, "form_birth_number")
    field_residence_street_and_house_number = (By.ID, "form_residence_street_and_house_number")
    field_residence_city = (By.ID, "form_residence_city")
    field_residence_zip = (By.ID, "form_residence_zip")
    button_save_and_continue = (By.ID, "form_save_and_continue")


class PersonalInquiry2PageLocators:
    field_birth_place = (By.ID, "form_birth_place")
    button_save_and_continue = (By.ID, "form_save_and_continue")


class PersonalInquiry3PageLocators:
    field_paycheck_password = (By.ID, "form_paycheck_password")
    dropdown_health_insurance_company_code = (By.ID, "form_health_insurance_company_code")
    radio_having_some_pension = (By.NAME, "form[having_some_pension]")
    radio_having_handicap_or_disability_card = (By.NAME, "form[having_handicap_or_disability_card]")
    radio_having_wages_deductions = (By.NAME, "form[having_wages_deductions]")
    radio_having_social_insurance_abroad = (By.NAME, "form[having_social_insurance_abroad]")
    button_save_and_recap = (By.ID, "form_save_and_recap")


class SearchPageLocators:
    wrap = (By.XPATH, "//*[@class[contains(.,'f-search__wrap')]]")
    button_show_search_form = (By.ID, "btn-show-search-form")
    field_search = (By.NAME, "q")
    radio_scope_users = (By.XPATH, "//input[@id='search-scope-users']/..")
    table_quick_results = (By.XPATH, "//div[@id='search-form-quick-results-content']//table")
    button_search = (By.XPATH, "//form[@id='form-search']//button")


class EmployeeCardPageLocators:
    link_employements = (By.LINK_TEXT, "Pracovní poměry")
    # Employments
    button_add_employment = (By.XPATH, "//*[text()[contains(.,'Přidat nový pracovní poměr')]]/..")
    item_company = (By.XPATH, "//a[contains(.,'%s')]")


class NewEmployment1PageLocators:
    employment_number = (By.XPATH, "//*[@id='txt-employment-number']")
    radio_type = (By.NAME, "form[type]")
    field_start_date = (By.ID, "form_start_date")
    filed_boarding_date = (By.ID, "form_boarding_date")
    dropdown_organization_unit_id = (By.XPATH, "//*[@id='form_organization_unit_id']")
    dropdown_cost_center_id = (By.ID, "form_cost_center_id")
    dropdown_work_position_id = (By.ID, "form_work_position_id")
    dropdown_superior_of_unit_ids = (By.ID, "form_superior_of_unit_ids")
    dropdown_immediate_superior_user_id = (By.ID, "form_immediate_superior_user_id")
    dropdown_current_approver_id = (By.ID, "form_current_approver_id")
    button_save_and_continue = (By.ID, "form_save_and_continue")


class NewEmployment2PageLocators:
    dropdown_duration_months = (By.ID, "form_duration_months")
    dropdown_trial_period_months = (By.ID, "form_trial_period_months")
    dropdown_shift_type = (By.ID, "form_shift_type")
    field_working_hours_per_week = (By.ID, "form_working_hours_per_week")
    radio_working_hours_type = (By.NAME, "form[working_hours_type]")
    field_basic_salary = (By.ID, "form_basic_salary")
    link_add_benefits = (By.XPATH, "//*[text()[contains(., 'Přidat odměnu')]]")

    button_save_and_continue = (By.ID, "form_save_and_continue")

    # BENEFITS
    dropdown_type_id = (By.ID, "form_type_id")
    field_exact_amount = (By.ID, "form_exact_amount")
    field_hourly_amount = (By.ID, "form_hourly_bonus")
    field_percentual_amount = (By.ID, "form_percentage_bonus")

    button_save = (By.ID, "form_save")
    link_close = (By.XPATH, "//a[text()='Zavřít']")


class NewEmployment3PageLocators:
    button_save_and_continue = (By.ID, "form_save_and_continue")


class NewEmployment4PageLocators:
    button_save_and_continue = (By.ID, "form_save_and_continue")


# COMPANIES ------------------------------------------------------------------------------------------
class CompaniesPageLocators:
    button_add_company = (By.XPATH, "//*[text()[contains(.,'Přidat další společnost')]]/..")
    item_country = (By.XPATH, "//a[@href[contains(.,'%s')]]/.")
    link_delete_company = (By.XPATH, "//*[text()='%s']/../..//a[@class[contains(.,'remove')]]")
    link_delete_permanent = (By.XPATH, "//*[text()='Smazat trvale']/parent::button")
    link_delete_confirm = (By.XPATH, "//*[text()='Ano']/parent::button")


class NewCompany1PageLocators:
    field_name = (By.ID, "form_name")
    field_shortened_name = (By.ID, "form_shortened_name")
    field_identification_code = (By.ID, "form_identification_code")
    field_address_street_and_number = (By.ID, "form_address_street_and_number")
    field_address_city = (By.ID, "form_address_city")
    dropdown_address_zip = (By.ID, "form_address_zip")
    field_registered_when = (By.ID, "form_registered_when")
    field_court_name = (By.ID, "form_court_name")
    field_court_case = (By.ID, "form_court_case")
    field_default_wages_item_code = (By.ID, "form_default_wages_item_code")
    field_wages_constant_symbol = (By.ID, "form_wages_constant_symbol")
    dropdown_wages_variable_symbol_strategy = (By.ID, "form_wages_variable_symbol_strategy")
    button_save_and_continue = (By.ID, "form_save_and_continue")
    button_load_automatically = (By.ID, "a-load-from-business-register")


class NewCompany2PageLocators:
    radio_personal_number_format = (By.NAME, "form[personal_number_format]")
    radio_personal_number_editable = (By.NAME, "form[personal_number_editable]")
    field_minimal_personal_number = (By.ID, "form_minimal_personal_number")

    field_balancing_period = (By.ID, "form_balancing_period")
    radio_balancing_period_units = (By.NAME, "form[balancing_period_units]")
    field_balancing_period_starts_when = (By.ID, "form_balancing_period_starts_when")

    radio_having_benefits = (By.NAME, "form[having_benefits]")
    link_add_benefits = (By.XPATH, "//*[text()[contains(., 'Přidat typ benefitu')]]")

    button_save_and_continue = (By.ID, "form_save_and_continue")

    # BENEFITS
    field_name = (By.ID, "form_name")
    field_localized_name_cs = (By.ID, "form_localized_name_cs")
    field_localized_name_en = (By.ID, "form_localized_name_en")
    field_wage_item_code = (By.ID, "form_wage_item_code")
    dropdown_reward_type = (By.ID, "form_reward_type")
    field_exact_amount = (By.ID, "form_exact_amount")
    field_hourly_amount = (By.ID, "form_hourly_amount")
    field_percentual_amount = (By.ID, "form_percentual_amount")
    radio_for_all_organization_units = (By.NAME, "form[for_all_organization_units]")
    radio_for_all_work_positions = (By.NAME, "form[for_all_work_positions]")

    button_save = (By.ID, "form_save")
    link_close = (By.XPATH, "//a[text()='Zavřít']")


class NewCompany3PageLocators:
    button_continue = (By.ID, "form_continue")


class NewCompany4PageLocators:
    link_add_organization_unit = (By.XPATH, "//*[text()[contains(.,'Přidat organizační útvar')]]")
    button_continue = (By.ID, "form_continue")
    # Modal
    field_name = (By.ID, "form_name")
    field_new_cost_center_name = (By.ID, "form_new_cost_center_name")
    field_new_cost_center_code = (By.ID, "form_new_cost_center_code")
    radio_same_address_as_parent = (By.NAME, "form[same_address_as_parent]")
    button_save = (By.ID, "form_save")
    link_close = (By.XPATH, "//a[text()='Zavřít']")


class NewCompany5PageLocators:
    link_add_work_position = (By.XPATH, "//*[text()[contains(.,'Přidat novou pozici')]]")
    button_finish = (By.ID, "form_finish")
    # Modal
    field_name = (By.ID, "form_name")
    field_localized_names_for_contract_cs = (By.ID, "form_localized_names_for_contract_cs")
    radio_for_all_organization_units = (By.NAME, "form[for_all_organization_units]")
    dropdown_organization_units_ids = (By.ID, "form_organization_units_ids")
    radio_managing_position = (By.NAME, "form[managing_position]")
    dropdown_medical_examination_work_category = (By.ID, "form_medical_examination_work_category")
    dropdown_job_group = (By.ID, "form_job_group")
    dropdown_shift_type = (By.ID, "form_shift_type")
    radio_working_hours_type = (By.NAME, "form[working_hours_type]")
    dropdown_default_trial_period_months = (By.ID, "form_default_trial_period_months")
    dropdown_job_classification_id = (By.ID, "form_job_classification_id")
    checkbox_roles = (By.NAME, "form[roles][]")
    dropdown_superior_of_position_ids = (By.ID, "form_superior_of_position_ids")

    button_save = (By.ID, "form_save")
    link_close = (By.XPATH, "//a[text()='Zavřít']")


class BaseChangePageLocators:
    button_create_amendment = (By.ID, "form_create_amendment")
    dropdown_operation = (By.XPATH, "//*[@class[contains(.,'hamburger')]]/ancestor::div[@class='row__item']")
    dropdown_operation_item_change = (By.XPATH, "//*[text()='Změna poměru']/..")
    dropdown_operation_item_cancel = (By.XPATH, "//*[text()='Ukončit poměr']/..")
    dropdown_operation_item_extend = (By.XPATH, "//*[text()='Prodloužit pracovní poměr']/..")


class ChangeEmployment1PageLocators:
    field_date_from = (By.ID, "form_valid_from_date")
    field_date_to = (By.ID, "form_valid_to_date")
    checkbox_change = (By.XPATH, "//*[@name='form[changes][]']")
    button_save_and_continue = (By.ID, "form_save_and_continue")


class ChangeEmployment2PageLocators:
    button_save_and_continue = (By.ID, "form_save_and_continue")
    # salary
    field_salary = (By.ID, "form_basic_salary")
    radio_salary_type = (By.NAME, "form[salary_type]")
    # position
    dropdown_position = (By.ID, "form_work_position_id")
    # commitment_or_working_hours
    dropdown_shift_type = (By.ID, "form_shift_type")
    field_working_hours = (By.ID, "form_working_hours_per_week")
    # organization_unit_cost_center
    dropdown_organization_unit_id = (By.ID, "form_organization_unit_id")
    # other_workplace
    field_other_workplace = (By.ID, "form_other_workplace")
    # regular_workplace_for_travel_refunds
    field_regular_workplace_for_travel_refunds = (By.ID, "form_regular_workplace_for_travel_refunds")
    # other_agreements
    radio_having_holidays = (By.NAME, "form[having_holidays]")
    field_holiday_days_count = (By.ID, "form_holiday_days_count")

    # BENEFITS
    link_add_benefits = (By.XPATH, "//*[text()[contains(., 'Přidat odměnu')]]")
    dropdown_type_id = (By.ID, "form_type_id")
    field_exact_amount = (By.ID, "form_exact_amount")
    field_hourly_amount = (By.ID, "form_hourly_bonus")
    field_percentual_amount = (By.ID, "form_percentage_bonus")

    button_save = (By.ID, "form_save")
    link_close = (By.XPATH, "//a[text()='Zavřít']")


class ChangeEmployment3PageLocators:
    button_save_and_finish = (By.ID, "form_save_and_finish")


class CancelEmploymentPageLocators:
    dropdown_termination_method_identifier = (By.ID, "form_termination_method_identifier")
    field_termination_notice_delivery_date = (By.ID, "form_termination_notice_delivery_date")
    field_termination_date = (By.ID, "form_termination_date")
    dropdown_leaving_benefit_type = (By.ID, "form_leaving_benefit_type")
    radio_competitive_clause_agreed = (By.NAME, "form[competitive_clause_agreed]")
    field_leaving_benefit_bonus = (By.ID, "form_leaving_benefit_bonus")
    field_leaving_benefit_average_salary_multiplier = (By.ID, "form_leaving_benefit_average_salary_multiplier")
    field_competitive_clause_months = (By.ID, "form_competitive_clause_months")
    field_competitive_clause_average_salary_percent = (By.ID, "form_competitive_clause_average_salary_percent")
    field_competitive_clause_agreements = (By.ID, "form_competitive_clause_agreements")

    button_save_and_continue = (By.ID, "form_save_and_continue")
    button_create_termination = (By.ID, "form_create_termination")


class ExtendEmployment1PageLocators:
    dropdown_duration_extension_by_months = (By.ID, "form_duration_extension_by_months")
    field_duration_extension_to_date = (By.ID, "form_duration_extension_to_date")
    button_save_and_continue = (By.ID, "form_save_and_continue")


class ExtendEmployment2PageLocators:
    button_save_and_finish = (By.ID, "form_save_and_finish")


class AttendancePageLocators:
    dropdown_attendance_company_select = (By.ID, "attendance-company-select")
    link_new_absence = (By.XPATH, "//a[@data-src[contains(.,'new-absence')]]")
    link_new_shift = (By.XPATH, "//a[@data-src[contains(.,'new-shift')]]")


class AttendanceNewShiftPageLocators:
    dropdown_employment = (By.ID, "shift_form_employment")
    field_date_from = (By.ID, "shift_form_date_from")
    field_time_from = (By.ID, "shift_form_time_from")
    field_time_to = (By.ID, "shift_form_time_to")
    dropdown_breaks = (By.ID, "shift_form_breaks")
    dropdown_repetition = (By.ID, "shift_form_repetition")
    dropdown_color = (By.ID, "shift_form_color")
    field_name = (By.ID, "shift_form_name")
    field_note = (By.ID, "shift_form_note")
    button_save = (By.ID, "shift_form_save")
    link_close = (By.XPATH, "//a[text()='Zrušit']")


class AttendanceNewAbsencePageLocators:
    button_save = (By.ID, "shift_form_save")
    link_close = (By.XPATH, "//a[text()='Zrušit']")
