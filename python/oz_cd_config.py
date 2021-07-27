import os.path
import configparser
top_path = os.path.dirname(__file__)


def oz_config(mobile_os, input_file):
    if len(input_file) > 0:
        if os.path.isfile(input_file):
            config_file = input_file
    else:
        if os.path.isfile(top_path + '/oz_cd.cfg'):
            config_file = top_path + "/oz_cd.cfg"

    slack = {}
    teams = {}
    config = configparser.ConfigParser()
    config.file = config_file

    if os.path.isfile(config.file):
        config.read_file(open(config.file))

        # Slack
        slack['Enabled'] = config.getboolean("Slack", "SlackEnabled")
        slack['Channel'] = config.get("Slack", "SlackChannel")
        config.slack = slack

        # Teams
        teams['Enabled'] = config.getboolean("Teams", "TeamsEnabled")
        teams['Webhook'] = config.get("Teams", "TeamsWebhook")
        config.teams = teams

    else:
        # Slack
        config.add_section("Slack")
        config.set('Slack', 'SlackEnabled', 'false')
        config.set('Slack', 'SlackChannel', '')

        # Teams
        config.add_section("Teams")
        config.set('Teams', 'TeamsEnabled', 'false')
        config.set('Teams', 'TeamsWebhook', '')

        # Writing our configuration file to 'oz_cd.cfg'
        with open(config.file, 'w') as configfile:
            config.write(configfile)

    return config
