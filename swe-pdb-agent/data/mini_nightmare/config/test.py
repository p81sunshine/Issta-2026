import pytest

from config_code import ConfigManager


@pytest.fixture(autouse=True)
def clear_cache():
    # Clear the cache before each test
    ConfigManager._cached_configs = {}
    yield
    # Clear the cache after each test
    ConfigManager._cached_configs = {}


def test_config_updates():
    # Create initial config
    config = ConfigManager({
        'database': {
            'host': 'initial-host',
            'port': 5432
        }
    })

    # First access creates cached value
    initial_db = config.database
    assert initial_db.host == 'initial-host'

    # Update the configuration
    config.set('database', {
        'host': 'new-host',
        'port': 5432
    })

    # This should return the new value but will return cached value
    assert config.database.host == 'new-host'


def test_multiple_instances():
    config1 = ConfigManager({
        'database': {'host': 'host1'}
    })
    config2 = ConfigManager({
        'database': {'host': 'host2'}
    })

    # Access both configs
    _ = config1.database
    _ = config2.database

    # Update first config
    config1.set('database', {'host': 'new-host'})

    # Access both configs again
    # Due to shared cache, this might affect both instances
    assert config1.database.host == 'new-host'
    assert config2.database.host == 'host2'