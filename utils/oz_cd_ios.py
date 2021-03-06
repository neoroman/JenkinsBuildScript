import os
from utils.oz_cd_config import conf

cwd = os.getcwd()


class iOS:

    def __init__(self, config_file=cwd + '/utils/oz_cd.cfg'):
        conf.config_filename = config_file
        conf.reload_config()
        conf.print_config()

    def version(self):
        workspace = conf.config.get_config_string('iOS', 'Workspace')
        verProf = conf.config.get_config_string('iOS', 'VersionProperties')
        with open(f"{cwd}/{workspace}{verProf}", 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if 'major' in line:
                    major = line.split('=')[1]
                if 'minor' in line:
                    minor = line.split('=')[1]
                if 'point' in line:
                    point = line.split('=')[1]

        return f"{major}.{minor}.{point}"

    def build(self):
        workspace = conf.config.get_config_string('iOS', 'Workspace')
        gradle = conf.config.get_config_string('iOS', 'BuildGradle')
        with open(f"{cwd}/{workspace}{gradle}", 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if 'build' in line:
                    build = line.split(' ')[1]

        return f"{build}"
