import importlib.metadata

class VersionUtil:
    @staticmethod
    def get_version():
        return importlib.metadata.version("lib-version")