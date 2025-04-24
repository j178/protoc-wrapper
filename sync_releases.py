import logging
import os
import time

import pendulum
import requests

from make_wheels import to_pypi_version, write_wheels

session = requests.Session()


def get_pypi_versions(package: str) -> list[str]:
    url = f"https://pypi.org/pypi/{package}/json"
    resp = session.get(url)
    data = resp.json()
    versions = data["releases"].keys()
    return list(versions)


def get_latest_releases() -> list[str]:
    url = "https://api.github.com/repos/protocolbuffers/protobuf/releases"
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token := os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"

    page = 1
    releases = []
    while True:
        resp = session.get(url, params={"page": page}, headers=headers)
        data = resp.json()
        if not data:
            break

        for release in data:
            published_at = pendulum.parse(release["published_at"])
            if published_at < pendulum.now().subtract(days=7):
                continue
            releases.append(release["tag_name"])

        page += 1
        if len(data) < 30:
            break
        time.sleep(0.2)

    return releases


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    releases = get_latest_releases()
    logging.info(f"Latest releases: {releases}")

    pypi_versions = get_pypi_versions("protoc-wrapper")
    logging.info(f"PyPI versions: {pypi_versions}")
    pypi_versions = set(pypi_versions)

    for release in releases:
        version = to_pypi_version(release)
        if version not in pypi_versions:
            logging.info(f"Sync release {version} to PyPI")
            write_wheels(outdir="dist/", tag=release)


if __name__ == "__main__":
    main()
