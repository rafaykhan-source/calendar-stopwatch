import yaml


def get_logging_config() -> dict:
    """Returns logging config dictionary from logging_config.yml.

    Returns:
        dict: Logging config dictionary.
    """
    with open("config/logging_config.yml", encoding="utf-8", mode="r") as file:
        config = yaml.safe_load(file)

    return config


def main() -> None:
    print(get_logging_config())
    return


if __name__ == "__main__":
    main()
