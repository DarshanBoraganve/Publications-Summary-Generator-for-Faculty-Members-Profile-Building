import requests

def get_publications(author_name):
    """Fetches publications for a given author using the DBLP API"""
    formatted_name = author_name.replace(" ", "%20")  # Format for URL
    url = f"https://dblp.org/search/publ/api?q={formatted_name}&format=json&h=10"  

    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error: Unable to fetch data from DBLP")
        return []

    data = response.json()

    publications = []
    
    try:
        hits = data["result"]["hits"]["hit"]
        
        for item in hits:
            info = item["info"]
            title = info.get("title", "N/A")
            
            # Extract author names properly
            authors = info.get("authors", {}).get("author", "N/A")
            if isinstance(authors, list):  
                authors = ", ".join([author.get("text", "Unknown Author") if isinstance(author, dict) else author for author in authors])
            elif isinstance(authors, dict):  
                authors = authors.get("text", "Unknown Author")
            
            year = info.get("year", "N/A")
            venue = info.get("venue", "N/A")
            doi = info.get("doi", "N/A")
            
            publications.append({
                "title": title,
                "authors": authors,
                "year": year,
                "venue": venue,
                "doi": doi
            })
    
    except KeyError:
        print("No publications found")
    
    return publications