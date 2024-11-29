from src.modify import json_to_csv
from src.scrape import download_files


def main():
    urls = [
        "https://keskkonnaandmed.envir.ee/t_awvorm_001_curr"
    ]

    download_files(urls, "data")
    json_to_csv("data/t_awvorm_001_curr.json", "output")


if __name__ == "__main__":
    main()