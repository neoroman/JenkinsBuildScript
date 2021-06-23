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
#  1. Install slack from "https://github.com/rockymadden/slack-cli" (also use "brew install rockymadden/rockymadden/slack-cli"), run "slack init", and Enter Slack API token from https://api.slack.com/custom-integrations/legacy-tokens
#  2. Install jq path with "/usr/local/bin/jq" in "/usr/local/bin/slack"
#  3. Install a2ps via HomeBrew, brew install a2ps
#  4. Install gs via HomeBrew, brew install gs
#
import sys
import logging
import subprocess
import argparse


# import requests
################################################################################
# Check environments
parser = argparse.ArgumentParser(description="Hello, I'm Jenkins Bot !!!")
parser.add_argument("-l", "--list",
                    help="Create CSV of images",
                    action="store_true")
parser.add_argument("-d", "--dimensions",
                    help="Copy images with incorrect dimensions to new directory",
                    action="store_true")
parser.add_argument("-i", "--interactive",
                    help="Run script in interactive mode",
                    action="store_true")
args = parser.parse_args()

if len(sys.argv) == 1:
    # display help message when no args are passed.
    parser.print_help()
    sys.exit(1)

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logging.debug("Main:", sys.argv)  # check input arguments

################################################################################
# External commands and installations if not exist
from external_command import *
#subprocess.run([cmd_jq, "-h"])  # run external command

################################################################################
# Declaration


################################################################################
# Check path of file and directory and cope with them
from angel_cd_config import *

print("Config sections:", config.sections())
print("Slack:", slack_channel)
print("Slack Enabled:", slack_enabled)
print("Teams:", teams_webhook)
print("Teams Enabled:", teams_enabled)

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


################################################################################
# Report to slack, email, ... etc


# test `matplotlib`
# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()                   # Display the plot

# test from curl
# headers = {
#     'Content-Type': 'application/json',
# }
# data = {
#   '{"themeColor":"0076D7","summary":"UANGEL Jira Issue Notifications""sections":[{"activityTitle":"[UA-41] Key is Compressed?!? WTFWTFWTFWTFWTWFWTF!!!!!!!!","activitySubtitle":"h3. \uBA54\uC778 \uD654\uBA74\uC744 \uAD6C\uC131\uD558\uB294\uB370 \uB124\uD2B8\uC6CC\uD06C \uC2DC\uAC04\uB3D9\uC548\uC740 placeholder \uD654\uBA74\uACFC \uAC19\uC774 blurring effect \uB97C \uC0AC\uC6A9\uD558\uC5EC \uAD6C\uD604\uD55C\uB2E4.\\r\\n\\r\\n!AngelNet.app - 03_MainView@2x.png|thumnail!\\r\\n!AngelNet.app - 02_MainView_Placeholder@2x.png|thumnail!","activityImage":"http://jira.svcdiv.uangel.com/secure/project/EditProject!default.jspa?pid': '10315#","facts":[{"name":"Issue type","value":""},{"name":"Project","value":""},{"name":"Label","value":"Array"},{"name":"Component","value":"Array"}],"markdown":true}],"@type":"MessageCard","@context":"http://jira.svcdiv.uangel.com/rest/api/2/issue/24691"}'
# }
# response = requests.post('https://uangel.webhook.office.com/webhookb2/57dae0bf-abb2-43df-b7c1-73121c5a75a4@13a84ba8-5a74-4cdf-a639-57395cf71a8f/IncomingWebhook/9aa4021828da4535b0825b9bfd14ae68/a9b785d5-fbf6-4857-add7-dc64d1dd64c1', headers=headers, data=data)
# print(response)
