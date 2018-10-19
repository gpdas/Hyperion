import yaml
import os.path


# This is a solution provided by Josh Bode in stackoverflow to provide import
# https://stackoverflow.com/questions/528281/how-can-i-include-an-yaml-file-inside-another
class Loader(yaml.SafeLoader):
    """Custom loader class to feature including yaml files inside each other."""

    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)


Loader.add_constructor('!include', Loader.include)
