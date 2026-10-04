from html.parser import HTMLParser
from pathlib import Path
import json
import markdown
from urllib.parse import unquote, urlsplit
root=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
 def __init__(self):
  super().__init__();self.urls=[]
 def handle_starttag(self,tag,attrs):
  key={'a':'href','img':'src'}.get(tag)
  if key:
   value=dict(attrs).get(key)
   if value:self.urls.append(value)

errors=[]
for page in (root/'docs').rglob('*.md'):
 links=Links()
 links.feed(markdown.markdown(page.read_text(encoding='utf-8'),extensions=['fenced_code']))
 for url in links.urls:
  parts=urlsplit(url)
  if parts.scheme or parts.netloc:continue
  url=parts.path
  if not url:continue
  target=(page.parent/unquote(url)).resolve()
  if not target.is_relative_to(root/'docs') or not target.exists():errors.append(f'{page}: {url}')
config=json.loads((root/'mkdocs.yml').read_text(encoding='utf-8'))
def nav_pages(items):
 for item in items:
  for value in item.values():
   if isinstance(value,list):yield from nav_pages(value)
   else:yield value
listed=set(nav_pages(config['nav']))
for page in listed:
 if not (root/'docs'/page).is_file():errors.append('nav: '+page)
for page in (root/'docs').rglob('*.md'):
 if page.relative_to(root/'docs').as_posix() not in listed:errors.append('unlisted: '+str(page))
if errors:raise SystemExit('\n'.join(errors))
print(f'Checked {len(listed)} Markdown pages and navigation links')
