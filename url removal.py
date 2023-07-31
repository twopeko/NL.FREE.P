# Use forward slashes in the file path
with open("E:/wikipedia dataset/NLP language model/wiki_links_short.txt", "r", encoding="latin-1") as file:
    lines = file.readlines()

# Filter out URL entries and keep only other categories (MENTION and TOKEN)
filtered_lines = [line for line in lines if not line.startswith("URL")]

# Process each line individually
for line in filtered_lines:
    parts = line.strip().split('\t')  # Split the line using tabs

    # Check the category of the entry
    category = parts[0]
    if category == "MENTION":
        # Extract information from MENTION entries
        mention_name = parts[1]
        mention_id = parts[2]
        mention_link = parts[3]

        # Process MENTION entry as needed
        # (e.g., store the name, ID, and link for further analysis)

    elif category == "TOKEN":
        token = parts[1]
        # Process TOKEN entry as needed
        # (e.g., store the token for further analysis)

    else:
        # Handle unrecognized entries or empty lines
        print(f"Invalid entry: {line}")

# The rest of your code for preprocessing, storing data, etc. (as shown in the previous code snippet)
