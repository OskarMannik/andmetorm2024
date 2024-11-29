from src.modify import json_to_csv
from src.scrape import download_files


def main():
    urls = [
        # Pinnavee võtt
        "https://keskkonnaandmed.envir.ee/t_awtabel002_02_curr",
        # Veekasutus
        "https://keskkonnaandmed.envir.ee/t_awtabel004_curr"
    ]

    download_files(urls, "data")
    json_to_csv("data/t_awtabel002_02_curr.json", "output")


if __name__ == "__main__":
    main()
