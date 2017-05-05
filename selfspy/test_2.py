from subprocess import check_output
import stats
import os

output = check_output("chromix-too ls active | awk '{print$2}'", shell=True)

#print output

new_output = check_output("selfstats")

if "https://twitter.com/" in new_output:
    print "Yeah its there"

print check_output("selfstats")

