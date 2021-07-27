import platform
import sys
import logging
import os.path
from subprocess import run, PIPE

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)  # stream=sys.stderr,


class Commands:
    os_name = platform.system()
    system_info = platform.platform()

    logging.debug("OS name: %s", os_name)
    logging.debug("System info: %s", system_info)

    if os_name == 'Darwin':
        brew = run(['which', 'brew'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True).stdout.rstrip('\n')

    if not os.path.isfile(brew):
        logging.debug("File not exist: %s", brew)

    logging.info("External Command Argument: %s", sys.argv)

    if platform == 'ios':
        lipo = run(['which', 'lipo'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True).stdout.rstrip('\n')
        if not os.path.isfile(lipo):
            logging.warning("File not exist: %s", lipo if len(lipo) > 0 else "/usr/bin/lipo")

    xcode = run(['which', 'xcodebuild'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True).stdout.rstrip(
        '\n')
    if not os.path.isfile(xcode):
        logging.warning("File not exist: %s", xcode if len(xcode) > 0 else "/usr/bin/xcodebuild")

    pod = run(['which', 'pod'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True).stdout.rstrip('\n')
    if not os.path.isfile(pod):
        logging.warning("File not exist: %s, Install CocoaPods from https://cocoapods.org first",
                        pod if len(pod) > 0 else "/usr/local/bin/pod")

    zip = run(['which', 'zip'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True).stdout.rstrip('\n')
    if not os.path.isfile(zip):
        logging.debug("File not exist: %s", zip if len(zip) > 0 else "/usr/bin/zip")

    slack = run(['which', 'slack'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True).stdout.rstrip('\n')
    if not os.path.isfile(slack):
        logging.debug("File not exist: %s", slack if len(slack) > 0 else "/usr/local/bin/slack")

    a2ps = run(['which', 'a2ps'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True).stdout.rstrip('\n')
    if not os.path.isfile(a2ps):
        logging.debug("File not exist: %s", a2ps if len(a2ps) > 0 else "/usr/local/bin/a2ps")

    gs = run(['which', 'gs'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True).stdout.rstrip('\n')
    if not os.path.isfile(gs):
        logging.debug("File not exist: %s", gs if len(gs) > 0 else "/usr/local/bin/gs")

    convert = run(['which', 'convert'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True).stdout.rstrip(
        '\n')
    if not os.path.isfile(convert):
        logging.debug("File not exist: %s", convert if len(convert) > 0 else "/usr/local/bin/convert")

    curl = run(['which', 'curl'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True).stdout.rstrip('\n')
    if not os.path.isfile(curl):
        logging.debug("File not exist: %s", curl if len(curl) > 0 else "/usr/bin/curl")

