import os
from utils.oz_cd_config import conf


class iOS:
    cwd = os.getcwd()

    def __init__(self, config_file=cwd + '/utils/oz_cd.cfg'):
        conf.config_filename = config_file
        conf.reload_config()
        conf.print_config()

