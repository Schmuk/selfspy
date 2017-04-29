import gherkin
from behave import *
import os
import psutil


class Program:
    program_name = ""
    opened = False

program_data = Program


@given('the user has attempted opening said program')
def step_impl():
    program_data.program_name = "firefox"
    os.system(program_data.program_name)


@when('the program opens')
def step_impl():
    process_list = psutil.pids()
    for process in range(0, len(process_list)):
        try:
            process_to_check = psutil.Process(process_list[process])
            if process_to_check.cmdline()[0].find("firefox") != -1:
                program_data.opened = True
                print("DEBUG: Found firefox")
            break
        except:
            pass


@then('the program is recognized')
def step_impl(self):
    self.assertEqual(True, False)
    #From here, I need to understand the program itself to know what to assertEqual
