from pathlib import Path
import re,json
from urllib.parse import unquote
root=Path(__file__).resolve().parents[1]
errors=[]
for page in (root/'docs').rglob('*.md'):
 text=re.sub(r'```.*?```','',page.read_text(encoding='utf-8'),flags=re.S)
 for url in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text):
  url=url.split('#')[0].split('?')[0]
  if not url or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',url):continue
  target=(page.parent/unquote(url)).resolve()
  if not target.is_relative_to(root/'docs') or not target.exists():errors.append(f'{page}: {url}')
config=json.loads((root/'mkdocs.yml').read_text(encoding='utf-8'))
listed={v for item in config['nav'] for v in item.values()}
for page in listed:
 if not (root/'docs'/page).is_file():errors.append('nav: '+page)
for page in (root/'docs').rglob('*.md'):
 if page.relative_to(root/'docs').as_posix() not in listed:errors.append('unlisted: '+str(page))
if errors:raise SystemExit('\n'.join(errors))
print(f'Checked {len(listed)} Markdown pages and navigation links')
