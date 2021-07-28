import os
from oz_cd_config import conf

cwd = os.getcwd()


class Android:

    def __init__(self, config_file=cwd + '/python/oz_cd.cfg'):
        conf.config_filename = config_file
        conf.reload_config()
        # conf.print_config()

    @staticmethod
    def version():
        workspace = conf.config.get_config_string('Android', 'Workspace')
        verProf = conf.config.get_config_string('Android', 'VersionProperties')
        with open(f"{cwd}/python/{workspace}{verProf}", 'r') as f:
            lines = f.readline()
            for line in lines:
                print("A line:", line)
                if 'major' in line:
                    major = line.split('=')[1]
                if 'minor' in line:
                    minor = line.split('=')[1]
                if 'point' in line:
                    point = line.split('=')[1]

        return f"{major}.{minor}.{point}"
