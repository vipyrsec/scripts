"""Download GitHub repos from search query in bulk."""

import requests


def run(topics: list[str]) -> None:
    """get repos"""
    params = {"q": " ".join(f"topic:{topic}" for topic in topics)}
    response = requests.get("https://api.github.com/search/repositories", params=params)
    for item in response.json()["items"]:
        print("dowloading:", item["full_name"])
        repo_name = item["full_name"].replace("/", "--")
        zipball_url = item["archive_url"].replace("{archive_format}{/ref}", f"zipball/{item['default_branch']}")
        repo_zip_bytes = requests.get(zipball_url).content
        with open(f"{repo_name}.zip", "wb") as file:
            file.write(repo_zip_bytes)


if __name__ == '__main__':
    run(topics=["ecs", "go"])
