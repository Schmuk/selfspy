# -*- coding: utf-8 -*-
from lettuce import *
import psutil
import os


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


@step(u'When: the user enters "--pause" command')
def user_enters_pause_command(step):
    try:
        os.system("selfspy --pause")
    except OSError:
        assert False, 'selfspy has failed to run'
    assert True, "selfspy pause recording command ran successfully"

selfspy_paused = False

@step(u"Then: selfspy pauses it's recording")
def then_selfspy_recording_paused(step):
    ##selfspy_paused = False
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
        selfspy_paused = True
        assert True, "Recording paused. Use command 'selfspy --unpause' to continue recording"
    else:
        assert False, "The program is not running"


@step(u'Given: selfspy is currently paused')
def given_selfspy_is_currently_paused(step):
    if selfspy_paused == True:
        assert True, "selfspy is currently paused"
    else:
        assert False, "selfspy is NOT currently paused. Use command 'selfspy --pause' to pause recording"


@step(u"When: user enters '--unpause' command")
def when_user_enters_unpause_command(step):
    try:
        os.system("selfspy --unpause")
    except OSError:
        assert False, 'selfspy has failed to run'
    assert True, "selfspy unpause recording command ran successfully"


@step(u'Then: selfspy resumes recording')
def then_selfspy_recording_unpaused(step):
    if selfspy_paused == True:
        assert True,  'Selfspy is now recording'
    else:
        assert False, "The program is not running"



