import unittest
from configs import config
from configs.suite import currentSuite
from HtmlTestRunner import HTMLTestRunner
import os
import shutil
import argparse
import json
from configs.config import folders
from configs.constants import environments


def delete_assets_folder():
    path = folders['root']
    if os.path.exists(path):
        shutil.rmtree(path)


def parse_args():
    parse = argparse.ArgumentParser()
    parse.add_argument("--headless", type=bool, default=False, help="Run in headless mode. Add arg to run in headless.")
    parse.add_argument("-e", "--env", required=True, type=str, help="Name of enviroment: " + str(environments.keys()))
    args = parse.parse_args()
    return {'parse': parse, 'args': args}


def verify_args(parse, args):
    os.environ['headless'] = str(args.headless)
    if args.env in environments:
        os.environ['env'] = args.env
    else:
        print("Zadejte prosím platný název prostředí")
        parse.print_help()
        quit(2)


def run_tests():
    for browser in config.browsers:
        if browser['allowed']:
            print(browser['name'])
            os.environ['BROWSER'] = browser['name']
            tests = []
            for item in currentSuite:
                tests.append(unittest.TestLoader().loadTestsFromTestCase(item))
            HTMLTestRunner(
                combine_reports=True,
                output=folders['reports'],
                report_name='TestResults_' + os.environ.get("BROWSER"),
                add_timestamp=False,
                report_title='Report - ' + os.environ.get("BROWSER")
            ).run(unittest.TestSuite(tests))


def zip_screenshots():
    path = folders['screenshots']
    if os.path.exists(path):
        shutil.make_archive(folders['output'] + '/screenshots', 'zip', path)


def get_data_from_json(path):
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
        file.close()
        return data[0]