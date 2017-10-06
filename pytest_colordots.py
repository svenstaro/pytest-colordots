from colorama import init
from colorama import Fore
init()


def pytest_report_teststatus(report):
    if report.when == 'call':
        if hasattr(report, 'wasxfail'):
            if report.skipped:
                return "xfailed", Fore.YELLOW + "x" + Fore.RESET, "xfail"
            elif report.passed:
                return "xpassed", Fore.YELLOW + "p" + Fore.RESET, ("XPASS", {'yellow': True})
        if report.passed:
            letter = Fore.GREEN + "." + Fore.RESET
        elif report.skipped:
            letter = Fore.YELLOW + "s" + Fore.RESET
        elif report.failed:
            letter = Fore.RED + "F" + Fore.RESET
        return report.outcome, letter, report.outcome.upper()
