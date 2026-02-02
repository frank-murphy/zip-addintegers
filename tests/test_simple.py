
"""
test cases for addintegers command line tool
"""

import subprocess

def run_add_integers(*args):
    """Run addintegers with args on command line, return output & exit code """
    completed_process = subprocess.run(["./addintegers"] + list(args),
        capture_output = True, text = True, check = False)
    return completed_process.stdout.strip(), completed_process.returncode

# Test cases
def test_add3():
    """Add three integers"""
    output, exitcode = run_add_integers("1", "2", "9")
    assert output == "12"
    assert exitcode == 0

def test_add_one_and_one():
    """Add 1 + 1 to get 2"""
    output, exitcode = run_add_integers("1", "1")
    assert output == "2"
    assert exitcode == 0

def test_neg_null_arg():
    """Negative:  no input means no output and non-0 exit code"""
    output, exitcode = run_add_integers()
    assert output == ""
    assert exitcode != 0

def test_git_status():
    """Print git status"""
    completed_process = subprocess.run(["git", "status"],
        capture_output = True, text = True, check = False)
    output, exitcode = completed_process.stdout.strip(), completed_process.returncode
    output = output.splitlines()
    assert output[0] != "On branch main" # This will fail when on git main
    assert exitcode == 0
