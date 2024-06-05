import subprocess
import time
import os


def execute_script(script_path, args, report_path):
    start = time.time()
    process = subprocess.Popen(
        ["python", script_path] + args, stdout=subprocess.PIPE, cwd=os.getcwd(), stderr=subprocess.PIPE)
    print(f"Executing {script_path} with args {args}")
    stdout, stderr = process.communicate(input=b'\n')
    execution_time = time.time() - start

    with open(report_path, 'w') as report_file:
        report_file.write(f"Execution time: {execution_time} seconds\n")
        report_file.write("Output:\n")
        report_file.write(stdout.decode())
        if stderr:
            report_file.write("\nErrors:\n")
            report_file.write(stderr.decode())


if __name__ == "__main__":
    execute_script("game.py", ["-p", "tiny_set.txt", "-f",
                   "bfs", "-s", "4", "7", "-z", "fill"], "report.txt")
    execute_script("game.py", ["-p", "tiny_set.txt",
                   "-s", "4", "7", "-z", "fill"], "report.txt")
