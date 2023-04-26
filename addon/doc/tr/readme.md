# Thunderbird+

* Yazar: Pierre-Louis Renaud (Thunderbird 78 - 102) & Cyrille Bougot (TB 102), Daniel Poiraud (TB 68 - 91), Yannick (TB 45 - 60);
* Adres: [İletişim Fransızca ve İngilizce](https://www.rptools.org/NVDA-Thunderbird/toContact.html);
* [Kararlı sürümü indirin][1]
* [RPTools.org'daki en son sürümü](https://www.rptools.org/?p=8610) indirin
* NVDA uyumluluğu: 2019.3 ve üzeri;
* Thunderbird uyumluluğu: 102.x sürümleri;
* [RPTools.org'daki değişikliklerin geçmişi](https://www.rptools.org/NVDA-Thunderbird/changes.php?lg=tr)
* [gitHub'daki kaynak kodu][2]

Not 1: Bu Eklenti, Mozilla Apps Enhancements Eklentisiyle uyumlu değildir. İkincisi kuruluysa, ThunderbirdPlus'ı kurmadan önce onu devre dışı bırakmalı veya kaldırmalısınız;

Not 2: Bu belge Fransızcadan Türkçeye Google Translate tarafından çevrilmiştir. İnsan tarafından tercüme edilmiş bir versiyon yakında gelecek.

## Tanım

Bu eklenti, Mozilla Thunderbird posta istemcisini NVDA ile kullanmanın kolaylığını ve verimliliğini büyük ölçüde artırır.

İyileştirmeler aşağıdaki yönlerle ilgilidir:

### İşitme konforu

* "Falanca istendi alındı" uyarıları bir seçenek aracılığıyla devre dışı bırakılabilir;
* "Bu bir taslaktır" ve "Thunderbird bu mesajın sahte olduğunu düşünüyor" uyarıları dikkate alınmaz;
* Seçenekler, posta listelerinin adlarının duyurulmasını devre dışı bırakmayı, "RE" ifadelerini kaldırmayı veya gruplandırmayı ve sayıları ve diğer garip özel karakterleri kaldırarak muhabirlerin adlarını saflaştırmayı mümkün kılar;

### Ana pencerede gezinme

* Bir sonraki panele geçiş TAB tuşu kullanılarak yapılırken, escape tuşu bir önceki panele dönmenizi sağlar. Bu, F6 ve Shift+F6'dan daha rahattır.
* Control+Tab ve Control+a sayısı ile sekme seçme bu örnekteki gibi seslendirilir: Sekme 1/4, Gelen posta;
* Bir klavye kısayolu, kolayca etkinleştirmek için bir menüdeki sekmeleri listelemenizi sağlar;
* Sekme çubuğunun bağlamsal menüsünü görüntülemek için bir klavye kısayolu kullanılır;

### Klasör ağacı

* alt+aşağı ok ve Alt+yukarı ok, okunmamış mesajların bulunduğu klasörler arasında gezinir;
* Bir harf veya rakam yazıldığında, adı yazılan karakterle başlayan bir sonraki klasör seçilir. Shift tuşu ile hareket aşağıdan yukarıya doğrudur. Ayrıca klasörün ait olduğu hesabın adı duyurulur;
* Okunmamış mesajların bulunduğu bir klasördeki Space tuşu, mesaj listesindeki ilk okunmamış mesajı seçer;
* İki hesap iletişim kutusu ve ilişkili klasörleri, bunların anahtar kelimeye göre filtrelenmesine veya yalnızca okunmamış mesajların bulunduğu klasörlerin görüntülenmesine izin verir;

### Mesaj listesi

* Sütunların seçimi ve mesaj listesindeki düzenlemeleri basit bir iletişim kutusu aracılığıyla erişilebilir hale getirilir;
* Mesaj listesinin sütunlarına danışma: kısayollar, alfasayısal klavyede bir sayıya basarak gönderenin adını, konuyu veya mesajın tarihini tekrar dinlemenize, hecelemenize veya kolayca kopyalamanıza olanak tanır: örneğin, 1 veya & göndereni duyurur, 2 basış adı heceler ve 3 basış panoya kopyalar;
* F8 ile görüntülenen başlıklar bölmesinin başlıklarına danışma: Alt+bir sayı ile, 1 basış gönderici veya alıcıların adreslerini içeren bir başlığı söyler, 2 basış kopyalanmalarını sağlayan bir iletişim kutusu açar, 3 basış bağlamsal açar başlıkla ilişkilendirilmiş yerel Thunderbird menüsü;
* Boşluk, Alt+aşağı ok veya F4 ile mesaj metninin temiz hızlı önizlemesi: mesaj alıntılarındaki büyük blok başlıkları "Gönderenin adı yazdı" ifadesiyle değiştirilir. NVDA, uzun bağlantı adresi yerine "tıklanabilir bağlantı"yı da duyurur.
* Alıntıların kronolojik sırayla, aşağıdan yukarıya, Shift+Boşluk, Alt+yukarı ok veya Shift+F4 ile hızlı görünümü;
* Alt+sonraki sayfa kısayolunu veya alfanümerik klavyede 1 sayısını kullanarak eklere kolay erişim;

<!-- Çevirmenler: etiketler = etiketler -->
### Hızlı filtre çubuğu ve öncelikli etiket yönetimi

* Dikey okları kullanarak Filtre seçenekleri arasında gezinmek mümkündür. Enter tuşu, bir seçeneği işaretlemenizi veya işaretini kaldırmanızı sağlar;
* etiket ekleme veya kaldırma, alfanümerik klavyede Shift+a sayı tuşlarına basılarak yapılır. Örneğin, bir mesaja "Yapılacaklar" etiketini eklemek için 4'e basın. Ardından, artık erişilebilen hızlı filtre çubuğu aracılığıyla mesajların listesini etiketlere göre filtreleyebilirsiniz;


### Mesaj oluştur penceresi

Alt+1, Göndereni, Alt+2 alıcıyı, Alt+3 ekleri vb. duyurur. İki basış, odağı bu alanlardan birine yerleştirir;

### Yazım denetimi iletişim kutusu:

* yanlış yazılan kelime, önerilen kelimeden önce heceli veya hecesiz olarak duyurulur. NVDA+Tab veya Alt+yukarı ok kısayolları, yanlış yazılan ve değiştirilen sözcükleri duyurur: 1 tıklama sözcükleri normal hızda heceler, 2 dokunma sözcükleri hızlı heceler, 3 dokunma yanlış yazılmış sözcüğü başka bir düzenleme alanında analiz edilmek üzere panoya kopyalar;
* enter tuşunun çeşitli kombinasyonları Değiştir, Tümünü değiştir, Yoksay, Tümünü yoksay veya Sözcüğü sözlüğe ekle düğmelerini etkinleştirir, bu iletişim kutusunun daha rahat olması için eklenmiştir;

### Otomatik güncelleme

ThunderbirdPlus, devre dışı bırakma/yeniden etkinleştirme ve erteleme seçenekleriyle bağımsız bir otomatik güncelleme sistemine sahiptir;

### Chichi ile ikili operasyon

ThunderbirdPlus, doğrudan Thunderbird'e yüklenen bir eklenti olan Chichi ile sorunsuz çalışacak şekilde tasarlanmıştır.

Bu [Chichi'nin sayfası](https://www.rptools.org//Outils-DV/thunderbird-chichi-en.html) hakkında bilgi edinin;

### Diller Hakkında

ThunderbirdPlus, NVDA ve Thunderbird için kullandığınız dile çevrilmemişse bazı özellikler düzgün çalışmaz.

* uyarılar ele geçirilmeyecektir. Bunlar taslak uyarılar, iade makbuzu talebi, hileli mesaj, güncelleme vb. ;
* Thunderbird için eklenti arama işlevinin iyileştirilmesi çalışmaz;

Bugün itibariyle, eklenti aşağıdaki dillerde mevcuttur:

[Orijinal Fransızca sürüm](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_tr.html): geliştirici tarafından;

Kıdem sırasına göre çeviriler:

* [Portekizce](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_pt_PT.html): TifloTecnia.com'dan Rui Fontes ve NVDA Portekiz ekip üyesi;
* [İspanyolca](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_es.html): Rémy Ruiz tarafından;
* [İngilizce](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_en.html): Bachir Benanou tarafından;


Çevirmenlere teşekkürler.


## Mesaj sekmesi panelleri arasında gezinme (Tab, Escape)

Bu, şu panelleri içeren sekmedir: klasör ağacı, mesaj listesi ve başlık bölmesi ve mesaj ön izleme (F8 tuşuyla görüntülenir veya gizlenir).

* SEKME: sonraki panele gidin. Bu kısayol, bazı kişiler için F6'dan daha ergonomik olacaktır;
* Kaçış: önceki panele geri dönün. Shift+F6'ya eşdeğer;

Algılanan :

Mesaj listesinden metne geçiş yaparken başlıklar alanı atlanıyor. Bu başlık alanına ulaşmak için, alfasayısal klavyede hızlı bir şekilde Alt+a rakamına üç kez basın, ardından başlık içerik menüsünden çıkmak için Escape tuşlarına basın. Bu Alt+sayı kısayolları, başlıklar alanına gitme ihtiyacını azaltır. Daha fazla ayrıntı için aşağıdaki "Üstbilgileri görüntüleme" bölümüne bakın.


<a name="threadTree">

## Mesaj listesi, önizleme bölmesi ve ayrı okuma penceresi

Aşağıdaki kısayollardan bazıları bu üç bağlamda ortaktır, diğerleri ise belirli bir bağlamla ilgilidir.

<a name="ek">

### Eklere erişim (Alt+Page Down)

* Alt+sonraki sayfa veya Alt+p: ön izleme paneli görüntüleniyorsa (F8 aracılığıyla), seçilen mesajın eklerinin listesini açar;
* Alt+9 veya 1 veya 2 sayısı: yalnızca mesaj listesinden, bir basış ek sayısını belirtir, iki basış ek listesini açar;<a name="readPreview">

### Mesajların hızlı ve temiz okunması

* Bir mesajı hızlı bir şekilde okumak için komutlar üç bağlamda mevcuttur: mesajlar listesinden, bir sekmede veya ayrı bir pencerede açık bir mesajdan;
* Artık hepsi Framalistes'ten gelen mesajlarla uyumludur;
* Hızlı okuma kısayol tuşlarının çoğu, mesaj ağırlıklı bir okuma oturumu sırasında el hareketini en aza indirecek şekilde yoğunlaştırılmıştır;
* Bir kısayolun ana tuşuna bir kez basmak, mesajın düzenli bir şekilde okunmasını başlatır, yani alıntıların başlıkları büyük ölçüde kısaltılmıştır.
* Çift basış, mesajın orijinal biçiminde okunmasını başlatır. "Filtrelenmemiş okuma" terimi eşanlamlıdır;

<a name="readFromList">

#### Listedeki mesajları listeden ayrılmadan hızlıca okuyun (Boşluk, F4 veya Alt+aşağı ok)

Bu özellikten faydalanmak için öncelikle F8 tuşu ile mesaj okuma bölmesini açmalısınız. Bu tuşa basarak, bu bölmenin var olup olmadığını duyacaksınız;

Ardından mesaj listesine gidin ve aşağıdaki tuşları kullanın:

* Boşluk, Alt+Aşağı ok veya F4: listeden çıkmadan mesajın gövdesini okuyun. Bir mesajı okuduktan sonra, bir sonraki mesajı dinlemek için aşağı ok ve ardından Boşluk veya Alt+aşağı ok veya F4 tuşlarına basın;
* Çift dokunuşta, Chichi aktifse mesaj bağlantılarının listesini görüntüler. Bir RSS yayını makalesi seçilirse, web tarayıcısında açılır;
* Shift+boşluk, Alt+Yukarı ok veya Shift+f4: aynı, ancak alıntıları kronolojik sırayla okuyor (aşağıdan yukarıya);

Ve mesaj listesinde bulunan komutları tamamlamak için buraya alıntı yapalım:

* n harfi veya Alt+Sağ ok: klasörler arasında bile bir sonraki okunmamış mesajı seçer;
* Alt+Sonraki sayfa veya mesaj listesinden Alt+p: metinde sekmeye gerek kalmadan doğrudan ekler alanına ulaşmanızı sağlar;

<a name="readFromWinTab">

### Bir mesajı ayrı bir pencerede veya mesaj sekmesinde hızlıca okuyun (F4 veya Alt+Aşağı Ok)

Bir mesajı yeni bir pencerede açarken, mesajın gövdesi varsayılan olarak otomatik olarak okunur. Ancak, aşağıdaki kısayollar mesajı istediğiniz zaman tekrar dinlemenizi sağlar.

* F4 veya Alt+aşağı ok: mesajın gövdesinin hızlı okunması;
* Shift+F4 veya Alt+yukarı ok: aynı, ancak tersi;

Notlar :

* Bir hatırlatma olarak, bu kısayollara iki kez basıldığında orijinal mesajın okunması başlar;
* Otomatik oynatma, özellikle hesap IMAP olarak ayarlanmışsa, bazı bilgisayarlarda NVDA'yı engelleyebilir. Bu sorunu çözmek için Alt+d kısayolu, pencerenin açılması ile otomatik oynatmanın başlaması arasındaki gecikmeyi uzatmanıza izin veren bir giriş kutusu açar;<br>
Bu gecikmeyi ayarlamak sorunu çözmezse, [Shift+Quotes](keyequiv_tr.html#aboveTab) / Ana pencere seçenekleri / ayrı okuma penceresi aracılığıyla bu otomatik okumayı devre dışı bırakabilirsiniz: neden olursa mesajı otomatik olarak okuma NVDA çöküyor;
* Derli toplu okumadan en iyi şekilde yararlanmak ve aynı zamanda sizi gizliliğinize saygı duymayan uzak içerikten korumak için mesajların gövdesini basit HTML'de görüntüleyin. Bunu yapmak için Görünüm menüsünü açın, Mesaj gövdesine gidin ve alt menüde basit HTML seçeneğini doğrulayın.


Sütunların ve başlıkların danışması:

Burada sütunlar ve başlıklar arasında bir ayrım yapılmalıdır: Aşağıda "sütun" sözcüğü mesaj tablosundaki bir satırın bir hücresinin değerini belirtmek için kullanılmıştır. "Başlık" kelimesi mesajın kendisini ifade eder. Başlıklar, hem mesaj ön izleme bölmesinde hem de sekmede veya açık bir mesajın ayrı penceresinde görüntülenebilir;

<a name="readCols">

### Sütunlara danışma: alfasayısal klavyeden bir sayı

Bu tuşlar sadece mesaj listesinin sütunlarını etkiler. Shift tuşuna basmadan alfasayısal klavyede bir sayıya basın:
* Tek bir basış: karşılık gelen sütunun adını ve değerini söyler;
* Bir sayıya iki kez basıldığında: karşılık gelen sütunun değerini heceler;
* Üç hızlı basış: sütun değerini panoya kopyalar. Çeşitli gönderenlerin ve alıcıların adreslerini kopyalamak için aşağıda görülen başlıkların danışmalarını kullanın;

<a name="readHeaders">

### Başlıklara danışma: alfasayısal klavyeden Alt+bir sayı

Bu kısayollar, önizleme paneli görüntüleniyorsa (F8 aracılığıyla) ana pencereden ve açık bir mesajın sekmesinden veya ayrı penceresinden kullanılabilir. Duruma göre bir basış başlığı söyler ve iki basış bağlamsal bir menü görüntüler;

* Alt+1: gönderenin adını ve e-posta adresini duyurur.İki kez basıldığında bu değerleri düzenlemek için bir kutu açılır. Bunları düzenleyebilir ve ardından panoya kopyalamak için Enter tuşuna basabilirsiniz. 3 basış: başlığın açılır menüsünü açar;
* Alt+2: Varsa posta listesinin adıyla konu;
* Alt+3: mesajın tarihi;
* Alt+4 için: mesajın ana alıcıları, Birden fazla alıcı varsa, 3 basışları odağı ilk alıcıya konumlandırır, ardından sekmesi bir sonraki alıcıya geçmenizi sağlar, her alıcıdaki uygulamalar bağlamsal menüyü görüntüler;
* Alt+5: kopyadaki alıcılar;
* Alt+6: gizli kopya alıcıları;
* Alt+7: "yanıtla" adresi;
* Alt+8: kullanıcı, eğer tam başlıklar Görünüm / başlıklar / tam başlıklar menüsü aracılığıyla etkinleştirildiyse;
* Alt+9: 1 basış eklerin sayısını duyurur, 2 basış eklerin listesini açar;
* Alt+0:mesaja yerleştirilen öncelikli etiketlerin listesi;
* Alt+ [Eksi](keyequiv_tr.html#bs2) veya Alt+end: durum çubuğunun kısaltılmış bir versiyonunu söyler: okunmamış mesaj sayısı, toplam mesaj sayısı ve hızlı filtre ifadesi;
* Alt+ [Equal](keyequiv_tr.html#bs1): sekmelerin içerik menüsünü açar;
* Control + [Equal](keyequiv_tr.html#bs1): Seçilen sekmeyi seçmenize izin veren bir menüdeki açık sekmelerin listesini görüntüler;

<a name="etiketler">

### Öncelik etiketleri ekleme ve kaldırma: Shift+alfanümerik tuş takımından bir sayı

Bu özellik, örneğin bir mesajı önemli veya yapılacak olarak işaretlemenizi sağlar. Ardından, hızlı filtre çubuğu yalnızca bir veya daha fazla etiketi olan iletileri görüntüler. Örneğin, mesaj listesinde yalnızca önemli mesajları görüntüleyin;

İletiye önceden yerleştirilmiş etiketleri kontrol etmek için alfasayısal klavyede Alt+0 tuşlarına basın.

Etiket eklemek veya kaldırmak için Shift+1'den 9'a kadar bir sayıya basın;


<a name="qfb">

### Hızlı filtre çubuğu (f harfi veya Control+Shift+K)

* F harfi veya Control+Shift+K: geçerli klasördeki hızlı mesaj filtre çubuğunu görüntüler;
* Anahtar kelimeye göre filtreleme: bir anahtar kelime girin ve oklarla filtrelenmiş listeye göz atmak için Sekme tuşuna basın;
* Anahtar kelime giriş alanındaki aşağı ok, aşağıdaki seçenekler listesine erişmenizi sağlar:

    * 1: Klasörleri değiştirirken filtreleri koruyun c
    * 2: Yalnızca okunmamış mesajları göster l
    * 3: Yalnızca yıldızlı mesajları göster
    * 4: Yalnızca adres defterimdeki kişilerden gelen mesajları görüntüle d
    * 5: Yalnızca yıldız etiketli gönderileri göster
    * 6: Yalnızca ekleri olan mesajları göster j
    * vesaire.

* Bu kriterlerden birini veya birkaçını etkinleştirmek veya devre dışı bırakmak için enter tuşuna basın;
* Alt+end veya Alt+ [Equal](keyequiv_tr.html#bs1): etkin filtrelerin bir özetini ve filtrelenen mesajların sayısını duymanızı sağlar. Bu kısayolların her ikisi de yalnızca hızlı filtre çubuğundan değil, ileti listesinden de çalışır;

<br>
- hızlı bir filtre etkinken, ait olduğu liste veya sekme odaklandığında bir WAV ses dosyası oynatılır. Ses bir nefes gibidir;<br>
filter.wav dosyası şu klasörde bulunur:<br>
"%appdata%\\NVDA\\TB+ses" <br>
Dosyanızın adı filter.wav olduğu sürece beğeninize göre bir ses yerleştirebilirsiniz. Bu değişiklikten sonra NVDA'yı yeniden başlatın;v

<a name="tagFilter">

#### Etikete Göre Filtreleme

odak, hızlı filtreler çubuğunun düzenleme alanındayken:

* "Etiketler" ifadesini duyana kadar aşağı oka basın, ardından bu seçeneği işaretlemek için Enter'a basın;
* Ardından, etiketlere göre filtreleme modlarının açılır listesine ulaşmak için Sekme tuşuna basın.Örneğin, "yapılacak"ı seçerseniz, mesaj tablosunda yalnızca "yapılacak" olarak etiketlenen mesajlar listelenir;

<a name="colLayout">

### Sütun düzeni (Alt+c)

Alt+c kısayolu, mesaj listesindeki sütunların sırasını değiştirmenize ve sütun eklemenize veya kaldırmanıza olanak tanıyan bir iletişim kutusu görüntüler.

Kullanmak için önce kendinizi mesajlar listesine veya klasörlerin ağaç yapısına yerleştirin, ardından Alt+c tuşlarına basın;

Sütun düzeni iletişim kutusu görünür. Sütun listesinin yanı sıra "Yardım", "sütunlar" ve "Kapat" düğmelerinden oluşur.

"Sütunlar..." düğmesi yerel Thunderbird "Görüntülenecek sütunları seçin" menüsünü görüntüler

Sütun listesindeyken, aşağıdaki klavye kısayolları kullanılabilir:

* Sol ok: "Görüntülenecek sütunları seçin" adlı onay kutusu menüsünü görüntüler. Bu kısayol, "Sütunlar..." düğmesine karşılık gelir;
* Boşluk: seçilen sütunu taşımak için Boşluk tuşuna basın, ardından başka bir sütuna gidin ve sütunu oraya yerleştirmek için tekrar Boşluk tuşuna basın. Bu işlem kes ve yapıştır işlemine benzer;

Ayrıca şu doğrudan hareket kısayollarına sahipsiniz:

* Kontrol + yukarı ok veya aşağı ok: seçili sütunu bir konum yukarı veya aşağı hareket ettirin;
* Control + Home veya End: seçilen sütunu listede yukarı veya aşağı taşır;
* Control + Önceki sayfa veya Sonraki sayfa: seçilen sütunu üç konum yükseltir veya alçaltır;

Bu hareketleri gerçekleştirmek için, sütunlar aslında fare ile sürükleyip bırakarak taşınır. Her 10 işaretçi hareketinde bir milisaniyelik bir bip sesi oluşur;

"Görüntülenecek sütunları seçin" menüsü mevcut olduğunda, aşağıdaki yeni klavye kısayollarına sahipsiniz:

* Sağ ok: sütun düzeni iletişim kutusunu görüntüler;
* Boşluk: menüde seçilen sütunu kontrol eder veya işaretini kaldırır. Enter tuşu yine aynı davranışı üretir;

Bu nedenle, sol ve sağ oklarla, sütunları seçmek için menü ile bunların düzenlenmesi için iletişim kutusu arasında geçiş yapmak çok kolaydır;

<a name="smartReply">

### SmartReply: Control+r tuşlarına basarak tüm posta listelerini yanıtlayın

Google Grupları gibi bir posta listesine yanıt vermek için Control+Shift+l tuşlarına basmayı unutanlardansanız, bu özellik sizi bir iletiyi gönderene farkında olmadan özel olarak yanıt vermekten kurtaracaktır.

yine de Control+r tuşlarına şu şekilde basabilirsiniz:

* tek tuş vuruşu: listeye cevap vermek için;
* çift dokunma: mesajı gönderene özel olarak yanıt vermek için;
* Listeden gelmeyen bir mesajın göndericisine tek tuşla cevap verebilme;

Notlar :

Bu kısayollara tek veya çift dokunma arasındaki fark, GoogleGroups'ta çalışır.Çerçeveciler ve Serbest Listeler.

Bu üç listeden birine tek bir dokunuşla, düzenleme penceresi açılmadan önce "listeye" ifadesini duyacaksınız.

gönderenin cevabınızı özel olarak almaması için bir listeyi yanıtlarken "Tümünü yanıtla" komutunun kullanılmaması da tavsiye edilir;

Son olarak, Control+r'nin olağan davranışını bulmak istiyorsanız:

* Seçenekler menüsünü görüntülemek için [Shift+Quotes](keyequiv_tr.html#aboveTab) tuşlarına basın;
* "Chichi ve Thunderbird+ alt menüsü için Devre Dışı Bırakma" öğesini seçin;
* "Mesaj listesi: SmartReply yok" seçeneğinin işaretini kaldırmak için Enter'a basın;

### Seslendirilen a, j, m kısayolları

* a: Seçilen mesajı sesli olarak arşivler. Bu işlemi geri almak için Control+z tuşlarına basın;
* j: bu mesajı seslendirme ile spam olarak işaretle;
* Shift+j: Seslendirme ile bu mesajı kabul edilebilir olarak işaretleyin;
* m: seçili mesajları okunmadı olarak işaretler. Shift+m ​​​​okundu olarak işaretler;

<a name="klasörAğacı">

## Klasör Ağacı

<a name="okunmamış Klasörler">

### Okunmamış mesajlar içeren klasörler arasında hızlı gezinme (Alt+Aşağı Ok, Alt+Yukarı Ok)

Klasör ağacındayken şu tuşlara basabilirsiniz:

* Alt+aşağı ok: okunmamış mesajların olduğu bir sonraki klasöre gitmek için;
* Alt+yukarı ok: okunmamış mesajların bulunduğu bir önceki klasöre gitmek için;
* Space, Chichi yüklü değil: seçilen klasör okunmamış mesajlar içeriyorsa, listedeki ilk okunmamış mesajı seçer;
* Space, Chichi kurulu: klasörde okunmamış mesaj yoksa, Chichi'nin okunmamış klasörlerin listesini göstermesi dışında aynıdır.<br>
Bu listedeki okunmamış bir klasörde enter tuşuna basmak, mesaj listesindeki o klasördeki ilk okunmamış mesajı etkinleştirir; <br>
Bu, hangi klasörden okumaya başlamak istediğinize karar vermeden önce hangi klasörlerin mesaj aldığını hızlı bir şekilde görmenizi sağlar;<br>

Bu bağlamda, şu iki diyaloğa da bakın:

* Filtrelenmiş Hesap ve Klasör Listeleri İletişim Kutusu (F12)
* Ana ağaçtaki klasörlerin 4 türe göre listesi (F7, NVDA+F7 veya Shift+F12)

Not: Çok sayıda klasörle Chichi, bu iki iletişim kutusunun aksine anlıktır;

<a name="klasörDlg">

### Filtrelenmiş Hesap ve Klasör Listeleri İletişim Kutusu (F12)

Bu iletişim kutusu, hesapları ve bunlarla ilişkili klasörleri iki ayrı listede görüntüler. Bunları bir anahtar kelimeye göre filtreleyebilir veya klasör listesini okunmamış mesajları olanlarla sınırlayabilirsiniz.

Varsayılan görüntüleme modunu yapılandırma:

Çoğu zaman yalnızca okunmamış mesajları içeren klasörleri görüntülemeyi planlıyorsanız, önce klasör ağacına veya mesaj listesine gidin, ardından [Shift+Quotes](keyequiv_tr.html#aboveTab) ve ana pencerenin seçenekler alt menüsünde şu başlıklı öğeyi doğrulayın: Yalnızca okunmamış mesajları olan klasörleri göster.

Temel diyalog kullanımı:

* İletişim kutusunu görüntülemek için ana pencereden F12'ye basın.
* Klasörlerin varsayılan görüntüsünü okunmamış mesajlarla yapılandırdıysanız, bunlar şu listede görüntülenecektir: Hesap klasörleri;
* Aksi takdirde, tüm hesaplardaki tüm klasörler bu listeye dahil edilecektir;
* Bir klasör adının ilk harfine basarak bu listede gezinebilirsiniz;
* Ağaç yapısında gösterilmeyen klasörlerin burada da listelenmeyeceğini unutmayın. Bu, örneğin klasörler, hesaplar ve klasörler ağacındaki daraltılmış bir hesaba ait olduğunda olur;
* Bu noktada ilgilendiğiniz klasörü bulduysanız, ağaç yapısında seçmek için üzerinde Enter tuşuna basın. Klasör üzerinde tek bir sol tıklama simülasyonu yapmak için Alt+g tuşlarına veya tek bir sağ tıklama simülasyonu için Alt+d tuşlarına da basabilirsiniz;


Ekran modlarını değiştir:

* İstediğiniz zaman hangi görüntüleme modunda olduğunuzu hatırlatmak için "Geri al" tuşuna basın. Bilgileri duyduktan sonra, klasörler listesine dönmek için bu düğmeye tekrar basın;
* Ekranı "yalnızca okunmamış klasörlerle" modundan "tüm klasörler" moduna veya tam tersine geçirmek için F12'ye basın;
* "Tüm klasörler" modunda, hesaplar soldaki listede ve seçilen hesabın klasörleri sağdaki listede görüntülenir. Bir listeden diğerine geçmek için sol ve sağ okları kullanın;
* "Tüm hesaplar" adlı bir sanal hesap seçilir ve odak, tüm hesapların tüm klasörlerini içeren klasörler listesine yerleştirilir. Bu listedeki her klasör için ait olduğu hesabın adı belirtilir;


Anahtar kelime filtrelemeyi kullanma:

* Önceden, yukarıda açıklandığı gibi "Tüm klasörler" moduna geçmek büyük olasılıkla fayda sağlayacaktır;
* Aşağıda "Önceki sayfa" ve "Sonraki sayfa" tuşlarını dönüşümlü olarak kullanabilirsiniz;
* Bir listeden, filtre ifadesinin düzenleme alanına geri dönmek için "Önceki sayfa" tuşuna basın;
* Bir ifade girin ve ardından filtrelemeyi yürütmek için "Sonraki Sayfa" tuşuyla doğrulayın;
* Sonuçlar, klasörler listesinde görüntülenir. Klasör bulunamadıysa şunu duyarsınız: Sonuç bulunamadı. Bunu beklemiyorsanız, tüm klasörlerin görüntüleme moduna geçmeyi unutmuş olabilirsiniz;
-Son olarak, klasör ağacında istediğiniz klasörü seçmek için enter tuşuna basın. Yukarıda bahsedildiği gibi, Alt+g veya Alt+d tuşlarına basarak klasör üzerinde sol veya sağ tıklama simülasyonu yapabilirsiniz;#### Belirli klasörler, okunmamış klasörler listesinden hariç tutuluyor

Yukarıda bahsedildiği gibi, nadiren erişilen veya hiç erişilmeyen klasörleri okunmamış mesaj içeren klasörler listesinden çıkarabilirsiniz.

Tek yapmanız gereken, adının sonuna bir çizgi ekleyerek hariç tutulacak bir klasörü yeniden adlandırmaktır.

Burada, yeniden adlandırılan bu klasör bir mesaj filtresinin parçasıysa, Thunderbird'ün bu değişikliği hesaba katmak için bu filtreyi otomatik olarak değiştireceğini belirtmek gerekir.


<a name="klasör Listesi">

### Ana ağaçtaki klasörlerin 4 türe göre listesi (F7, NVDA+F7 veya Shift+F12)

Klasör ağacında veya mesaj listesindeyken, bu komut aşağıdaki dört düzeni benimseyen klasörlerin listesini içeren bir iletişim kutusu görüntüler:

* Yalnızca okunmamış iletilerde (düz liste), Alt+n;
* Tüm klasörler (düz liste), Alt+t;
* Yalnızca okunmamış iletilerde (dolu ağaç), Alt+o;
* Tüm klasörler (tam ağaç), Alt+u;


Okunmamış mesajları olan klasörler için Taslaklar, Çöp Kutusu ve kısa çizgiyle biten adlara sahip klasörler listeden çıkarılır;

Bu türlerden birini etkinleştirmek için ilgili klavye kısayoluna veya Shift+Tab tuşlarına ve ardından ok tuşlarına basarak modu değiştirebilirsiniz.

Seçilen tip, bu iletişim kutusunun bir sonraki görüntülenmesinde hafızaya alınacak ve etkinleştirilecektir;

Listeyi anahtar kelimeye göre de filtreleyebilirsiniz. Giriş alanına ulaşmak için Tab veya boş Alt+e tuşlarına basın.

Düz bir listede veya ağaç yapısında gezinme, yukarı ve aşağı okların yanı sıra bir klasör adının baş harfiyle yapılır;

Ana ağaçta seçilen klasörü etkinleştirmek için üzerinde Enter tuşuna basmanız yeterlidir.

İpucu: Okunmamış mesajların bulunduğu bir klasörde Enter tuşuna bastıysanız, mesaj tablosundaki ilk okunmamış mesajı seçmek için Boşluk tuşuna basın;
<br>
Algılanan :

Bu iletişim kutusunu açan kısayol tuşları kaldırılabilir ve NVDA'nın Hareket Ayarları iletişim kutusundan başka bir kısayol eklenebilir. Aşağıdaki gibi ilerleyin:

* Önce Thunderbird penceresini ön plana yerleştirin;
* NVDA menüsünü açın ve "Tercihler"i seçin;
* Alt menüde, şunları doğrulayın: Komut hareketleri";
* İletişim kutusunda, şunu duyana kadar t harfine basın: Thunderbird;
* Bu dalı genişletmek için sağ oka basın;
* Şu öğeye ilerleyin: "Thunderbird'ün ana ağaç yapısındaki klasörlerin listesini birkaç türe göre görüntüleyin. 4'te 2 azaltılmış 1. düzey", ardından bu düzeyi genişletmek için sağ oka basın;
* Sekerek "Ekle" düğmesine gidin, onaylayın ve ardından yeni iletişim kutusunda bir kontrol hareketine basın;
* Seçiminizi doğrulamak için Enter tuşuna basın;
* Komutlar listesine geri dönün, yeni komut hareketinizin varlığını kontrol edin;* Diyaloğu Tamam düğmesiyle kapatın.

<a name="uyarılar">

## Uyarılar erişilebilir hale getirildi

Müdahalenizi gerektiren uyarılar için düğmelere erişilebilir ve ok tuşları kullanılarak bunlar arasında gezinilebilir:

* Thunderbird için modüllerin kurulumu: "Yükle" düğmesi seçilidir ve kuruluma devam etmek için üzerinde Enter tuşuna basmanız yeterlidir;
* Yeni Thunderbird güncellemesi: bu uyarıya da erişilebilir;
* Mesajın alındığına dair bir onay talebi: bu, ana pencere için [Shift+Quotes](keyequiv_tr.html#aboveTab) / seçenekler menüsündeki bir seçenek aracılığıyla göz ardı edilebilir ;;
* Mesajlarda uzak içeriğin görüntülenmesini engelleme: "Seçenekler" düğmesi seçilir ve mesaja aşağıdaki cümle eklenir: İpucu: Görünüm menüsünü açın, Mesaj gövdesine gidin ve alt menüde basit HTML'yi doğrulayın . Önerilen ayarlar uygulandığında, bu uyarı artık görüntülenmez;

Mesaj listesine göz atmayı engelleyen uyarılar için:

* Uyarı Bu bir taslaktır: bu gereksiz uyarı silinmiştir;
* Thunderbird bu mesajın sahte olduğunu düşünüyor: bu duyuru insan sesine yakın bir frekansta (200 Hertz) iki kısa tonla değiştirildi. Mesajı kabul edilebilir veya istenmeyen yapmak için [Alıntılar](keyequiv_tr.html#aboveTab) tuşuna basın ve "Uyarı" alt menüsünden istediğiniz eylemi seçin;

<a name="sekmeler">

## Sekme Klavye Kısayolları

Yeni komutlarla birlikte, sekmeler bu örnekte olduğu gibi duyurulur: Sekme 1/4, Gelen Posta.

* Control+Tab ve Control+Shift+Sekme: sonraki veya önceki sekmeye gider;
* Control+a sayı: sekme çubuğunda sıra numarasına karşılık gelen sekmeyi seçer. Açık sekme sayısından daha büyük bir sayıya basarsanız sonuncuya yerleştirilirsiniz;
* Control + [Equal](keyequiv_tr.html#bs1): bir menüdeki açık sekmelerin listesini görüntüler. Bir sekme adına gitmek için enter tuşuna basın;
* Alt + [Equal](keyequiv_tr.html#bs1): sekme çubuğunun içerik menüsünü görüntüler. Özellikle şu komutları içerir: Etkin sekmeyi kapat ve Diğer sekmelerimi kapat;
* Control+w, Control+backspace veya Control+F4: etkin sekmeyi kapatın;
* Control+j: sabit sürücünüze kaydedilen ekleri ve indirmeleri gruplandıran "Kayıtlı dosyalar" sekmesini açar;

<a name="tabAddons">

## Eklentiler sekmesi

Eklenti, Thunderbird için eklentileri bulmayı ve kurmayı kolaylaştırır.

* "Eklentiler" sekmesinde bir modül adı girin ve ardından Enter tuşuna basın;
* Eklenti, arama sonuçları sekmesinin açılmasını bekleyecek ve ardından bulunan ilk eklentiyi seçmeye çalışacaktır;
* daha somut olarak,[Inbox modülü kurulumuyla Başlayın](#stwInstall) örneğini okuyabilirsiniz;

<!-- Çeviriciler: yazma penceresi = Yazma penceresi -->
<a name="writeWnd">

## Oluştur penceresi

Düzenleme penceresi açıldığında, aşağıdaki klavye kısayolları mevcut olmasına rağmen özel bir şey fark edilmez:

* Escape: düzenleme penceresini kapatır;
* Adresleme bölgelerine danışma: Alt + bir sayıya basmak başlığı duyurur, iki kez basmak ilgili giriş bölgesine odaklanır:<br>
Alt+1: Gönderen: e-posta adresleriniz listesinde görünen e-posta adreslerinizden biri;<br>
Alt+2: için:<br>
Alt+3: ek adları. İki basış, eklerin listesine odaklanır;<br>
diğer rakamlar, şu gibi isteğe bağlı üstbilgilere erişim sağlar: kopyala, gizli kopyala ve yanıtla;
* [Alıntılar](keyequiv_tr.html#aboveTab) mesaj metninde: aşağıdaki bağlamsal menüyü görüntüler: - Posta araç çubuğu, ardından alt menüde: Gönder, Yazım Denetimi, Ekle, Güvenlik, Kaydet.<br>
Alt menüde metin biçimlendirme: (Stilleri) Paragraf, Madde işaretli listeyi uygula veya kaldır, Numaralı listeyi uygula veya kaldır, Yazı Tipleri, Girintiler, bağlantı, resim, bağlantı, yatay çizgi veya tablo ekle.

<br>
Not: Bu menü, [Shift+ Quotes](keyequiv_tr.txt) tuşuna bir veya iki kez hızlıca basarak elde edilen oluşturma penceresi için seçenekler menüsündeki ayara bağlı olarak [Quotes](keyequiv_tr.html#aboveTab) tuşuna bir veya iki tuş vuruşuyla elde edilir. html#aboveTab);

<a name="spellDlg">

### Yazım denetimi iletişim kutusu: F7

El hareketini kısıtlayan kısayol tuşları eklendi. Odak, değiştirilen sözcük düzenleme alanındayken, aşağıdaki kısayol tuşlarına basabilirsiniz:

* Enter: "Değiştir" düğmesini etkinleştirir;
* Shift+Enter: "Tümünü değiştir" düğmesini etkinleştirir;
* Control+Enter: "Yoksay" düğmesini etkinleştirir;
* Shift+Control+Enter: "Tümünü yoksay" düğmesini etkinleştirir;
* Alt+Enter: "Sözcükleri sözlüğe ekle" düğmesini etkinleştirir;


Enter tuşunun bu kombinasyonlarını hatırlamak için Kontrol, "Yoksay" eylemine atıfta bulunur ve Shift'in varlığı "tüm oluşumları" belirtir.


Ayrıca, Alt+yukarı ok kısayolu şu sözcükleri heceler:

* 1 basış sözcükleri normal hızda heceler;
* 2 basış hızlı bir şekilde kelimeleri heceler;
* 3 basış, yanlış yazılmış kelimeyi başka bir düzenleme alanında analiz edilmek üzere panoya kopyalar;

<a name="menüler">

## ThunderbirdPlus Seçenekleri ve Komutları Menüleri

<a name="optMenu">

### Seçenekler Menüsü([Shift+Tırnaklar](keyequiv_tr.html#aboveTab))
 

Ana pencere için seçenekler:

* Birden fazla 'RE' sözünü bir araya getirin: örneğin, Re: Re: Re: 3Re:'ye dönüştürülecek;* Konu sütunundaki 'RE' ibarelerini silin:
* 'RE' ifadelerindeki 2 noktayı silin:
* Mesaj listesindeki kişilerin isimlerini temizleyin: Muhatapların isimlerini dinlemeyi daha az yorucu hale getirmek için sayıları ve belirli özel karakterleri kaldırın;
* Sütunlar arasına noktalama işaretleri ekleyin: mesaj listesinin bir satırını duyururken aralarındaki küçük bir duraklamayı işaretlemek için belirli sütunların arasına virgül eklenir;
* Çalma Listesi Adlarını Gizle: Her çalma listesi için farklı bir klasör kullanırken daha kolay dinleme için parantez içindeki liste adlarının duyurusunu kaldırır. Aksi takdirde, bir posta listesinin adı, bir iletinin konusunda birden çok kez geçiyorsa yalnızca bir kez söylenir;
* Mesajların konusunda gizlenecek kelimeleri düzenle: mesajların konusunda duyurulmayacak kelimeleri eklemenizi veya silmenizi sağlayan bir giriş kutusu açar. Örneğin, *** Spam ***'in Spam olarak bildirilmesi için * ekleyin;
* 'İstenmeyen durum' sütununda görüntüleniyorsa 'istenmeyen' olarak duyurun: mesaj tablosunda "istenmeyen durum" sütunu varsa, bu seçenek "İstenmeyen" durumunun duyurulmasına izin verir veya vermez;
* Okunmamış bir klasördeki boşluk, mesaj listesinin başından itibaren ilk okunmamış mesajı arar: Varsayılan olarak, bu seçenekle ilgili komut dosyası, mesaj listesindeki bir sonraki okunmamış mesajı seçmek için "n" komutunu gönderir. Thunderbird mutlaka listedeki ilk okunmamış mesajı seçmez. Bu seçeneği işaretlediğinizde eklenti, bazı PC'lerde duyulabilen bir sapma yaparak klasördeki ilk okunmamış mesajı seçecektir;
* Klasör ağacında ilk gezinmeyi kullanmayın: "Klasör tuşunda hızlı gezinme" eklentisini kullanıyorsanız bu seçenek kullanışlıdır;
* Dolaylı baş harflere göre tarama: klasör ağacında bir harf veya rakama basar basmaz bir klasör adı giriş kutusu görüntüler. Bu seçenek devre dışıysa, z harfine basarak bu arama kutusunu görüntüleyebilirsiniz;
* Onay isteklerini yoksay: bu seçenek etkinleştirilirse, mesaj listesinden bir mesaj seçildiğinde onay talebi bölmesi susturulur;
* Shift+F6'yı escape ile taklit etmeyin: ana pencerede paneller arasında gezinirken escape tuşunun kullanımını devre dışı bırakır;
* 'Ağaç Klasörler' iletişim kutusunda yalnızca okunmamış klasörleri göster a: F12 tuşu aracılığıyla bu iletişim kutusunu her görüntülediğinizde yalnızca okunmamış iletileri olan klasörlerin görüntülenmesini sağlar;
* ayrı okuma penceresi: NVDA'nın çökmesine neden olursa mesajı otomatik olarak okuma: Varsayılan olarak,mesaj listesinden Enter tuşuna basarak bir mesajı açtığınızda, yeni pencere açıldığında mesajın incelikli bir okuması başlar. Bazı bilgisayarlarda ve e-posta hesabı IMAP olarak ayarlandığında NVDA çökebilir. Bu seçenek işaretlendiğinde, engellemeyi önlemek için bu otomatik oynatma devre dışı bırakılır.<br>
Bu pencereyi açarken bir donma yaşarsanız, otomatik oynatma başlamadan önceki gecikmeyi uzatabilirsiniz. Bunu yapmak için başka bir değer girmek üzere Alt+d tuşlarına basın. Bu engellemeyi kaldıramıyorsanız, bu seçeneği işaretleyin;

<br>
Oluştur penceresi seçenekleri:

* Yazım denetimi: yanlış yazılmış sözcük ve önerilen sözcük: bu seçenek, yazım denetimi iletişim kutusundaki duyuruları değiştirir;
* Yazarken gelişmiş Yazım Denetimini etkinleştirin: bu seçenekle ilgili komut henüz NVDA sürüm 2022.1'de çalışmıyor;
* Esc tuşu yazılmakta olan mesajı kapatır; işaretli l
* Bağlamsal menüyü görüntülemek için tek tuş vuruşu, [Alıntılar](keyequiv_tr.html#aboveTab) veya [Shift+Quotes](keyequiv_tr.html#aboveTab) veya bunların yerine geçenleri yazmak için çift tuş vuruşu: bu seçenek bağlamsal menüyü [Quotes](keyequiv_tr.html#aboveTab) tuşuna basarak [Quotes](keyequiv_tr.html#aboveTab) ve [Shift+Quotes](keyequiv_tr.html#aboveTab) karakterlerini nadiren yazarsanız daha pratik olacaktır;

<br>
Güncelleme seçenekleri:

Bu seçenek, Thunderbird+ otomatik güncellemelerini devre dışı bırakmanıza veya yeniden etkinleştirmenize olanak tanır;

<br>
Chichi ve Thunderbird+ için devre dışı bırakmalar:

Bu seçeneklerin ana amacı, yinelenen özelliklerden kaçınarak Thunderbird+ ve Chichi arasında iyi bir birlikteliğe izin vermektir. Ancak bunları tercihlerinize uyacak şekilde sorunsuz kullanabilirsiniz;

Aşağıdaki "klasörler" terimi, klasör ağacını ifade eder;

* Klasörler: Boşluk, listedeki bir sonraki okunmamış mesajı seçmez ve okunmamış klasörler listesini göstermez d: Chichi'nin henüz bağımsız bir eşdeğeri yoktur;
* Klasörler: baş harflerle gezinme yok d: bu seçeneği etkinleştirerek, Chichi kullanılacaktır. Yalnızca yukarıdan aşağıya çalışır ve etkinleştirilen klasörün ait olduğu hesabın adını söylemez;
* Mesaj listesi: Boşluk önizleme bölmesi mesajını okumaz l: bu seçeneği işaretlerseniz, Chichi önizleme bölmesi mesajını konuşur. Thunderbird+'dan farklı olarak, bu oynatma sterilize edilmeyecektir. Öte yandan, F4 ve Alt+aşağı ok, Thunderbird+'ın düzenli okumasına hitap etmeye devam edecek;
* Mesajları listele: SmartReply yok:Control+r ile bir posta listesine tek dokunuşla veya göndereni Control+r ile çift dokunuşla yanıtlamaya izin veren özelliği devre dışı bırakır,
* Mesajları listele: hızlı filtre çubuğunu yönetme: aşağı ok ile filtre seçeneklerine erişimi kaldırır;
* ana pencere: Sekme sonraki bölmeye taşınmaz: bu seçenek, klasör ağacı, mesaj listesi ve başlıklar ve mesaj bölmesi arasında gezinme ile ilgilidir;
* Ana pencere: escape tuşunun varsayılan davranışını geri yükleyin. Bu, özellikle yukarıda belirtilen bölümler arasındaki gezinme ile ilgilidir;
* Thunderbird'ü Control+w veya Control+F4 ile kapatmaya izin ver: bu seçeneği işaretleyerek, bu iki kısayol açık yalnızca bir sekme kaldığında Thunderbird'ü kapatır. Bu davranış bazı insanlar için utanç vericidir;

<br>
Yedekleme ve geri yükleme seçenekleri:

* Geçerli yapılandırmayı yedekle: eklentinin .ini dosyasını bir .inibak dosyasına kopyalar;
* Kaydedilen yapılandırmayı geri yükleyin r: .inibak dosyasını .INI dosyasına kopyalayın ve parametreleri yeniden yükleyin;
* Yapılandırmayı sıfırla: eklentinin varsayılan ayarlarını yeniden yükler. Önceden, henüz yoksa bir yedek alın;

<a name="cmdMenü">

### Komutlar Menüsü (Alıntılar)

* Mesaj listesi sütunlarını seçin ve düzenleyin: "Görüntülenecek sütunları seçin" adlı Thunderbird onay kutusu menüsünü görüntüler. Bir sütun adından, sütun düzeni iletişim kutusunu açmak için sağ oka basın;
* Desteğe yazın: Fransızca veya İngilizce. Bu komut, eklenti desteğine önceden adreslenmiş bir yazma penceresi açar. Bu, yalnızca Thunderbird'ün varsayılan e-posta istemciniz olarak doğru şekilde ayarlanması durumunda çalışır;

<a name="başlangıç">

## Geliştirilmiş Thunderbird başlatma

Doğal olarak, Thunderbird'ün son kapanışından sonra, son aktif sekmede ve hiçbir şeyi etkinleştirmeden başlar, bu oldukça tatsız.

Rahat bir başlangıç ​​yapmak için doğrudan Thunderbird'e yüklenen iki eklenti vardır:

* Yannick tarafından geliştirilen Chichi: Bu modül tavsiye edilir çünkü diğer pek çok erişilebilirlik özelliği sunar ve ThunderbirdPlus onunla etkileşime girecek şekilde tasarlanmıştır;
* Gelen kutusuyla başlayın: Chichi kullanmıyorsanız, bu modül iyi bir iş çıkarır;

<a name="bok">

### Chichi ile

Chichi'yi kullanmak için, [Chichi sayfasının](https://www.rptools.org//Outils-DV/thunderbird-chichi-en.html) İndirme ve Yükleme bölümünü ve Başlangıç ​​Klasörünü Ayarla bölümünü okuyun;

<a name="stwi">

### ile Gelen kutusuyla başla

Ekim 2022 itibarıyla Thunderbird 102 için bu eklentinin en son sürümü 2.5.2 idi.

Özellikler :

* Tesis :Thunderbird'ün "Eklentiler" sekmesinde adını arayarak;
* Başlangıç ​​klasörü: her zaman aynı, modül ayarlarında seçilen hesabın gelen posta klasörü veya birleştirilmiş klasör;
* Otomatik odaklama: modül seçeneklerindeki ayara bağlı olarak, mesaj listesindeki son mesaja veya ağaç yapısındaki "Gelen posta" klasörüne. Bu ikinci seçenek varsayılan olarak seçilidir;
* Ayarlamalar: daha az kolay erişim. Eklentiler sekmesine gitmeli, yüklü eklentiler listesinde "Gelen kutusuyla başlat"ı seçin ve ardından yeni bir "Ayarlar Gelen kutusuyla başla" sekmesini açan "Eklentiler seçenekleri" düğmesine basarak enter tuşuna basmalısınız.
<br>Bir açılır liste, Thunderbird başladığında gelen posta klasörünün seçileceği e-posta hesabını seçmenizi sağlar,
<br>Üç radyo düğmesi, mesaj listesindeki son mesaj veya ilk okunmamış mesaj veya ağaç yapısındaki klasör arasındaki odağı seçmenize olanak tanır;

<a name="stwInstall">

Tesis :

* Thunderbird'de "Araçlar" menüsünü açın ve ardından şunları doğrulayın: Eklentiler ve temalar;
* Modül Yöneticisi sayfasında kendinizi arama alanına yerleştirin. Navigasyon modunda, hızlı bir şekilde ulaşmak için e harfine basabilirsiniz;
* yaz: Inbox ile başlayın ve Enter'a basın;
* Thunderbird+4'ünüz varsa, sonuçlar sekmesinde aradığınız modülü seçmesi için biraz bekleyin;
* Aksi takdirde, örneğin "Inbox ile başla::Ara::Thunderbird için Modüller" sekmesini manuel olarak seçin. daha sonra aradığınız modülün adının bulunduğu 3. seviye başlığa ulaşana kadar 3 veya tırnak tuşuna basın;
* Aşağı ok ile "Thunderbird'e Ekle" bağlantısına ilerleyin ve ardından Enter tuşuna basın;
* Prosedürü takip edin ve ardından Thunderbird'ü yeniden başlatın;
* Her şey yolunda giderse, Thunderbird ana sekmeyi açar ve mesaj listesine odaklanır;

Gelen Kutusuyla Başlat seçeneklerini ayarlayın:

* "Ek Modül Yöneticisi" sekmesine dönün;
* Gerekirse, navigasyon moduna geçmek için arama alanından çıkın;
* "Yüklü modüller listesinde Inbox ile başla;
* Ardından düğmeyi doğrulayın: Modül seçenekleri. Bu, şu başlıklı yeni bir sekme açar: Gelen Kutusuyla Başla, Ayarlar;
* İşte varsayılan olarak görüntülenenler:

<!-- Çevirmenler: İngilizce için, diğer çevirmenlere ne yapmaları gerektiğini göstermek için "Fransızca tercüme" bölümünü yorumlayın -->
İngilizce :

Inbox ile Başlayın - Ayarlar

Lütfen Thunderbird başladıktan sonra gelen kutusunun görüntüleneceği hesabı seçin.

açılır liste :\<ilk e-posta hesabınız\>

Seçin ve şuna odaklanın:

işaretlenmemiş tıklanabilir radyo düğmesi: en son* mesaj.

Klasör ağacındaki gelen kutusu klasörü tıklanabilir radyo düğmesi işaretsiz.
boş
işaretli radyo düğmesi: ilk okunmamış mesaj.

* "Son" tanımı: Gelen kutusuna atılan son mesaj (tarihten bağımsız)
mesajın).

Gelen kutusu mesaj içermiyorsa, klasör ağacındaki gelen kutusu klasörü seçilecek ve
odaklanmış.


Fransızca Tercüme:

Gelen Kutusu - Ayarlar ile başlayın;

Thunderbird başladığında Gelen Posta klasörü görüntülenecek olan hesabı seçin;

açılır liste: \<ilk e-posta hesabınız\>

Seç ve odaklan:

işaretlenmemiş tıklanabilir radyo düğmesi: Listedeki son mesaj;

radyo düğmesi işaretlenmemiş tıklanabilir Klasör ağacındaki Gelen Posta klasörü;

işaretli radyo düğmesi: Listedeki ilk okunmamış mesaj;

Gelen Posta klasörü mesaj içermiyorsa, bu klasör klasör ağacında odak alır;


Ayarlarınızı yaptıktan sonra Thunderbird'ü yeniden başlatın.


AltGr+[Alıntılar](keyequiv_tr.html#aboveTab) özellikli yerleşik Thunderbird başlatıcısı:

Kolaylık ve hız için AltGr+[Quotes](keyequiv_tr.html#aboveTab) tuşlarına basarak Thunderbird'ü başlatabilirsiniz.

Bu kısayol tuşu, NVDA'nın AltGr ile sınırlı olan Windows kısayol tuşlarına göre daha fazla değiştirici tuş seçme özgürlüğü sunan Komut Hareketi Yöneticisi aracılığıyla yapılandırılabilir;

Başka bir kontrol hareketi eklemek için şu adımları izleyin:

* Önce Thunderbird penceresini ön plana yerleştirin;
* NVDA menüsünü açın ve "Tercihler"i seçin;
* Alt menüde Enter tuşuna basın: Kontrol hareketleri";
* İletişim kutusunda, şunu duyana kadar t harfine basın: "Thunderbird, Başlatıcı";
* Bu dalı genişletmek için sağ oka basın;
* Şu öğeye ilerleyin: "Thunderbird'ü Başlat", ardından bu seviyeyi genişletmek için sağ oka basın;
* Sekerek "Ekle" düğmesine gidin, onaylayın ve ardından yeni iletişim kutusunda bir kontrol hareketine basın;
* Seçiminizi doğrulamak için Enter tuşuna basın;
* Komutlar listesine geri dönün, yeni komut hareketinizin varlığını kontrol edin;
* Diyaloğu Tamam düğmesiyle kapatın.

Notlar :

* Thunderbird başlatıcısı, yalnızca Thunderbird.exe yolları tahmin edilebilir olan yüklü Thunderbird sürümü için tasarlanmıştır.
* 64 bit Windows yapılandırmasında, sisteminizde hem 64 bit hem de 32 bit sürümler yüklüyse, eklenti Thunderbird'ün 32 bit sürümünü başlatmaz;
<!-- links section -->


[1]: https://github.com/RPTools-org/ThunderbirdPlus/releases/download/v4.6/thunderbirdPlus-4.6.3-TB102.nvda-addon

[2]: https://github.com/RPTools-org/ThunderbirdPlus/
