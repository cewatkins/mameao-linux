from mameao.mame import run_mame
from mameao.xml2db import parse_mame_xml, create_machines_db
import os

def process_operation(arguments):
    op = arguments.get("operation", "").lower()
    if op in ("about", "version"):
        return about_operation(arguments)
    if op == "verifyroms":
        return verifyroms_operation(arguments)
    if op == "makedb":
        return makedb_operation(arguments)
    print(f"[Operations] Unknown operation: {op}")
    return 1

def about_operation(arguments):
    print("MAME-AO Python/Linux Port")
    print("GitHub: https://github.com/sam-ludlow/mame-ao")
    print("This is an in-progress port of the original C# application.")
    return 0

def verifyroms_operation(arguments):
    machine = arguments.get("machine")
    if not machine:
        print("Missing 'machine' argument. Example: machine=pacman")
        return 1
    mame_args = [machine, "-verifyroms"]
    print(f"Running: mame {machine} -verifyroms")
    exit_code, stdout, stderr = run_mame(mame_args)
    print("Exit code:", exit_code)
    print("STDOUT:\n", stdout)
    if stderr:
        print("STDERR:\n", stderr)
    return exit_code

def makedb_operation(arguments):
    """
    Example: python3 -m mameao.main operation=makedb [system=systemname]
    Calls: mame -listxml or mame <system> -listxml and saves output, then parses and stores in SQLite.
    """
    system = arguments.get("system")
    xml_file = arguments.get("xmlfile", "mame_list.xml")
    db_file = arguments.get("dbfile", "mame.db")
    if system:
        mame_args = [system, "-listxml"]
        print(f"Running: mame {system} -listxml")
    else:
        mame_args = ["-listxml"]
        print("Running: mame -listxml")
    exit_code, stdout, stderr = run_mame(mame_args)
    if exit_code != 0:
        print("MAME exited with non-zero code. STDERR:\n", stderr)
        return exit_code
    # Save XML to file
    with open(xml_file, "w", encoding="utf-8") as f:
        f.write(stdout)
    print(f"XML saved to: {xml_file}")
    # Parse XML and create DB
    print("Parsing XML and saving to DB...")
    machines = parse_mame_xml(xml_file)
    create_machines_db(machines, db_file)
    print(f"Database created: {db_file} ({len(machines)} machines)")
    return 0
