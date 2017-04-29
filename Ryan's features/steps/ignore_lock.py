#from gherkin import *
from behave import *
import os
import psutil



class Selfspy_status:
    opened = True
    locked = False

program_data = Selfspy_status


@given('the user has entered the command line switch to ignore the lock')
def step_impl():
    os.system("selfspy --ignore-lock")


@when('selfspy program runs')
def step_impl():
    process_list = psutil.pids()
    for process in range(0, len(process_list)):
        try:
            process_to_check = psutil.Process(process_list[process])
            if process_to_check.cmdline()[0].find("selfspy") != -1:
                program_data.opened = True
                print("DEBUG: Selfspy is running!")
            break
        except:
            pass


@then('the program will ignore the lock')
def step_impl(self):
    self.assertEqual(True, False)
    # From here, I need to understand the program itself to know what to assertEqual


@given('the user has not entered the command line switch to ignore the lock')
def step_impl():
    try:
        os.system("selfspy")
    except:
        pass
        #The tests will fail if selfspy does not start, might as well let them


@when('the program runs')
def step_impl():
    process_list = psutil.pids()
    for process in range(0, len(process_list)):
        try:
            process_to_check = psutil.Process(process_list[process])
            if process_to_check.cmdline()[0].find("selfspy") != -1:
                program_data.opened = True
                print("DEBUG: Selfspy is running!")
            break
        except:
            pass
    # I have no idea how selfspy checks locks, excuse the extreme lack of code here to check such thing
    # I plan to learn how to kill 9 a process later on in order to properly test this.


@then('the program will acknowledge the lock')
def step_impl(self):
    self.assertEqual(True, False)
    # From here, I need to understand the program itself to know what to assertEqual
# -*- coding: utf-8 -*-
from lettuce import step

@step(u'Given: the user has entered the command line switch to ignore the lock')
def given_the_user_has_entered_the_command_line_switch_to_ignore_the_lock(step):
    assert False, 'This step must be implemented'
@step(u'When: program runs')
def when_program_runs(step):
    assert False, 'This step must be implemented'
@step(u'Then: the program will ignore the lock')
def then_the_program_will_ignore_the_lock(step):
    assert False, 'This step must be implemented'
@step(u'Given: the user has not entered the command line switch to ignore the lock')
def given_the_user_has_not_entered_the_command_line_switch_to_ignore_the_lock(step):
    assert False, 'This step must be implemented'
@step(u'When: the program runs')
def when_the_program_runs(step):
    assert False, 'This step must be implemented'
@step(u'Then: the program will acknowledge the lock')
def then_the_program_will_acknowledge_the_lock(step):
    assert False, 'This step must be implemented'
@step(u'Given: the user has attempted opening said program')
def given_the_user_has_attempted_opening_said_program(step):
    assert False, 'This step must be implemented'
@step(u'When: the program opens')
def when_the_program_opens(step):
    assert False, 'This step must be implemented'
@step(u'Then: the program is recognized')
def then_the_program_is_recognized(step):
    assert False, 'This step must be implemented'
