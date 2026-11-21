# Bizim Hikayemiz · Bölüm 1

Mert’ten Rümeysa’ya tanışma yıldönümü oyunu. Tasarım belgesi: `Bizim_Hikayemiz_Spesifikasyon.md` (sürüm 1.3).

Tek sayfa HTML5, vanilla JS ve CSS. Kurulum ya da derleme gerekmez.

## Dosyalar

| Yol | Ne |
| --- | --- |
| `index.html` | Oyunun tamamı (CSS + JS içinde) |
| `assets/doku/*.webp` | İnternetten alınan CC0 dokular (aşağıda) |
| `tools/tek_dosya.py` | Her şeyi tek dosyaya gömer → `dist/bizim-hikayemiz.html` |
| `dist/bizim-hikayemiz.html` | Self-contained sürüm (0,7 MB), tek başına açılır |

## Hızlı deneme

```bash
python3 -m http.server 8000      # depo klasöründe
# telefonda / tarayıcıda: http://<bilgisayar-ip>:8000/
```

`dist/bizim-hikayemiz.html` dosyası çift tıklayınca da açılır.

Geliştirme parametreleri:

- `?hiz=4`: her şeyi 4 kat hızlı oynatır (test için)
- `?sahne=lapse|fin|sleep|morning|notes|chat`: doğrudan o sahneden başlar

## Değiştirmesi kolay yerler (`index.html` başındaki `<script>`)

- `CONFIG.NOTE_TEXT`: Rümeysa’nın Instagram notu. Ortadaki “…” Mert’ten gelecek.
- `CONFIG.DM_NAME` / `CONFIG.CHAT_NAME` / `CONFIG.CHAT_MSG`
- `ASSETS`: raster görseller hazır olunca yolunu yaz. O katmanın kodla çizilmiş hâli kendiliğinden devre dışı kalır. Beklenen biçim: bölüm 9’daki gibi 1080x1920, şeffaf PNG/WebP, tam tuval.
  - `avatar2022`: Mert’in 2022 profil fotoğrafı (yuvarlak kırpılır, yoksa boş avatar)
  - `notesIcon`: Not Defteri simgesi (yoksa turuncu kare)
  - `bouquet`: çiçek buketi (yoksa 💐)
  - `wardrobe`, `door`, `momShadow`, `bear`, `bed`, `rSit`, `rDown`, `rLie`, `quilt`: oda katmanları
- `OPEN_TXT` / `FIN_TXT`: senaryo, bölüm 7’den birebir.
- `PH`: ışık fazlarının renkleri (bölüm 5). Sabah paleti seçilmediği için şimdilik şeftali-pembe duvar (`#f0c4b4`) ve açık lila zemin (`#c7b4d8`) kullanılıyor.

## Grafikler

Oda kodla, katman katman canvas’a boyanıyor: titrek kenarlar, fırça darbeleri, kenarda boya birikmesi, gerçek kumaş, ahşap ve sıva dokuları, kâğıt dokusu, tanecik, vinyet ve toz. Her katman `index.html` içinde ayrı bir `<div class="layer">` ve kendi paralaks derinliğine sahip. Bu sayede bir PNG ile tek tek değiştirilebilir.

### Dokular: kaynaklar ve lisans

Hepsi [Poly Haven](https://polyhaven.com)’dan alındı. Lisansları **CC0** (kamu malı, atıf zorunlu değil). Gri tonlamaya çevrilip küçültüldü ve WebP yapıldı.

| Dosya | Poly Haven dokusu | Yazar(lar) |
| --- | --- | --- |
| `siva.webp` (duvar) | [White Rough Plaster](https://polyhaven.com/a/white_rough_plaster) | Rob Tuytel |
| `zemin.webp` (zemin) | [Wood Floor](https://polyhaven.com/a/wood_floor) | Dimitrios Savva |
| `battaniye.webp` (battaniye, yorgan) | [Knitted Fleece](https://polyhaven.com/a/knitted_fleece) | colormass, Rico Cilliers |
| `pelus.webp` (ayı) | [Curly Teddy Natural](https://polyhaven.com/a/curly_teddy_natural) | colormass, Rico Cilliers |
| `ahsap.webp` (dolap, yatak çerçevesi) | [Wood Cabinet Worn Long](https://polyhaven.com/a/wood_cabinet_worn_long) | Dimitrios Savva, Rico Cilliers |
| `suveter.webp` (kazak) | [Cotton Jersey](https://polyhaven.com/a/cotton_jersey) | colormass, Rico Cilliers |
| `kagit.webp` (kâğıt dokusu, yastık) | [Rough Linen](https://polyhaven.com/a/rough_linen) | colormass, Rico Cilliers |

Yazı tipi: [Nunito](https://fonts.google.com/specimen/Nunito) (Google Fonts, SIL OFL). İnternet yoksa sistemin yuvarlak yazı tipine düşer.

### Ses

Hazır ses dosyası kullanılmadı. Bütün sesler WebAudio ile kodda üretiliyor: uzak rüzgâr, gece saat tiktağı, tuş tıkı, mesaj “pop”u, kilit ekranındaki yıl tıkı. Anne ünlemi çıkınca sesler kısa süre kısılıyor. Müzik yok. Sesler ilk dokunuştan (Başla) sonra açılır.

## Spesifikasyondan bilinçli küçük farklar

- Kamera konumu: oda geniş planında telefon bölüm 4’teki yerde durur (yatay %7–50, dikey %56–100). Mesajlar okunurken ve yazılırken kamera telefona yaklaşır: telefon alttaki yaklaşık %60–64’e büyür, oda üstte kararmış ama canlı görünür. Geniş planda yazılar okunamayacak kadar küçük kalıyordu.
- Rümeysa’nın kendi alıntı yanıtlarında etiket “Yanıt verdin” (Instagram’daki gibi). Mert’in alıntılarında “Sana yanıt verdi”.
- Kilit ekranında yıl dönerken gün adı da doğru günle birlikte değişir: Salı → Çarşamba → Cuma → Cumartesi → **Pazar**.
- Yazma kolaylığı: telefon klavyesindeki tuşlar küçük. Bu yüzden parlayan tuşun dokunma alanı çevresine doğru genişletildi. Masaüstünde fiziksel klavye ve Enter da çalışır.
- “Baştan oyna” sayfayı yeniler ve başlık ekranına döner.

## Raspberry Pi 5’te yayın (Nginx + Cloudflare Tunnel)

1. Dosyaları Pi’ye kopyala:

   ```bash
   sudo mkdir -p /var/www/bizimhikayemiz
   sudo cp -r index.html assets /var/www/bizimhikayemiz/
   # ya da sadece tek dosya:
   # sudo cp dist/bizim-hikayemiz.html /var/www/bizimhikayemiz/index.html
   ```

2. Nginx ayarı, `/etc/nginx/sites-available/bizimhikayemiz`:

   ```nginx
   server {
       listen 8080;
       server_name _;
       root /var/www/bizimhikayemiz;
       index index.html;
       charset utf-8;
       types { image/webp webp; }
       location / { try_files $uri $uri/ =404; }
       location /assets/ { expires 7d; }
       # Cloudflare Access kullanılmayacaksa basit parola:
       # auth_basic "Bizim Hikayemiz";
       # auth_basic_user_file /etc/nginx/.htpasswd_bh;
   }
   ```

   ```bash
   sudo ln -s /etc/nginx/sites-available/bizimhikayemiz /etc/nginx/sites-enabled/
   # parola istersen: sudo apt install apache2-utils && sudo htpasswd -c /etc/nginx/.htpasswd_bh rumeysa
   sudo nginx -t && sudo systemctl reload nginx
   curl -I http://localhost:8080/   # 200 OK görmelisin
   ```

3. Cloudflare Tunnel ile alt alan adı (cloudflared kurulu ve `cloudflared tunnel login` yapılmış olmalı):

   ```bash
   cloudflared tunnel create bizimhikayemiz
   cloudflared tunnel route dns bizimhikayemiz hikaye.ALANADIN.com
   ```

   `~/.cloudflared/config.yml`:

   ```yaml
   tunnel: bizimhikayemiz
   credentials-file: /home/pi/.cloudflared/<TUNNEL-ID>.json
   ingress:
     - hostname: hikaye.ALANADIN.com
       service: http://localhost:8080
     - service: http_status:404
   ```

   ```bash
   sudo cloudflared service install && sudo systemctl restart cloudflared
   ```

   Zaten çalışan bir tünel varsa ona yalnızca yeni `hostname` satırını ekle ve servisi yeniden başlat.

4. Koruma: Cloudflare Zero Trust → Access → Applications → Self-hosted. Alan adını `hikaye.ALANADIN.com` yap. Kural olarak “Emails: sizin iki e-postanız” ekle, oturum süresini uzun tut (ör. 1 ay). Basit parola (`auth_basic`) da yeter. İkisini birlikte kullanmaya gerek yok.

5. Kontrol: telefonda `https://hikaye.ALANADIN.com` adresini aç. Ses için sessiz modu kapat. iPhone’da eğim paralaksı yalnızca HTTPS’te ve izin verilince çalışır (Başla’ya basınca izin sorar).

Yarın için öneri: telefonu dikey tut, ekran parlaklığını yüksek yap. Ana ekrana ekle (Paylaş → Ana Ekrana Ekle) ve tam ekran aç.
