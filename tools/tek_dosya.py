#!/usr/bin/env python3
"""index.html + assets/ klasörünü tek, self-contained HTML dosyasına çevirir.
Kullanım:  python3 tools/tek_dosya.py   →  dist/bizim-hikayemiz.html
Görseller base64 olarak gömülür (bölüm 11: toplam 16 MB altı)."""
import base64, mimetypes, pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
html = (root / 'index.html').read_text(encoding='utf-8')
def inline(m):
    rel = m.group(2)
    p = root / rel
    if not p.is_file():
        return m.group(0)
    mime = mimetypes.guess_type(p.name)[0] or ('image/webp' if p.suffix == '.webp' else 'application/octet-stream')
    return m.group(1) + 'data:%s;base64,%s' % (mime, base64.b64encode(p.read_bytes()).decode()) + m.group(3)
html = re.sub(r"""(['"])(assets/[^'"]+)(['"])""", inline, html)
out = root / 'dist' / 'bizim-hikayemiz.html'
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding='utf-8')
mb = out.stat().st_size / 1e6
print(f'{out}  {mb:.2f} MB')
assert mb < 16, '16 MB sınırı aşıldı'
