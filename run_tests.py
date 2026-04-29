import unittest
import HtmlTestRunner

if __name__ == '__main__':
    suite = unittest.TestLoader().discover('tests', pattern='test_*.py')
    runner = HtmlTestRunner.HTMLTestRunner(output='reports', report_name='tests_report', combine_reports=True, verbosity=2)
    runner.run(suite)