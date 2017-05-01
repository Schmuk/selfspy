# -*- coding: utf-8 -*-
from lettuce import step
import os
import psutil
PROGRAM_NAME = "google-chrome-stable"
PROCESS_NAME = "chrome"


# Scenario: Program is recognized
@step(u'Given: the user has attempted opening said program')
def given_the_user_has_attempted_opening_said_program(step):
    try:
        os.system(PROGRAM_NAME)
    except OSError:
        assert False, PROGRAM_NAME + ' has failed to run'
    assert True, "command ran successfully"


@step(u'When: the program opens')
def when_the_program_opens(step):
    process_found = False
    pid_exists = True
    process_list = psutil.pids()
    # print process_list
    for process in range(0, len(process_list)):
        try:
            process_to_check = psutil.Process(process_list[process])
        except psutil.NoSuchProcess:
            pid_exists = False
        if pid_exists:
            for i in range(process_to_check.cmdline().__len__()):
                if PROCESS_NAME in process_to_check.cmdline()[i]:
                    process_found = True
    if process_found:
        assert True, "The program is running"
    else:
        assert False, "the program is not running"


@step(u'Then: the program is recognized')
def then_the_program_is_recognized(step):
    assert False, 'This step must be implemented'
