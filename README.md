NLP Language Model - README

1. Overview:
   This NLP (Natural Language Processing) program is designed to fetch content from a list of Wikipedia links and perform text pre-processing on the retrieved content. The pre-processed content is then stored in a text file, along with other related data.

2. Requirements:
   - Python 3.x
   - Libraries: urllib, re, BeautifulSoup, nltk, json

3. Usage:
   - Place the list of Wikipedia links in a text file, with each link on a separate line. The file should be named "wiki_links_short.txt" and located in the same directory as the program file.
   - Run the program by executing the Python script "nlp_language_model.py".
   - The program will process each link from the text file and perform the following actions:
     - For URL entries, it will attempt to fetch the content from the link, perform text pre-processing, and save the pre-processed content to "preprocessed_contents.txt".
     - For MENTION entries, it will extract information (name, ID, link) and store them in "mentions_data.json".
     - For TOKEN entries, it will store the tokens in "tokens.txt".
   - Any invalid entries or errors encountered during processing will be displayed in the console.

4. Output Files:
   - preprocessed_contents.txt: Contains the pre-processed content from the fetched URLs, each separated by a new line.
   - mentions_data.json: Contains a JSON array with information about mentions, including name, ID, and link.
   - tokens.txt: Contains the tokens extracted from the TOKEN entries.

5. Error Handling:
   - The program can handle HTTP errors (e.g., 404, 406), SSL certificate verification errors, URL errors, and general exceptions that may occur during URL fetching and processing.

6. Note:
   - Some URLs from the provided list may not be accessible or may lead to errors due to various reasons, such as server issues, expired certificates, or invalid links.
   - The program will continue processing other entries even if errors occur during the processing of specific URLs.
