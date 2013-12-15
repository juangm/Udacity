# Testing coverage of the file: SplayTree_Test.py
import coverage
cov = coverage.coverage()
cov.start()

import SplayTree_Test
SplayTree_Test.test()

cov.stop()
cov.save()
cov.html_report()