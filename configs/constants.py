import os
import sys

dataPath = os.path.dirname(os.path.realpath(sys.modules['__main__'].__file__)) + "\\data\\"

environments = {
    'dev': 'http://tria.epk-tech.com/',
    'test': '',
    'stage': 'https://stage.decasport.triahr.com/'
}

unwanted_status_codes = ["4", "5"]

select_allowed_cases = {
    "known": "//option[@value='%s']",
    "contains": "//option[@value[contains(.,'%s')]]",
    "text": "//option[contains(text(),'%s')]"
}

checbox_locators = {
    "1": "..",
    "2": "../.."
}

url_delimiters = {
    "employee": "/employee-created/",
    "user": "/user-created/"
}

screens = {
    "users": "users",
    "employees": "employees",
    "inquiry": {
        "1": "contract-info",
        "2": "other-employee-details",
        "3": "wages-info",
        "summary": "summary"
    },
    "employment": {
        "newEmployment": {
            "1": "basic-info",
            "2": "contract-info",
            "3": "other-employee-details",
            "4": "wages-info",
            "summary": "summary"
        },
        "changeEmployment": {
            "1": "contract-info",
            "2": "other-employee-details",
            "3": "wages-info",
            "summary": "summary"
        },

    },
    "newEmployment": {
        "1": "contract-info",
        "2": "other-employee-details",
        "3": "wages-info",
        "summary": "summary"
    },
    "company": {
        "1": "new-company/%s",
        "2": "settings",
        "3": "company-documents",
        "4": "organization-units",
        "5": "work-positions",
        "finish": "setup-finished"
    }
}

menu = {
    "attendance": {
        "main": "Docházka",
        "plan": {
            "locator": "attendance/plan",
            "link": "Plánování směn",
        },
        "closing": {
            "locator": "attendance/closing",
            "link": "Uzávěrka",
        }
    },
    "employees": {
        "main": "Zaměstnanci",
        "employees": {
            "locator": "employees",
            "link": "Přehled zaměstnanců",
        },
        "documentDefinition": {
            "locator": "employees/document-definitions",
            "link": "Nastavení dokumentů",
        },
        "changes": {
            "locator": "employees/not-checked-changes",
            "link": "Přehled změn",
        },
        "changesNew": {
            "locator": "employees/changes/overview",
            "link": "Nový přehled změn",
        },
        "documentOverview": {
            "locator": "employees/documents-overview/accountant",
            "link": "Nahrané dokumenty",
        }
    },
    "requests": {
        "locator": "approval-requests/handled-by-me",
        "link": "Žádosti"
    },
    "system": {
        "main": "Systém",
        "users": {
            "locator": "users",
            "link": "Uživatelé",
        },
        "roles": {
            "locator": "roles",
            "link": "Role",
        },
        "companies": {
            "locator": "companies",
            "link": "Společnosti",
        },
        "systemSettings": {
            "locator": "system-settings",
            "link": "Nastavení aplikace",
        },
        "licence": {
            "locator": "licence",
            "link": "Licence",
        }
    }
}