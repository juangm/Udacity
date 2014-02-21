#Finish crawl web

# Function for returning the html content of a web page
def get_page(url):
    try:
        import urlib
        return urllib.open(url).read()        
    except:
        return ""
    return ""

# Function which find a link in the html code and return 
# the link and the last_position for keep looking
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

# Union of both list without repeating elements
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

# Function which return a list with all the links of the html code (url)
def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

# Function for adding url and keyword to the index
def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    temp = content.split()
    for i in temp:
        add_to_index(index,i,url)
    return index

# Main function to start to crawl the web, starting from a page "seed"
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index
    
                   
