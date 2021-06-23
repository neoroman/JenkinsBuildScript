import os.path
import configparser

config = configparser.ConfigParser()
config_file = "python/angel_cd.cfg"

if os.path.isfile(config_file):
    config.read_file(open(config_file))

    # Slack
    slack_enabled = config.getboolean("Slack", "SlackEnabled")
    slack_channel = config.get("Slack", "SlackChannel")

    # Teams
    teams_enabled = config.getboolean("Teams", "TeamsEnabled")
    teams_webhook = config.get("Teams", "TeamsWebhook")
else:
    # Slack
    config.add_section("Slack")
    config.set('Slack', 'SlackEnabled', 'false')
    config.set('Slack', 'SlackChannel', '')

    # Teams
    config.add_section("Teams")
    config.set('Teams', 'TeamsEnabled', 'false')
    config.set('Teams', 'TeamsWebhook', '')

    # Writing our configuration file to 'angel_cd.cfg'
    with open(config_file, 'w') as configfile:
        config.write(configfile)
