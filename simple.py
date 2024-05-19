def check_code_for_debugger_statements(code):
    """Process code using pycodestyle Checker and return all errors."""
    from tempfile import NamedTemporaryFile

    test_file = NamedTemporaryFile(delete=False)
    test_file.write(code.encode())
    test_file.flush()
    report = CaptureReport(options=_debugger_test_style)
    lines = [line + "\n" for line in code.split("\n")]
    checker = pycodestyle.Checker(filename=test)

    checker.check_all()
    return report._results
