import urllib.request
import re

def fetch_html(url):
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')
            #print(html_content)
        return html_content
        
    except urllib.error.URLError as e:
        print("Error fetching URL:", e)
        return None

def extract_latest_stories(html_content):
    latest_stories = []
    pattern = r'<a href="([^"]+)">\s*<h3 class="latest-stories__item-headline">(.*?)</h3>'
    matches = re.findall(pattern, html_content)
    for link, title in matches[:6]: 
        full_link = f"https://time.com{link}"  
        latest_stories.append({"title": title.strip(), "link": full_link})

    return latest_stories

def main():
    url = 'https://time.com'
    html_content = fetch_html(url)
    if html_content:
        latest_stories = extract_latest_stories(html_content)
        # Print the latest stories in the desired format
        print("[")
        for story in latest_stories:
            print("{")
            print(f'"title": "{story["title"]}",')
            print(f'"link": "https://time.com{story["link"]}"')
            print("},")
        print("]")
    else:
        print("Failed to fetch HTML content.")

if __name__ == "__main__":
    main()
