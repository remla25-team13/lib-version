from lib_version.version_util import VersionUtil

def test_get_version_returns_str():
    version = VersionUtil.get_version()
    assert isinstance(version, str)
    assert len(version) > 0