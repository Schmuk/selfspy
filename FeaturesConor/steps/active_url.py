from lettuce import step, world
from subprocess import check_output
url_I_want_to_see = "https://twitter.com/"

@step("I have been running selfspy and using Google Chrome")
def step_impl(step):
    pass

@step(u'When I enter the "([^"]*)" command')
def when_i_enter_the_selfstats_command(step, my_command):
    world.my_command = check_output("selfstats")


@step("I should see the the active tab urls in the ouput")
def step_impl(step):
    if url_I_want_to_see in world.my_command:
        assert True
    else:
        assert False



