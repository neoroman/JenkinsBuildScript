import os
from utils.oz_cd_config import conf

cwd = os.getcwd()


class Android:

    def __init__(self, config_file=cwd + '/utils/oz_cd.cfg'):
        conf.config_filename = config_file
        conf.reload_config()
        # conf.print_config()

    @staticmethod
    def version():
        workspace = conf.config.get_config_string('Android', 'Workspace')
        verProf = conf.config.get_config_string('Android', 'VersionProperties')
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

    @staticmethod
    def version_code():
        workspace = conf.config.get_config_string('Android', 'Workspace')
        gradle = conf.config.get_config_string('Android', 'BuildGradle')
        with open(f"{cwd}/{workspace}{gradle}", 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if 'versionCode' in line:
                    versionCode = line.split(' ')[1]

        return f"{versionCode}"