import subprocess

def run_mame(arguments, cwd=None):
    """
    Run the 'mame' binary with the given arguments.
    Returns (exit_code, stdout, stderr)
    """
    cmd = ['mame'] + arguments
    try:
        process = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=False)
        return process.returncode, process.stdout, process.stderr
    except FileNotFoundError:
        print("Error: 'mame' binary not found in PATH.")
        return -1, '', 'mame not found'
    except Exception as e:
        print(f"Error running mame: {e}")
        return -1, '', str(e)
