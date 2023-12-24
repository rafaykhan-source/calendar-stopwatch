"""This module represents the settings for the google-stopwatch project.

This module contains a function responsible for retrieving the logging
configuration required for the project.
"""

import yaml


def get_logging_config() -> dict:
    """Returns logging config dictionary from logging_config.yml.

    Returns:
        dict: Logging config dictionary.
    """
    with open("config/logging_config.yml", encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def main() -> None:
    """Unit Testing."""
    print(get_logging_config())
    return


if __name__ == "__main__":
    main()
