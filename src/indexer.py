import json

def index(pages):
    """
    Index the text content of html pages.

    Args:
        pages (dict): A dictionary mapping page URLs to their text content.

    Returns:
        dict: An inverted index mapping words to their occurrences across pages, 
        including frequency and positions for each page.
    """

    index_data = {}

    for url, text in pages.items():
        words = text.lower().split()
        for position, word in enumerate(words):
            if word not in index_data:
                index_data[word] = {url: {"frequency": 1, "positions": [position]}}
            else:
                if url in index_data[word]:
                    index_data[word][url]["frequency"] += 1
                    index_data[word][url]["positions"].append(position)
                else:
                    index_data[word][url] = {"frequency": 1, "positions": [position]}      

    return index_data

def save_index(index_data, filepath):
    """
    Saves the index data to a JSON file on disk. 

    Args:
        index_data (dict): The index data to save.
        filepath (str): The path to the save location.

    Returns:
        None         
    """

    with open(filepath, "w") as f:
        json.dump(index_data, f, indent=4)

def load_index(filepath):
    """
    Loads the index data from a JSON file on disk.

    Args:
        filepath (str): The path to the index file.

    Returns:
        dict: The inverted index laoded from the JSON file.    
    """

    with open(filepath, "r") as f:
        return json.load(f)        