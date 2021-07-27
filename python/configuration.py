import configparser


class Configuration:

    def __init__(self):
        self.config = configparser.ConfigParser()

    def load_config(self, fileName):
        self.config.read(fileName)

    def get_config_string(self, *args) : 
        if not args:
            return ''
        if len(args) < 3:
            try:
                return self.config.get(args[0], args[1])
            except:
                return ''
        else:
            try:
                return self.config.get(args[0], args[1])
            except:
                return args[2]    # return default value

    def get_config_integer(self, *args):
        if not args: return 0
        if len(args) < 3:
            try:
                return self.config.getint(args[0], args[1])
            except:
                return 0
        else:
            try:
                return self.config.getint(args[0], args[1])
            except:
                return int(args[2])    # return default value

    def get_config_bool(self, *args):
        if not args:
            return True
        if len(args) < 3:
            try:
                return self.config.getboolean(args[0], args[1])
            except:
                return True
        else:
            try:
                return self.config.getboolean(args[0], args[1])
            except:
                return bool(args[2])    # return default value
         
    def get_config_list(self, *args):
        if not args:
            return ''
        try:
            value = self.config.get(args[0], args[1])
        except:
            return []

        return value.split(',')
      

