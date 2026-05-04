from crawler import crawl
from indexer import index, save_index, load_index
from search import print_results, find_word

BASE_URL = "https://quotes.toscrape.com"
INDEX_FILEPATH = "data/index.json"

def main():
    """
    Runs the command-line interface for the search engine tool.

    Accepts the following commands:
    - build: Crawls the website and builds the inverted index.
    - load: Loads the inverted index from the file system.
    - print: Prints the index entry for a given word.
    - find: Finds pages containing one or more search terms.
    - quit: Exits the program.
    """

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
                if len(parts) < 2:
                    print("Please provide a word to print.")
                    continue
                if index_data is None:
                    print("No index found. Please run 'build' or 'load' first.")
                    continue
                print_results(index_data, parts[1])                  

            case "find":
                if len(parts) < 2:
                    print("Please provide a word to find.")
                    continue    
                if index_data is None:
                    print("No index found. Please run 'build' or 'load' first.")
                    continue

                query = " ".join(parts[1:])
                results = find_word(index_data, query)
                if results:
                    print(f"Pages containing '{query}':")
                    for url in results:
                        print(f"-   {url}")

            case "quit":
                print("Exiting search tool.")
                break

            case _:
                print("Unknown command. Use: build, load, print, find, quit")

if __name__ == "__main__":
    main()