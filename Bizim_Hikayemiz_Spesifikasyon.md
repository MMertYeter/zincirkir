# Bizim Hikayemiz: Oyun Tasarım ve Teknik Spesifikasyon

Mert’ten Rümeysa’ya tanışma yıldönümü oyunu. Sürüm 1.3, 21 Kasım 2026. Bu belge, oyunu devralacak kişi ya da Claude oturumu için tek başına yeterli olacak şekilde yazıldı.

## 1. Proje özeti

- Mert, Rümeysa ile tanışma yıldönümü için bir oyun yapıyor. Çift uzak ilişki yaşıyor, ara ara görüşebiliyorlar. Oyun, tanışma günü Rümeysa’nın yanında Mert tarafından açılacak ve Rümeysa oynayacak.
- Hedef tarih: tanışma günü 22 Kasım 2026, Pazar. Oyunun sabah sahnesi bu tarihi gösterir.
- Şimdilik tek bölüm var (Bölüm 1, Bölüm 1 sonu ekranıyla biter). Sonra bölümler eklenebilir.
- Ton: sakin, sessiz, sevimli, hafif karanlık, cozy. Referanslar: Good Pizza, Great Pizza’nın sıcak ve yumuşak çizgisi; The Long Dark’ın sessizliği (korku yok, sadece huzurlu loşluk).
- Dil Türkçe. Oyuncu Rümeysa, karşı taraf Mert.
- Hikâye ve sahne odaklı bir oyun. Masa başı mini oyun değil.
- Gerçek hayat bağlantısı: oyun, Mert’in kendi yazdığı iki gerçek uygulamaya (Not Defteri ve Sohbet) açılan bir kapıyla biter (bölüm 6.8).

## 2. Kritik kararlar (bunlara aykırı çalışma)

1. **Tek bakış açısı: Rümeysa.** Mert’in ekranı oyunda hiç gösterilmez. Mert’in mesajları Rümeysa’nın telefonuna gelen mesajlar olarak görünür (önce Mert yazıyor göstergesi, sonra balon). Mert’in otomatik yazma sahnesi iptal edildi.
2. **Telefon ekranı hiçbir zaman tam ekran arayüz olmaz.** Oyun omuz üstü kamerayla odada geçer, telefon odanın içindeki bir nesnedir ve arkada oda hep görünür. Yazma sırasında kamera telefona yaklaşır: telefon ekranın alt yaklaşık %60’ında büyür, oda üstteki yaklaşık %40’ta kalır (hafif bulanık ya da kararmış ama canlı; ışık, kapı ve ünlem görünür). Sabah bölümünde de aynı kural geçerli: kilit ekranı, ana ekran ve uygulamalar telefon nesnesinin yüzeyinde görünür.
3. **Dar kadraj.** Rümeysa’nın yatağı, kendisi ve telefon ana öğedir. Kardeşin yatağı ve kardeş hiç görünmez. Dolap sadece kenarından görünür.
4. **Anne hiç görünmez.** Sarı ünlem kapının ortasında çıkar. Annenin tek izi, zemindeki koridor ışığına düşen gölgesi ve ekrana düşen yazıdır.
5. **Grafik vektör (SVG) değil.** Boyalı, dokulu illüstrasyon hissi veren raster görseller (PNG ya da WebP). Claude görsel (raster) üretemez, görselleri Mert harici bir araçla hazırlar (bölüm 9).
6. **Yazma mekaniği:** Rümeysa yanan tuşa her bastığında mesajın sıradaki 5 ila 10 harfi yazılır (bölüm 6.1).
7. **Sessizlik:** müzik yok, yavaş hareket, loş ışık.
8. Oyun içi tüm metinlerde Türkçe karakterler ve doğru kesme işareti (’) kullanılır.
9. **Mert’in görünen adı iki dönemde farklıdır.** Instagram DM bölümlerinde (tanışma günü, 22 Kasım 2022) adı **mertyeter** olarak yazar. Uyandıktan sonraki sabah bölümünde (Sohbet uygulaması) adı **mertt 🍯🐻🤍** olarak yazar. İki ad hiçbir sahnede karışmaz.

## 3. Akış (sahne sahne)

1. **Başlık ekranı:** Bizim Hikayemiz, alt başlık Bölüm 1: Bir not, bir cevap, Başla düğmesi. Arkaplan yumuşak pembe-lila gradyan.
2. **Açılış, öğlen:** Oda loş gün ışığında. Rümeysa pembe battaniyeli yatağında oturuyor, elinde telefon, kamera sağ omzunun arkasında. Instagram DM açık, sohbetin üst çubuğunda Mert’in adı mertyeter yazar. İlk mesaj Mert’ten: notuna verilen yanıt.
3. **Canlı açılış (13 mesaj, bölüm 7.1):** Mert’in mesajları sırayla gelir (her biri önce Mert yazıyor göstergesi, sonra balon). Rümeysa’nın 6 mesajını oyuncu tuşlarla yazar. Alıntı yanıtlar ve ❤️ tepkileri vardır.
4. **Zaman akışı (yaklaşık 12 sn artı anne kesintisi):** Sohbet okunmayan bulanık balonlarla hızla yukarı kayar. Saat 13:10’dan 19:40’a ilerler. Işık öğlenden akşama geçer. Ortada anne kesintisi olur (bölüm 6.3).
5. **Son mesajlar (bölüm 7.2), akşamdan geceye:** 41 mesaj okunur hızda akar. Bunların dördünü Rümeysa tuşlarla yazar. Telefondaki saat 19:40’tan 02:00’ye ilerler, ışık akşamdan geceye döner (gerçek saatler; o gece saat 2’de uyudular).
6. **Uyku:** Saat 02:00 olunca uyku başlar. Mesajlar hafif hafif kayar. Rümeysa telefonu yastığının altına koyar, başını sola çevirir, yorganı üzerine çekip uyur. Işık geceye döner (bölüm 6.6).
7. **Ertesi sabah (bilinçli zaman atlaması):** Rümeysa telefonu eline alır. Kilit ekranında önce 2022 yazar, yılın son hanesi tık tık kayarak 2022 → 2023 → 2024 → 2025 → 2026 olur ve 22 Kasım 2026, Pazar’da durur (bölüm 6.7). Kilit açılınca ana ekranda Not Defteri adlı uygulama vardır.
8. **Gizli giriş:** Not Defteri’nde sağ üstteki üç nokta 5 saniye basılı tutulur, sonra ekrana 5 kez dokunulur. Sohbet uygulamasına giriş yapılır (bölüm 6.7).
9. **Sohbet uygulaması:** Mert’in sohbeti (adı mertt 🍯🐻🤍) açılır. Mert’in mesajı gelir, ardından sticker gibi bir çiçek buketi görseli.
10. **Bitiş kartı:** Günaydın, Rümeysa. Tanışma günümüz kutlu olsun. Bu daha ilk bölümdü. Bölüm 1 sonu. Baştan oyna düğmesi.

## 4. Sahne: oda ve kamera

Mert’in el çizimine göre oda iki yataklıdır. Kamera Rümeysa’nın sağ omzunun hemen arkasında ve yakındır, odanın arka duvarına bakar.

- Sağ yatak: Rümeysa’nın yatağı, pembe battaniye, yastık kameraya yakın uçta. Kadrajın ana öğesi, alt yarıyı ve sağı kaplar.
- Sol yatak: kardeşin yatağı, duvara bitişik, koyu renk. Odada vardır ama kadraj dışındadır. Hiç çizilmez.
- Arka duvarda solda elbise dolabı (kadrajda sadece sağ kenarı), sağda her zaman açık duran kapı (kapatmıyorlar) ve koridor ışığı.
- Dolabın dibine yaslı oturan peluş ayı: kahverengi, göbeğinde pembe kalp.
- Poster ve lamba yok. Duvar sade.
- Ön planda Rümeysa arkadan: siyah ya da koyu kestane saç, karışık kıyafet (şimdilik lila süveter varsayımı). Elindeki telefonun ekranı kameraya dönüktür.

Başlangıç yerleşimi (dikey kadraj, yüzde olarak; prototip v0.2’den): kapı yatay %52 ila 88, dikey %5 ila 48; ayı yatay %5 ila 29, dikey %31 ila 47; Rümeysa’nın yatağı yatay %39 ila 100, dikey %45 ila 100; Rümeysa’nın başı merkezi yatay %70, dikey %61; telefon yatay %7 ila 50, dikey %56 ila 100; sarı ünlem kapının ortası, yatay %68, dikey %13.

Katman sırası arkadan öne (parantezde paralaks derinliği): duvar ve zemin (0.15), dolap kenarı, kapı ve koridor ışığı, zemindeki ışık şeridi, ayı (0.5), Rümeysa’nın yatağı (0.9), Rümeysa ve telefon (1.4), ışık katmanı, vinyet, tanecik. Paralaks kaynakları: parmak ya da fare hareketi, cihaz eğimi (iOS’ta izin ister) ve çok yavaş otomatik sallanma. Kayma miktarı küçük tutulur (en fazla yaklaşık 20 birim).

## 5. Işık fazları ve renkler

Geçişler yumuşak (yaklaşık 1,4 sn, renkler CSS değişkeniyle). Aşağıdaki değerler prototipten gelir ve başlangıç noktasıdır.

| Faz | Duvar | Zemin | Koridor ışığı | Genel ton (renk, saydamlık) | Telefon parıltısı |
| --- | --- | --- | --- | --- | --- |
| Öğlen | #b7a5d0 | #8a769f | #fff1cf, güçlü | #3b2a63, 0,18 | 0,12 |
| Akşam | #a97390 | #7a5170 | #ffc47e, sıcak | #ff8a3d, 0,20 | 0,30 |
| Gece | #2f2a55 | #1f1b3d | #35305f, kapalı | #070518, 0,50 | 0,85 |
| Sabah | yumuşak şeftali-pembe (yeni, seçilecek) | açık lila | #fff1d8, çok yumuşak | #ffd9c4, 0,10 | 0,05 |

Vurgu rengi sarı (#ffd23f, ünlem; #ffc94d, tuş parlaması). Pembe battaniye #ff9ec4. Uygulama balonu rengi #6b5bd6.

## 6. Mekanikler

**6.1 Mesajlaşma (Instagram DM benzeri).** Sohbetin üst çubuğunda Mert’in adı **mertyeter** yazar (22 Kasım 2022’deki Instagram adı). Adın solunda Mert’in 2022’deki Instagram profil fotoğrafı yuvarlak olarak görünür (görsel Mert’ten gelecek; gelmezse yuvarlak boş avatar). Mert yazıyor göstergesi ve diğer etiketlerde de bu ad kullanılır. Sohbetin en üstünde Rümeysa’nın Instagram notu küçük bir not baloncuğu olarak görünür: elinden kupası alınmış Slytherin … var üstümde (ortası Mert’ten gelecek; Harry Potter göndermesi, Mert’in ilk mesajı bu nota yanıttır). Gelen mesajlar (Mert) solda açık lila balon, giden mesajlar (Rümeysa) sağda #6b5bd6 balon. Mert’in mesajı gelmeden önce kısa bir Mert yazıyor göstergesi (1 ila 2 sn, mesaj uzunluğuna göre). İlk mesajın üstünde küçük etiket: Notuna yanıt verdi. Alıntı yanıtlarda balonun üstünde küçük bir alıntı kutusu ve Sana yanıt verdi etiketi bulunur. ❤️ tepkisi, mesajdan yaklaşık 0,6 sn sonra balonun sol altında belirir.

Rümeysa’nın yazması: Türkçe Q klavye. Satırlar: `qwertyuıopğü`, `asdfghjklşi`, `zxcvbnmöç`; alt satır: virgül, geniş boşluk tuşu, nokta, soru işareti, ünlem. Sıradaki harfin tuşu sarı (#ffc94d) parlar ve hafif yükselir (harf küçük harfe çevrilir, tr yerel ayarıyla; klavyede olmayan karakter için boşluk tuşu parlar). Doğru tuşa basılınca mesajın sıradaki 5 ila 10 harfi (rastgele) yazılır ve yeni sıradaki tuş parlar. Yanlış tuş 0,3 sn titrer. Mesaj bitince gönder düğmesi sarı parlar ve basılınca mesaj balonu olur. Yazma kutusunda son 30 karakter ve imleç görünür. Uzun mesajlar bile en fazla yaklaşık 20 basışla biter.

**6.2 Zaman akışı.** 48 bulanık balon (4 piksel blur) hızla eklenir, her biri rastgele uzunlukta, sağ ya da soldan. Aralık 200 ms’den başlayıp azalarak 70 ms’ye iner. Üstteki saat 13:10’dan 19:40’a doğrusal ilerler. 27. balondan itibaren ışık akşam fazına geçer. Balonlar gerçek mesaj değildir, rastgele harf dizileridir.

**6.3 Anne kesintisi.** 21. balonda tetiklenir. Kapıdan koridor ışığı güçlenir, kapının ortasında sarı ünlem belirir (sarı daire #ffd23f, koyu sarı kenar #7a5a00, beyaz ünlem değil koyu #3a2b00, yukarı aşağı sekme). Akış durur ve oyuncu ünleme dokunana kadar bekler. Dokununca ünlem kaybolur, ekranda 2,6 sn şu yazı görünür: Rümeysa, gel yemeğe yardım et! Bu sürede Rümeysa telefonu indirir (telefon aşağı kayıp soluklaşır), zemindeki ışık şeridinde annenin gölgesi görünür (kafa ve gövde, koyu mor, saydam). Sonra ışık normale döner, telefon geri gelir ve akış hızla devam eder. Annenin sesi ve görüntüsü yoktur.

**İkinci anne kesintisi (gece, Uyu artık!).** Son mesajlar bölümünde telefondaki saat 01:45’e geldiğinde (iki mesaj arasında) tetiklenir. Mekanik birincisiyle aynıdır: koridor ışığı güçlenir, kapının ortasında sarı ünlem çıkar, akış dokunulana kadar durur. Dokununca 2,6 sn şu yazı görünür: Uyu artık! Rümeysa telefonu indirir, zemindeki ışık şeridinde annenin gölgesi görünür. Sonra telefon geri gelir, kalan mesajlar akar ve 02:00’de uyku başlar. Yedek cümle (şimdilik kullanılmıyor): akşam Hâlâ telefonda mısın?

**6.4 Okunur hızlı akış.** Son mesajlar bölümünde her mesaj eklendikten sonra bekleme süresi en fazla 520 ms’dir (180 ms artı karakter sayısı çarpı 7 ms). Mert’in mesajları gelen, Rümeysa’nın mesajları giden olarak görünür. Dört mesaj (bölüm 7.2’de ty işaretli) oyuncu tarafından yazılır: bu sırada kamera telefona yaklaşır ve klavye açılır, yazma bitince klavye kapanır ve akış devam eder. Telefonun durum çubuğundaki saat bu bölüm boyunca 19:40’tan 02:00’ye mesaj sırasına göre ilerler (son mesajda 01:5x civarı). Işık akşam fazından gece fazına yumuşakça geçer; geçiş yaklaşık 23:00’te başlar. Telefon parıltısı giderek artar. Koridor ışığı ise açık kalır ve ancak uyku sahnesinde söner (bölüm 6.6). Saat 02:00’yi gösterdiğinde uyku sahnesi tetiklenir.

**6.5 Ayı.** Dokununca ayıdan küçük bir kalp çıkar ve yukarı süzülüp kaybolur. Gece fazında ayının kalbi çok hafif pembe parlar. Hediye ipuçlarından biri ileride ayıya bağlanabilir.

**6.6 Uyku sahnesi.** Tetik: telefondaki saatin 02:00 olması. Sıra: (1) son mesajlar yaklaşık 3 sn boyunca hafifçe yukarı kayar; (2) yazı: Rümeysa telefonu yastığının altına koyuyor; (3) telefon aşağı kayıp kaybolur (1,5 sn); (4) Rümeysa başını sola çevirir, yorganı üzerine çeker, ışık geceye döner (koridor ışığı söner, pembe yorgan yükselir), 💤 simgeleri süzülür; (5) yaklaşık 5,5 sn bu sahnede kalınır. Rümeysa için gereken pozlar: telefonla oturuyor, telefonu indirmiş, sola dönük yatıyor, yorganı çekmiş. Prototipte bu sahne odadan bağımsız basit bir animasyondur ve odayla birleştirilecektir.

**6.7 Sabah ve gizli giriş.** (1) Kilit ekranı: büyük saat 08:12, altta kilidi açmak için dokun yazısı. Tarih önce 2022 olarak gelir (Rümeysa 2022’de uyudu). Yaklaşık 1 sn sonra yılın son hanesi kilometre sayacı gibi aşağıdan yukarı tık tık kayar: 2 → 3 → 4 → 5 → 6. Her adım yaklaşık 0,4 sn, her tıkta yumuşak bir tık sesi. 2026’da durur, tarih 22 Kasım 2026, Pazar olarak kalır ve yıl kısa bir an hafif parlar. Kilidi açma dokunuşu animasyon bitince etkin olur. (2) Ana ekran: birkaç sahte uygulama simgesi (Kamera, Mesajlar, Müzik, Harita, Galeri, Saat, Hava) ve parlayan Not Defteri simgesi (turuncu; gerçek simge Mert’ten gelecek). (3) Not Defteri açılır: üstte uygulama adı ve sağda üç nokta düğmesi, altında Merhaba Rümeysa kartı ve birkaç sahte not kartı. Gerçek uygulamanın görünümü: krem arkaplan, yanık turuncu vurgu (#e8531a civarı), Kaldığın yer kartı, Takip Çizelgesi, PDF Araçları, Derslerim klasörü, sağ altta artı düğmesi. Deneme alanım kartı sadece Mert’e görünür, oyunda gösterilmez. (4) Gizli giriş: üç noktaya 5 saniye basılı tutulur. Altta turuncu bir ilerleme çubuğu dolar. Erken bırakılırsa çubuk anında sıfırlanır. 5 saniye dolunca ipucu yazısı ekrana 5 kez dokun (0/5) olur, her dokunuşta sayı artar (üç noktaya dokunmak sayılmaz). 5. dokunuşta giriş yapılır. Oyuncu 4,5 saniye boşta kalırsa ipucu çıkar: sağ üstteki üç noktaya 5 saniye basılı tut.

**6.8 Sohbet uygulamasına geçiş (final).** Giriş yapılıyor animasyonu (1,4 sn). Koyu temalı Sohbetler listesi, ilk kartta Mert’in sohbeti (gerçek uygulamada karşı tarafın profil resmi kalpli bir kaplumbağa, adı Mert’in telefonunda hatuunn 🧚🤍 olarak görünür). Oyunda Rümeysa tarafı gösterildiği için listede ve sohbet başlığında Mert’in adı **mertt 🍯🐻🤍** yazar. Mert’in profil resmi yerine yuvarlak içinde 🐻 simgesi kullanılır. Dokununca sohbet açılır. Önce Mert yazıyor göstergesi (1,7 sn), sonra Mert’in mesajı: günaydınnn meleğimmm her şeyim bitanemm bugün tanışma tarihimiz seni çokk cokk seviyorummm. Ardından büyük bir çiçek buketi görseli sticker gibi belirir (zıplayarak büyür). Yaklaşık 3,8 sn sonra bitiş kartına geçilir. Gerçek Sohbet uygulaması ayrıca şunları içerir (oyunda gösterilmez, ileride bağlanabilir): Notlarımız, Panomuz (tanışma sayacı 3 yıl 11 ay 30 gün ve anılar), Ortak Kitaplık, Oyunlar, Kahve ve tarifler, Takip bölümü.

## 7. Senaryo verisi (gerçek mesajlar)

Biçim: `gönderen | metin | seçenekler`. Gönderen m = Mert, r = Rümeysa. Seçenekler: `note` ilk mesaj etiketi (Notuna yanıt verdi), `re=` alıntı yapılan mesaj, `rx=` tepki, `ty` oyuncu tuşlarla yazar. Metinler gerçek yazışmadan birebir alınmıştır, yazım hataları bilerek korunur. (Bilgi: 7.2’deki sev, sevgili demektir; metin değiştirilmez.)

**7.1 Canlı açılış (13 mesaj). Rümeysa’nın tüm mesajları oyuncu tarafından yazılır:**

```text
m | Mazbatası geri alınıp sonra tekrardan teslim edilen Ekrem İmamoğlu gibiyim ama hala geri teslim edilmemiş hali | note
r | CKSNVDJVJSKGKEKGRİVJSKVNSKSNSKFNSKDSJVNSKFJDKGNDKFNGKNDVJSJVNSKFNFKVNSKGNDKGNEGJDJFOEKTNNDNCSKFKSJFKTKROEJEJRJEKD
r | oha patladim buna coki | rx=❤️
m | Bide slytherinin elinden kupayı ne zaman alıyorlardı la izlemeyeli çok oldu
r | birinci bölümde kupayı slytherin almışken dumbledore gtünden puan uydurup kupayı Griffindora vermisti
m | Hee evet doğru KRHSKDHKSGSBD
r | sen Harry Potter mi izliyorsun
m | Tüm bölümleri izlemiştim geçen sene
m | İlk kitabı da vardı da baya şey hatırlıyorum diye kitaba başlamamıştım daha
r | saygı duydum | re=Tüm bölümleri izlemiştim geçen sene
m | Kdgsjsgshf
m | Az unutmayı bekliyom kitabını okurum bide
r | oku hepsini oku acil | re=İlk kitabı da vardı da baya şey hatırlıyorum diye kitaba başlamamıştım daha ; rx=❤️
```

**7.2 Son mesajlar (41 mesaj, akşam ışığı). Okunur hızda akar, sadece ty işaretliler tuşlarla yazılır:**

```text
m | La çok düşünme sıkıntı yok
r | beynim yok zaten benim bu ara
m | Başın ağrıyo zaten yorma çok dur
r | ben seninle konuşmak istiyorum
r | ama
r | sev yapamam
m | Tamam konuşuruz o dursun bi | re=sev yapamam
m | Onunda zamanı gelir kdgsjsg
r | konuşalım
m | Bak şeyi sorim ama
r | ya
r | tamm sor
m | Sebebi benle mi alakalı yoksa durumlarla mı | re=sev yapamam
r | ailem | rx=❤️
m | Tamamiyle özeleştiri yapabilmek amaçlı
m | Ah be | re=ailem
m | Ne zamana kadar böyle sürecek ki bu
m | Üniversite den önce biteceğini sanmıyorum | rx=❤️
r | mert beni görsen sevmezsin zaten
m | Zamanında kimleri sevmiş olduğunu bilsen aklın almaz kdhsnsg
m | Ki neden sevmeyeyim | re=mert beni görsen sevmezsin zaten
r | oylr işte
r | güzel degilim
r | ayrica
r | uyumsuz biriyum
r | inatciyim
r | gıcık biriyim
m | Güzellik kimin umrunda ki ve erkeğe sevdiği güzel gelir onu soyliyim
m | Bana hiç gıcıklık yapmadın | re=gıcık biriyim
r | noldu bi günde böyle ya djejfdjdj | ty
m | KKFHSJDGSJSGHSKSGSJGS
m | Bende ilk kez böyle bişey yaşıyom
m | Dünya garip
m | Hızlı oldu
r | baya hızlı | ty
m | Dün cihanı sikecek kişi olarak tanıyodum seni kdhsjdhd
r | ya | ty
r | xjsjcjsjcjs | ty
r | cihan ne dedi
m | Benden başkası sana el suremez demiştim de sen gay misin diyodu kfhsjdg
m | İşte rıza gösterdi falan biseyler diyodu sonra sana yazmış işte | re=cihan ne dedi
```

Not: cihan ne dedi mesajı tuşla yazılmaz, okunarak akar (Mert’in kararı). Cihan’la ilgili ek bir ipucu ya da açıklama oyuna eklenmez; mesajlar olduğu gibi kalır.

## 8. Veri şeması ve motor

Önerilen: tüm senaryo tek bir veri nesnesinde, akış tek bir async zaman çizelgesi kontrolcüsünde. Bölüm 7’deki satırlar şu nesneye çevrilir: `{w:'m'|'r', t:metin, re?:alıntı, rx?:emoji, note?:1, ty?:1}`. Bölüm türleri: `open` (canlı), `lapse` (zaman akışı, bulanık balonlar, mom olayı), `fin` (okunur akış), `sleep`, `morning`. Her sahne bir async fonksiyondur ve bir sonrakini bekler (sahne kontrolcüsü). Faz (öğlen, akşam, gece, sabah) tek bir veri özelliğiyle (data-phase) değiştirilir, renkler CSS değişkenleridir.

Durum değişkenleri: mesaj geçmişi, görünüm modu (oda geniş, yazma yakın planı), beklenen tuş, gönder hazır mı, faz. Mesaj geçmişi bulanık balonları da içerir ve sahneler arasında korunur.

## 9. Grafik üretimi ve varlık listesi

Claude görsel (raster) üretemez, kodla çizer. Boyalı illüstrasyon için Mert harici bir görsel üretim aracı (örneğin ChatGPT, Gemini, Midjourney) ya da bir çizer kullanır. Hazır olmayan varlıklar için geçici yer tutucular (basit şekiller, emoji) kullanılır ve sonra değiştirilir.

Stil tarifi (her istemde aynı): cozy, sakin, hafif karanlık, boyalı gouache dokusu, 2.5D diorama hissi, koyu mor-lacivert palet, tek sıcak vurgu sarı, hafif tanecik, sade, yazı yok, şeffaf arkaplan (PNG ya da WebP), 1080x1920 dikey tuval.

Varlıklar (hepsi ayrı şeffaf katman):

- Duvar ve zemin (tek nötr ışıklı sürüm, faz renkleri kodla verilir ya da faz başına sürüm)
- Dolap kenarı
- Kapı çerçevesi ve koridor ışığı (ışık ayrı katman)
- Zemindeki ışık şeridi ve annenin gölgesi (ayrı katman)
- Ayı ve ayının kalbi (parlama katmanı ayrı)
- Rümeysa’nın yatağı, pembe battaniye, yastık
- Rümeysa arkadan: oturuyor, telefonu indirmiş, sola dönük yatıyor, yorganı çekmiş (dört poz)
- Telefon gövdesi (ekran alanı şeffaf, arayüz HTML olarak üstüne gelir)
- Sarı ünlem
- Mert’in 2022 Instagram profil fotoğrafı (Mert gönderecek, yuvarlak kırpılır)
- Ek: vinyet, tanecik dokusu, toz parçacıkları
- Not Defteri uygulama simgesi (Mert gönderecek)
- Çiçek buketi görseli, sticker (Mert gönderecek)

## 10. Ses

Müzik yok. Başlangıçta sessiz, ilk dokunuştan sonra WebAudio ile: uzak rüzgâr, gece saat tiktağı, yumuşak tuş tıkı, mesaj geldiğinde çok hafif bir pop. Anne ünlemi çıkınca sesler kısa süre kesilir.

## 11. Teknik

- Platform: mobil tarayıcı, dikey ekran öncelikli (9:16); masaüstünde ortalanmış telefon oranı. Güvenli alanlar ve dokunma hedefleri (en az 44 piksel) gözetilir.
- Teknoloji: tek sayfa HTML5, vanilla JS, CSS animasyonları (sadece transform ve opacity), katmanlar için CSS transform ya da canvas. Gerekirse Phaser. Hedef 60 fps.
- Barındırma: Raspberry Pi 5 (8 GB) üzerinde Nginx ile statik dosyalar, Cloudflare Tunnel ile alt alan adı, parola ya da Cloudflare Access ile koruma.
- Claude içinde yayımlanacaksa: tek self-contained HTML dosyası. Harici betik sadece cdnjs ya da jsDelivr’den ve sabit sürümle. Uzak görsel yok; görseller base64 olarak sayfaya gömülür (toplam 16 MB altı). Yazı tipi gerekirse Google Fonts (Nunito) ve yedek yazı tipi tanımlı.
- Erişilebilirlik: prefers-reduced-motion’a saygı, açık ve koyu tema değişkenleri.
- Telefon eğimi için deviceorientation (iOS’ta kullanıcı izni gerekir), yoksa pointer hareketi.

## 12. Kabul ölçütleri

1. Oyun boyunca Mert’in ekranı hiç görünmez.
2. Telefon arayüzü hiçbir anda tam ekran değildir; oda her zaman en az kadrajın bir bölümünde görünür.
3. Kardeş ve kardeşin yatağı hiç görünmez.
4. İlk 13 mesaj bölüm 7.1’deki sırayla ve metinle oynar.
5. Yazma sırasında her doğru basışta 5 ila 10 harf eklenir, yanlış tuş titrer.
6. Zaman akışında saat 13:10’dan 19:40’a ilerler ve ışık akşama döner.
7. Anne ünlemi kapının ortasında çıkar, dokunulmadan akış devam etmez. İki kesinti vardır: öğleden sonra (Rümeysa, gel yemeğe yardım et!) ve 01:45’te (Uyu artık!).
8. Son 41 mesaj bölüm 7.2’deki sırayla okunur hızda akar, dört mesaj oyuncuyla yazılır.
9. Uyku sahnesi: telefon yastık altına girer, Rümeysa sola dönüp yorganı çeker, gece olur.
10. Kilit ekranında yıl 2022’den 2026’ya tık tık kayar ve 22 Kasım 2026, Pazar’da durur.
10b. Son mesajlarda saat 19:40’tan 02:00’ye ilerler; 02:00’de uyku başlar.
11. Gizli giriş: 5 saniye basılı tutma, sonra 5 dokunuş. Erken bırakınca sıfırlanır.
12. Sohbet mesajı ve çiçek buketi gösterilir, bitiş kartı gelir, Baştan oyna çalışır.
13. Instagram DM bölümlerinde Mert’in adı mertyeter, sabahki Sohbet uygulamasında mertt 🍯🐻🤍 olarak görünür.

## 13. Yol haritası

1. Oda sahnesinin raster görsellerle kurulması (katmanlar, paralaks, faz ışıkları).
2. Telefon nesnesinin odaya yerleştirilmesi ve yazma yakın planı (kamera yaklaşması).
3. Mesajlaşma sistemi (bölüm 6.1 ve 7) odaya entegre.
4. Zaman akışı ve anne kesintisi.
5. Son mesajlar, uyku sahnesi.
6. Sabah, Not Defteri, gizli giriş, Sohbet ve final.
7. Ses, cila, test (bölüm 12).
8. Pi’ye yayın, alt alan adı ve parola.

## 14. Açık sorular ve eksikler

- Rümeysa’nın saç uzunluğu ve kıyafeti kesin değil (varsayım: siyah ya da koyu kestane saç, lila süveter).
- Not Defteri uygulama simgesi ve çiçek buketi görseli Mert’ten bekleniyor.
- Sabah fazının renk paleti seçilmedi.
- Rümeysa’nın Instagram notunun tam metni (bilinen: elinden kupası alınmış Slytherin … var üstümde).
- Mert’in 2022 Instagram profil fotoğrafı bekleniyor.
- Mert, 22 Kasım 2026 günü (bitiş günü) oyuna 1-2 şey daha ekleyecek; henüz belirlenmedi.
- Bölüm 1 sonrası devam planı yok. İleride anılar, hediye kutuları ve gerçek hediye eşleşmesi düşünülüyor.
- Sohbet ve Not Defteri ekranları gerçek uygulamalara ne kadar benzesin?

## 15. Mevcut prototipler ve bilinen sapmalar

Prototipler sadece mekanik referanstır. İkisi de bu belgeyle çelişen noktalar içerir ve yeni sürümde bu noktalar düzeltilecektir.

- Oda sahnesi (vektör, kadraj ve ünlem doğru, telefon ekranı içermez): https://claude.ai/artifact/QHJbZgoN3GncerRoXWABC5
- Sohbet akışı (mekanikler, gerçek mesajlar, uyku ve sabah sahnesi çalışır): https://claude.ai/artifact/2UfYAF7XGjfo656N5r49vD. Sapmalar: telefon tam ekran gösteriliyor, Mert’in ekranı ve otomatik yazma var, oda yok, uyku sahnesi odadan bağımsız, ünlem ekranın sağ kenarında. Hepsi bu belgedeki kararlara göre değişecek.

## 16. Değişiklik günlüğü

- 21 Kasım 2026, sürüm 1.3: İkinci anne kesintisi eklendi (01:45, Uyu artık!). cihan ne dedi okunarak akar. Cihan’la ilgili ek ipucu yok. Oyun 22 Kasım 2026’da Rümeysa’ya gösterilecek.
- 21 Kasım 2026, sürüm 1.2: Zaman atlaması bilinçli; kilit ekranında yıl 2022’den 2026’ya tık tık kayar. Son mesajlarda saat 02:00’ye ilerler, 02:00’de uyku başlar (gerçek saat). DM’de 2022 profil fotoğrafı ve Rümeysa’nın Instagram notu (kısmen bilinen metin). Sohbet uygulamasında Mert’in avatarı 🐻. sev = sevgili notu. Açık sorular güncellendi.
- 21 Kasım 2026, sürüm 1.1: Mert’in görünen adı eklendi. DM bölümlerinde (22 Kasım 2022) mertyeter, sabah Sohbet uygulamasında mertt 🍯🐻🤍 (kritik karar 9, bölüm 3, 6.1, 6.8, kabul ölçütü 13). Açık sorulara zaman atlaması ve profil resimleri eklendi.
- 21 Kasım 2026, belge baştan yazıldı (sürüm 1.0): Mert’in ekranı iptal, telefon tam ekran olmayacak (omuz üstü kamera ve yakın plan), kardeş kadrajdan çıkarıldı, ünlem kapının ortasında, grafik raster, gerçek mesajlar ve final eklendi.
- Önceki kararlar: 2.5D paralaks diorama, gün boyunca ışık fazları, sessiz ve cozy ton, her basışta 5 ila 10 harf, zaman akışı ve anne kesintisi, uyku ve ertesi sabah, gizli giriş ve Sohbet uygulaması.
