from blessings import Terminal

t = Terminal()

def pytest_report_teststatus(report):
    if report.when == 'call':
        if hasattr(report, 'wasxfail'):
            if report.skipped:
                return "xfailed", t.yellow(u"x"), "xfail"
            elif report.failed:
                return "xpassed", t.yellow("p"), "XPASS"
        if report.passed:
            letter = t.green(u".")
        elif report.skipped:
            letter = t.yellow(u"s")
        elif report.failed:
            letter = t.red(u"F")
        return report.outcome, letter, report.outcome.upper()
