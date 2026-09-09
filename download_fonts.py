import urllib.request
import re
import os

url = "https://fonts.googleapis.com/css2?family=Alex+Brush&family=Montserrat:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap"

req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
)
with urllib.request.urlopen(req) as response:
    css_content = response.read().decode('utf-8')

# Find all url(...) in the css
urls = re.findall(r'url\((.*?)\)', css_content)

if not os.path.exists('fonts'):
    os.makedirs('fonts')

for i, font_url in enumerate(urls):
    font_url = font_url.strip("'\"")
    if font_url.startswith('http'):
        filename = f'font_{i}.woff2'
        urllib.request.urlretrieve(font_url, os.path.join('fonts', filename))
        # replace in css content
        css_content = css_content.replace(font_url, f'fonts/{filename}')

with open('fonts.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Fonts downloaded successfully.")
