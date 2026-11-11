from pathlib import Path
import base64, mimetypes, re

root = Path(__file__).resolve().parent
dist = root / 'dist'
html = (dist / 'index.html').read_text(encoding='utf-8')
css = (dist / 'styles.css').read_text(encoding='utf-8')
catalog = (dist / 'catalog.js').read_text(encoding='utf-8')
script = (dist / 'app.js').read_text(encoding='utf-8')

def embed(match):
    asset = match.group(0)
    content = (dist / asset).read_bytes()
    mime = mimetypes.guess_type(asset)[0] or 'application/octet-stream'
    return 'data:' + mime + ';base64,' + base64.b64encode(content).decode('ascii')

html = html.replace('<link rel="preload" as="image" href="assets/hero.webp">', '')
html = html.replace('<link rel="stylesheet" href="styles.css">', '<style>' + css + '</style>')
html = html.replace('<script src="catalog.js" defer></script>', '')
html = html.replace('<script src="app.js" defer></script>', '')
html = html.replace('</body>', '<script>' + catalog + '\n' + script + '</script></body>')
html = re.sub(r'assets/[a-zA-Z0-9_.-]+\.(?:webp|jpg|svg)', embed, html)
(root / 'LeJardin_Preview.html').write_text(html, encoding='utf-8')
print('Prévia autossuficiente criada:', len(html.encode('utf-8')), 'bytes')
