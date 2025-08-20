#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#                                                                                                                              
#                                                                                                                              #
#       Welcome to the NettravelerEX project! Originally written in Lua, the main parts of the codebase have been              #
#       rewritten in Python to make it easier to find new contributors and employees for the Cosmic Sec&Dev company.           #
#                                                                                                                              #
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#

import subprocess
import sys
import pytest

@pytest.mark.parametrize("args, expected", [
    (["map.local", "--output_mode_html"], "<span><span style="),
    (["map.local", "--output_mode_none"], "[exec] :: map.local"),
    (["map.local"], "[exec] :: map.local"),
])
def test_netex_output(args, expected):
    cmd = [sys.executable, "nettraveler.py"] + args
    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    assert expected in result.stdout, (
        f"Expected '{expected}' in output, but got:\n{result.stdout}"
    )

def test_netex_with_random_argument():
    random_arg = "�{�{�{$8`|`|`|�8880hhhDDS�td8880P�tdPiPiPi��Q�tdR�td�{�{�"  # generates a random string
    cmd = [sys.executable, "nettraveler.py", random_arg]
    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    assert result.returncode != 0, "Expected non-zero exit code for invalid argument."

    assert '' in result.stdout.lower(), (
        f"Expected default message:\n{result.stdout}"
    )