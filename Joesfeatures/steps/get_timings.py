# -*- coding: utf-8 -*-
from lettuce import *
import psutil
import os
import sys

#Used Ryan's existing logic to check if Spyspy is running
@step(u'Given: selfspy is running')
def given_selfspy_is_running(step):
    selfspy_running = True
    pid_exists = True
    process_list = psutil.pids()
    for process in range(0, len(process_list)):
        try:
            process_to_check = psutil.Process(process_list[process])
        except psutil.NoSuchProcess:
            pid_exists = False
        if pid_exists:
            for i in range(process_to_check.cmdline().__len__()):
                if "selfspy" in process_to_check.cmdline()[i] and "nautilus" not in process_to_check.cmdline()[i]:
                    selfspy_running = True
    if selfspy_running:
        assert True, "The program is running"
    else:
        assert False, "The program is not running"


@step(u'When: the user enters "--get-timings" into the command line')
def when_user_enters_gettimings_into_command_line(step):
    try:
        os.system("selfspy --get-timings")
    except OSError:
        assert False, 'selfspy has failed to run'
    assert True, "selfspy get-timings command ran successfully"


@step(u'Then: sql database will get return timings of all process_ids')
def then_database_will_return_process_id_timings(step):
    command = sys.argv
    if command == "selfspy --get-timings":
        assert True, "Process_Id timings have been returned successfully!"
    else:
        assert False, "Process_Id timings were not found."


