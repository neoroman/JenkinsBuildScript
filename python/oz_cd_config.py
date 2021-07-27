import logging
from configuration import Configuration


class OZConfig():
    config = Configuration()
    def __init__(self, file_name):
        self.config_filename = file_name
        self.config.load_config(file_name)
        logging.info("Config file is %s", file_name)

    def load_config(self):
        self.slack_channel = self.config.get_config_string('Slack', 'SlackChannel', 'default_channel')
        self.slack_enabled = self.config.get_config_bool('Slack', 'SlackEnabled', True)

        self.teams_webhook = self.config.get_config_string('Teams', 'TeamsWebhook', 'default_webhook')
        self.teams_enabled = self.config.get_config_bool('Teams', 'TeamsEnabled', True)

    def reload_config(self):
        self.config.load_config(self.config_filename)
        self.load_config()

    def print_config(self):
        logging.info(f'slack_channel: [{self.slack_channel}]')
        logging.info(f'slack_enabled: [{self.slack_enabled}]')

        logging.info(f'teams_webhook: [{self.teams_webhook}]')
        logging.info(f'teams_enabled: [{self.teams_enabled}]')


def printUsage(arg):
    print('Usage : ' + arg[0] + ' -c [ConfigFile] -d [DBConfigFile]')


conf_filename = './oz_cd.cfg'


print('Config File name: ' + conf_filename)
conf = OZConfig(conf_filename)
conf.load_config()



