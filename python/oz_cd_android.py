import os
from oz_cd_config import conf


class Android:
    cwd = os.getcwd()

    def __init__(self, config_file=cwd + '/python/oz_cd.cfg'):
        conf.config_filename = config_file
        conf.reload_config()
        conf.print_config()

