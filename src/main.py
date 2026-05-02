from crawler import crawl
from indexer import index, save_index, load_index

BASE_URL = "https://quotes.toscrape.com"
INDEX_FILEPATH = "data/index.json"

def main():
    index_data = None 

    while True:
        command = input("> ").strip()
        parts = command.split()

        if not parts:
            print("Please enter a command.")
            continue

        match parts[0]:
            case "build":
                print("Crawling website...")
                pages = crawl(BASE_URL)
                print("Indexing pages...")
                index_data = index(pages)
                save_index(index_data, INDEX_FILEPATH)
                print(f"Index built and saved to {INDEX_FILEPATH}")

            case "load":
                try:
                    index_data = load_index(INDEX_FILEPATH)
                    print(f"Index loaded from {INDEX_FILEPATH}")
                except FileNotFoundError:
                    print("No index found. Please run 'build' first.")

            case "print":
                pass

            case "find":
                pass

            case "quit":
                print("Exiting search tool.")
                break

            case _:
                print("Unknown command. Use: build, load, print, find, quit")

if __name__ == "__main__":
    main()