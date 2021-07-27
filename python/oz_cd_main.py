#!/usr/bin/env python3
##
# pip install -r requirements.txt
##
# Script for Android preRelease Build on Jenkins - http://mini.company.com/job/AppV3-AOS_preRelease
# Written by Henry Kim on 5/22/2018
# Modified by Henry Kim on 2019.06.19 referenced from jenkins-shell-AOS-preRelease.sh
# Porting by Henry Kim on 2021.06.23
#
# Prerequisites for executing this script
#  1. Install slack from "https://github.com/rockymadden/slack-cli"
#     (also use "brew install rockymadden/rockymadden/slack-cli"),
#      run "slack init", and Enter Slack API token from https://api.slack.com/custom-integrations/legacy-tokens
#  2. Install jq path with "/usr/local/bin/jq" in "/usr/local/bin/slack"
#  3. Install a2ps via HomeBrew, brew install a2ps
#  4. Install gs via HomeBrew, brew install gs
#
import subprocess
# import requests
import sys
import os.path
import json
from ext_commands import Commands, logging
from oz_cd_config import conf

import argparse

################################################################################
# Check environments
parser = argparse.ArgumentParser(description="Hello, I'm Jenkins Bot !!!")
parser.add_argument("-p", "--platform", choices=['ios', 'android'],
                    help="Assign platform as ios or android to process jenkins' build",
                    nargs=1,
                    type=str)
parser.add_argument("-c", "--config",
                    help="Assign configuration file, default file in ~/.ozlab/oz_cd.cfg",
                    nargs=1,
                    type=str)
parser.add_argument("-i", "--interactive",
                    help="Run script in interactive mode",
                    action="store_true")
args = parser.parse_args()

top_path = os.path.dirname(__file__)


def main():
    if len(sys.argv) == 1:
        # display help message when no args are passed.
        parser.print_help()
        sys.exit(1)

    logging.debug("Main arguments: %s", args)  # check input arguments
    mobile_os = ""

    if args.platform:
        mobile_os = args.platform[0]
        if mobile_os == 'android':
            logging.debug("Platform(android?): %s", mobile_os)
        else:
            logging.debug("Platform(ios?): %s", mobile_os)

    ################################################################################
    # External commands and installations if not exist
    command = Commands()
    subprocess.run([command.curl, "--version"])  # run external command

    ################################################################################
    # Declaration

    ################################################################################
    # Check path of file and directory and cope with them
    if args.config and os.path.isfile(args.config[0]):
        conf.load_config(args.config[0])
    else:
        conf.load_config()

    conf.reload_config()
    # conf.print_config()

    # x = int(input("Please enter an integer: "))
    # if x < 0:
    #     x = 0
    #     print('Negative changed to zero')
    # elif x == 0:
    #     print('Zero')
    # elif x == 1:
    #     print('Single')
    # else:
    #     print('More')

    ################################################################################
    # Run gradlew for android, run xcodebuild for ios

    ################################################################################
    # Run extra work with output APK or IPA files

    ################################################################################
    # Create HTML file and JSON file for distribution site
    if os.path.isfile(top_path + '/gapp3_3.3.0(527)_210723.json'):
        with open(top_path + '/gapp3_3.3.0(527)_210723.json') as json_file:
            json_data = json.load(json_file)
            print(json_data['title'], json_data['appVersion'], json_data['urlPrefix'])

    ################################################################################
    # Report to slack, email, ... etc

    # test from curl
    # headers = {
    #     'Content-Type': 'application/json',
    # }
    # data = {
    #   '{"themeColor":"0076D7","summary":"OZLAB Jira Issue Notifications""sections":[{"activityTitle":"[OZ-41] Key is Compressed?!? WThe","activitySubtitle":"h3. \uBA54\uC778 \uD654\uBA74\uC744 \uAD6C\uC131\uD558\uB294\uB370 \uB124\uD2B8\uC6CC\uD06C \uC2DC\uAC04\uB3D9\uC548\uC740 placeholder \uD654\uBA74\uACFC \uAC19\uC774 blurring effect \uB97C \uC0AC\uC6A9\uD558\uC5EC \uAD6C\uD604\uD55C\uB2E4.\\r\\n\\r\\n!ozNet.app - 03_MainView@2x.png|thumnail!\\r\\n!ozNet.app - 02_MainView_Placeholder@2x.png|thumnail!","activityImage":"http://jira.svcdiv.ozlab.com/secure/project/EditProject!default.jspa?pid': '10315#","facts":[{"name":"Issue type","value":""},{"name":"Project","value":""},{"name":"Label","value":"Array"},{"name":"Component","value":"Array"}],"markdown":true}],"@type":"MessageCard","@context":"http://jira.svcdiv.ozlab.com/rest/api/2/issue/24691"}'
    # }
    # response = requests.post('https://ozlab.webhook.office.com/webhookb2/57dae0bf-abb2-43df-b7c1-73121c5a75a4@13a84ba8-5a74-4cdf-a639-57395cf71a8f/IncomingWebhook/9aa4021828da4535b0825b9bfd14ae68/a9b785d5-fbf6-4857-add7-dc64d1dd64c1', headers=headers, data=data)
    # print(response)


if __name__ == '__main__':
    main()
