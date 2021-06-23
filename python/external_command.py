import sys
import logging
import os.path

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logging.debug("External Command Argument:", sys.argv)

cmd_lipo = "/usr/bin/lipo"
if os.path.isfile(cmd_lipo):
    logging.debug("File exist:", cmd_lipo, os.path.getsize(cmd_lipo))
else:
    logging.debug("File not exist:", cmd_lipo)

cmd_xcode = "/usr/bin/xcodebuild"
if os.path.isfile(cmd_xcode):
    logging.debug("File exist:", cmd_xcode, os.path.getsize(cmd_xcode))
else:
    logging.debug("File not exist:", cmd_xcode)

cmd_zip = "/usr/bin/zip"
if os.path.isfile(cmd_zip):
    logging.debug("File exist:", cmd_zip, os.path.getsize(cmd_zip))
else:
    logging.debug("File not exist:", cmd_zip)

cmd_slack = "/usr/local/bin/slack"
if os.path.isfile(cmd_slack):
    logging.debug("File exist:", cmd_slack, os.path.getsize(cmd_slack))
else:
    logging.debug("File not exist:", cmd_slack)

cmd_a2ps = "/usr/local/bin/a2ps"
if os.path.isfile(cmd_a2ps):
    logging.debug("File exist:", cmd_a2ps, os.path.getsize(cmd_a2ps))
else:
    logging.debug("File not exist:", cmd_a2ps)

cmd_gs = "/usr/local/bin/gs"
if os.path.isfile(cmd_gs):
    logging.debug("File exist:", cmd_gs, os.path.getsize(cmd_gs))
else:
    logging.debug("File not exist:", cmd_gs)

cmd_convert = "/usr/local/bin/convert"
if os.path.isfile(cmd_convert):
    logging.debug("File exist:", cmd_convert, os.path.getsize(cmd_convert))
else:
    logging.debug("File not exist:", cmd_convert)

cmd_curl = "/usr/bin/curl"
if os.path.isfile(cmd_curl):
    logging.debug("File exist:", cmd_curl, os.path.getsize(cmd_curl))
else:
    logging.debug("File not exist:", cmd_curl)

cmd_jq = "/usr/local/bin/jq"
if os.path.isfile(cmd_jq):
    logging.debug("File exist:", cmd_jq, os.path.getsize(cmd_jq))
else:
    logging.debug("File not exist:", cmd_jq)

cmd_pod = "/usr/local/bin/pod"
if os.path.isfile(cmd_pod):
    logging.debug("File exist:", cmd_pod, os.path.getsize(cmd_pod))
else:
    logging.debug("File not exist:", cmd_pod)
