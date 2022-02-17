from colores import colorized_print, RED, MAGENTA, YELLOW
import subprocess

tests = [
    {
        "input": """7
1
.
1
B
1
R
2
BR
BB
4
BBBB
BBB.
RRR.
RRRR
4
BBBB
BBBB
RRR.
RRRR
6
......
..R...
BBBBBB
..R.R.
..RR..
......""",
        "output": """Case #1: Nobody wins
Case #2: Blue wins
Case #3: Red wins
Case #4: Impossible
Case #5: Blue wins
Case #6: Impossible
Case #7: Blue wins""",
    }
]


for index, test in enumerate(tests):
    result = subprocess.getoutput(f"echo '{test['input']}' | python challenge.py ")

    if result == test["output"]:
        colorized_print("[OK]")
        exit()

    colorized_print(f"\n[FAIL: TEST {index}]", RED)

    colorized_print("\nExpected:", YELLOW)

    colorized_print(f"\n{test['output']}\n", MAGENTA)

    colorized_print("\nGot:", YELLOW)

    colorized_print(f"\n{result}\n", MAGENTA)
