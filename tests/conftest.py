"""Configuration for pytest."""


def pytest_configure(config):
    """Configure pytest.

    Args:
        config: pytest config
    """
    config.addinivalue_line("markers", "ask: mark as user ask test.")
