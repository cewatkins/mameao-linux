def console_heading(level, messages):
    print("\n" + ("=" * (level * 2)))
    for msg in messages:
        print(msg)
    print("=" * (level * 2) + "\n")
    # TODO: Add more shared utility functions as needed

# Example for downloading files (used in asset/artwork/sample features)
import requests

def download_file(url, dest):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Downloaded: {url} -> {dest}")
