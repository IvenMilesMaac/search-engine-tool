def print_results(index_data, query):
    """
    Prints the inverted index entry for a given word, showing each page it appears on
    along with wits frequency and positions.

    Args:
        index_data (dict): The inverted index data.
        query (str): The word to look up in the index.

    Returns:
        None
    """

    query = query.lower()
    if query not in index_data:
        print(f"No results found for '{query}'.")
        return None

    results = index_data[query]
    for url, stats in results.items():
        print(f"URL: {url}")
        print(f"    Frequency: {stats['frequency']}")
        print(f"    Positions: {stats['positions']}")

def find_word(index_data, query):
    """
    Searches for pages containing all words contained in the query and returns a set of URLs where they appear.

    Args:
        index_data (dict): The inverted index data.
        query (str): The words to search for across the inverted index.

    Returns:
        set: A set of URLs where the search terms appear.
        None: If no results are found or if the query is empty. 
    """

    query = query.lower().split()
    if not query:
        print("No search terms provided.")
        return None
    for word in query:
        if word not in index_data:
            print(f"No results found for '{word}'.")
            return None
        
    results = set(index_data[query[0]].keys())
    
    for word in query[1:]:
        results &= set(index_data[word].keys())
    if not results:
        print(f"No pages found containing all search terms.")
        return None        

    return results        