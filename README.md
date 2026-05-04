# Search Engine Tool

## Overview

A command-line search engine tool that crawls a target website, builds an inverted index of all word occurrences, and allows users to search for words across all pages.

Built for [quotes.toscrape.com](https://quotes.toscrape.com) as part of COMP3011 Web Services and Web Data.

## Installation

1. Clone the repository:
```bash
    git clone https://github.com/IvenMilesMaac/search-engine-tool.git
    cd search-engine-tool
```

2. Create and activate a virtual environment:
```bash
    python3 -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
    pip install -r requirements.txt
``` 
Dependencies: `requests`, `beautifulsoup4`

---

## Usage

Run the tool:
```bash
    venv/bin/python src/main.py
    >
```

Then use the following commands:

**build** - Crawls the website and builds the index:
```bash
    > build
    Crawling website...
    Indexing pages...
    Index built and saved to data/index.json
```

**load** - Loads the index from data/index.json:
```bash
    > load
    Index loaded from data/index.json
```

**print** - Prints the index data of that word:
```bash
    > print life
    URL: https://quotes.toscrape.com/page/1/
        Frequency: 3
        Positions: [92, 193, 266]
    URL: https://quotes.toscrape.com/page/2/
        Frequency: 7
        Positions: [8, 216, 464, 497, 565, 584, 597]
    ...                
```

**find** - Find pages containing a word or phrase: 
```bash
    > find world
    Pages containing 'world':
    -   https://quotes.toscrape.com/page/8/
    -   https://quotes.toscrape.com/page/9/
    -   https://quotes.toscrape.com/page/6/
    -   https://quotes.toscrape.com/page/1/
    > find good friends
    Pages containing 'good friends':
    -   https://quotes.toscrape.com/page/1/
    -   https://quotes.toscrape.com/page/7/
    -   https://quotes.toscrape.com/page/2/
    -   https://quotes.toscrape.com/page/3/
```

**quit** - Exit the program:
```bash
    > quit
    Exiting search tool.
```

---

## Testing

Run all tests:
```bash
    venv/bin/python -m unittest discover tests/ -v
```

Expected output:
```bash
    Ran 22 tests in 0.005s
    OK
```