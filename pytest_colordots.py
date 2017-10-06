from colorama import init
from colorama import Fore
init()


def pytest_report_teststatus(report):
    if report.when == 'call':
        if hasattr(report, 'wasxfail'):
            if report.skipped:
                return "xfailed", Fore.YELLOW + "x", "xfail"
            elif report.passed:
                return "xpassed", Fore.YELLOW + "p", ("XPASS",
                                                      {'yellow': True})
        if report.passed:
            letter = Fore.GREEN + "."
        elif report.skipped:
            letter = Fore.YELLOW + "s"
        elif report.failed:
            letter = Fore.RED + "F"
        return report.outcome, letter, report.outcome.upper()
