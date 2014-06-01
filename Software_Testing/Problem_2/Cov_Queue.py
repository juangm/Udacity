# Testing coverage of the file: Queue_Test.py
# Author: Juan Garcia
import coverage
cov = coverage.coverage()
cov.start()

import Queue_Test
Queue_Test.test()

cov.stop()
cov.save()
cov.html_report()
