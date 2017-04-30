# -*- coding: utf-8 -*-
from lettuce import step
import os
import psutil
import time
USERNAME = "ryan"


# Scenario: lock is ignored
@step(u'Given: a lock already exists')
def given_a_lock_already_exists(step):
    if os.path.exists('/home/'+USERNAME+'/.selfspy/selfspy.pid.lock'):
        assert True, "the lockfile already exists"
    else:
        assert False, "the lockfile does not exist"


@step(u'When: the user has entered the command line switch to ignore the lock')
def when_the_user_has_entered_the_command_line_switch_to_ignore_the_lock(step):
    try:
        os.system("selfspy --ignore-lock")
    except OSError:
        assert False, 'selfspy has failed to run'
    assert True, "selfspy ignore lock command ran successfully"


@step(u'Then: the program will delete_the_lock_and_close')
def then_the_program_will_delete_the_lock_and_close(step):
    if os.path.exists('/home/'+USERNAME+'/.selfspy/selfspy.pid.lock'):
        lock_deleted = False
    else:
        lock_deleted = True
    process_found = False
    pid_exists = True
    process_list = psutil.pids()
    for process in range(0, len(process_list)):
        try:
            process_to_check = psutil.Process(process_list[process])
        except psutil.NoSuchProcess:
            pid_exists = False
        if pid_exists:
            for i in range(process_to_check.cmdline().__len__()):
                if "selfspy" in process_to_check.cmdline()[i]:
                    process_found = True
    if not process_found and lock_deleted:
        assert True, "The program deleted the lock and closed"
    else:
        assert False, "the program did not delete the lock OR the program is still running"


# Scenario: lock is acknowledged
@step(u'Given: a lock exists')
def given_a_lock_exists(step):
    os.system("selfspy &")
    time.sleep(3)
    os.system("pkill --signal 9 selfspy")
    if os.path.exists('/home/'+USERNAME+'/.selfspy/selfspy.pid.lock'):
        assert True, "the lockfile already exists"
    else:
        assert False, "the lockfile does not exist"


@step(u'When: the user has not entered the command line switch to ignore the lock')
def when_the_user_has_not_entered_the_command_line_switch_to_ignore_the_lock(step):
    try:
        os.system("selfspy")
    except OSError:
        assert False, 'selfspy has failed to run'
    assert True, "command entered successfully"


@step(u'Then: the program will acknowledge the lock and close')
def then_the_program_will_acknowledge_the_lock_and_close(step):
    process_found = False
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
                    process_found = True
    if process_found:
        assert False, "The program is running"
    else:
        assert True, "The program is not running"
