import requests
from bs4 import BeautifulSoup

CDP_DOCS = {
    "segment": "https://segment.com/docs/",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}

def fetch_documentation(cdp_name):
    """Scrape the documentation of a given CDP"""
    url = CDP_DOCS.get(cdp_name.lower())
    if not url:
        return "Documentation not available."
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract text from documentation
        content = ' '.join([p.text for p in soup.find_all("p")])
        return content[:5000]  # Limit to first 5000 characters
    except Exception as e:
        return f"Error fetching {cdp_name} documentation: {str(e)}"
