from lettuce import step
import os
program_name = "Google-chrome"

@step(u'Google chrome is open')
def given_i_have_an_active_browser(step):
    try:
        os.system(program_name)
    except OSError:
        assert False, program_name + ' is not running'
    assert True, "command ran successfully"
@step(u'When selfstats is ran')
def when_selfstats_is_ran(step):
    assert False, 'This step must be implemented'
@step(u'Then the URL will be in the output')
def then_the_url_will_be_in_the_output(step):
    assert False, 'This step must be implemented'


'''

@step(u'Given I have an active browser')
def given_i_have_an_active_browser(step):
    assert False, 'This step must be implemented'
@step(u'When selfstats is ran')
def when_selfstats_is_ran(step):
    output = os.system("selfstats --showtext")
@step(u'Then the URL will be in the output')
def then_the_url_will_be_in_the_output(step):
    if 'site' in output:
        return 'it's there'


'''
# os.system("selfstats --showtext")
