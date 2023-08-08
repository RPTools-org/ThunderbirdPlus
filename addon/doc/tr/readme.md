# Thunderbird+

* Yazarlar: Pierre-Louis Renaud (Thunderbird 78'den 102'ye) & Cyrille Bougot (TB 102), Daniel Poiraud (TB 78'den 91'e), Yannick (TB 45'ten 60'a);
* Bağlantılar: [Kullanım kılavuzu][4] ;
  [RPTools.org'daki değişiklik günlüğü][5] ;
  [Fransızca veya İngilizce iletişim kurun][6] ;
* [Kararlı sürümü indirin][1]
* [En son sürümü RPTools.org'dan indirin][3]
* NVDA Uyumluluğu: 2019.3 ve sonrası;
* Thunderbird uyumluluğu: 102.x sürümleri;
* [GitHub'daki kaynak kodu][2]

## Açıklama

Bu eklenti, Mozilla Thunderbird e-posta istemcisinin rahatlığını ve NVDA ile verimli kullanımını büyük ölçüde geliştirir.

İyileştirmeler aşağıdaki hususlarla ilgilidir:

### İşitsel Konfor

* "Şu veya bu şekilde istenen onay" uyarıları bir seçenek aracılığıyla devre dışı bırakılabilir;
* "Bu bir taslaktır" ve "Thunderbird bu iletinin sahte olduğunu düşünüyor" uyarıları basitçe göz ardı edilir;
* Seçenekler, posta listesi ad duyurusunu devre dışı bırakmanıza, "RE" sözlerini kaldırmanıza veya gruplandırmanıza, sayıları ve diğer sinir bozucu özel karakterleri kaldırarak karşılık gelenlerin adlarını temizlemenize olanak tanır;

### Ana Pencerede Gezinme

* Sonraki panele geçiş TAB tuşu kullanılarak yapılırken, Escape tuşu önceki panele döner. Bu, F6 ve Shift+F6'dan daha rahattır.
* Sekmelerin Control+Sekme ve Control+sayı ile seçimi bu örnekte olduğu gibi konuşulur: Sekme 1 / 4, gelen kutusu;
* Bir klavye kısayolu, bir menüdeki sekmeleri listeleyerek bunlardan birini kolayca etkinleştirmenizi sağlar;
* Sekmeler çubuğunun içerik menüsünü görüntülemek için bir klavye kısayolu kullanılır;

### Klasör Ağacı görünümü

* Alt+Aşağı Ok ve Alt+Yukarı Ok, okunmamış iletileri içeren klasörler arasında gezinmenizi sağlar;
* Bir harf veya sayı yazmak, adı o karakterle başlayan bir sonraki klasörü seçer. Shift tuşu ile aşağıdan yukarıya doğru hareket gerçekleşir. Ayrıca klasörün ait olduğu hesabın adı duyurulur;
* Okunmamış iletiler içeren bir klasörde Boşluk çubuğuna basmak, ileti listesindeki ilk okunmamış iletiyi seçer;
* Hesaplar ve ilişkili klasörleri için iki iletişim kutusu, bunları anahtar sözcüğe göre filtrelemenize veya yalnızca okunmamış iletilere sahip klasörleri görüntülemenize olanak tanır;

### İleti Listesi

* İleti listesindeki sütunları ve düzenlerini seçmek, basit bir iletişim kutusuyla erişilebilir hale getirilir;
* İleti listesinin sütunlarını görüntüleme: kısayollar, alfanümerik tuş takımında bir rakam yazarak gönderenin adını, ileti konusunu veya tarihini kolayca dinlemenizi, hecelemenizi veya kopyalamanızı sağlar. Örneğin, 1 veya diğer rakam düğmelerine düğmelerine tek bir basış göndereni duyurur, iki basış adı heceler ve üç basış onu panoya kopyalar;
* F8 kullanılarak görüntülenen başlık bölmesindeki başlıkları görüntüleme: Alt+bir rakam ile, 1 basış gönderenin adreslerini veya alıcılarını içeren herhangi bir başlığı duyurur, 2 basış bunları kopyalamak için bir diyalog açar, 3 basış başlıkla ilişkili yerel Thunderbird bağlam menüsünü açar;
* Boşluk tuşu, Alt+aşağı ok veya F4 aracılığıyla temizlenmiş hızlı ileti metni önizlemesi: Mesaj alıntılarındaki büyük başlık blokları, "Gönderen adı yazdı" ifadesiyle değiştirildi. NVDA, bağlantının uzun adresi yerine "tıklanabilir bağlantı"yı da duyurur.
* Alıntılara kronolojik sırayla, aşağıdan yukarıya, Shift+Boşluk, Alt+yukarı ok veya Shift+F4 üzerinden hızlı genel bakış;
* Alt+sayfa aşağı kısayolunu kullanarak veya alfasayısal tuş takımının 1 numarası aracılığıyla eklere kolay erişim;

### Hızlı Filtre Çubuğu ve Öncelikli Etiket Yönetimi 

* Filtreleme seçeneklerinde Aşağı/Yukarı oklarla gezinmek mümkündür. Enter tuşu, bir filtreyi kontrol etmek veya seçimini kaldırmak için kullanılır;
* Etiketlerin eklenmesi veya çıkarılması, alfanümerik klavyede Shift+ herhangi bir rakama basılarak yapılır. Örneğin, bir iletiye "Yapılacaklar" etiketini eklemek için Shift+4 tuşlarına basın. Ardından, erişilebilir olan hızlı filtre çubuğu aracılığıyla ileti listesini etikete göre filtreleyebilirsiniz;

### İleti Yazma Penceresi

Alt+1 Göndereni duyurur, Alt+2 Alıcıyı duyurur, Alt+3 Ekleri duyurur vb. İki kez basıldığında odak bu alanlardan birine taşınır;

### Yazım Denetimi İletişim Kutusu

* Yanlış yazılan kelime, önerilen kelimeden önce heceli veya hecesiz olarak duyurulur. NVDA+sekme veya Alt+yukarı ok kısayolları yanlış yazılan ve değiştirilen sözcükleri duyurur: 1 basış sözcükleri normal hızda heceler, 2 basış hızlı heceler, 3 basış yanlış yazılmış sözcüğü başka bir düzenleme alanında analiz için panoya kopyalar;
* Enter tuşunu içeren çeşitli kombinasyonlar, Değiştir, Tümünü Değiştir, Yoksay, Tümünü Yoksay veya Sözlüğe Kelime Ekle düğmelerini tetikleyerek bu iletişim kutusuna daha da fazla kolaylık sağlamak için eklenmiştir;

### Otomatik güncelleme

ThunderbirdPlus, devre dışı bırakma/yeniden etkinleştirme ve erteleme özelliklerine sahip bağımsız bir otomatik güncelleme sistemi içerir;

### Chichi ile Yan Yana Çalışma

ThunderbirdPlus, doğrudan Thunderbird'e yüklenen bir eklenti olan Chichi ile sorunsuz çalışacak şekilde tasarlanmıştır.

Bununla ilgili bilgileri [Chichi sayfasında][7] okuyun;


Ve [kullanım kılavuzunu][4] okuyarak keşfedeceğiniz diğer birçok şey;

<!-- Çevirmenler : aşağıdaki 4, 5 ve 7 numaralı bağlantılarda, lang=en gördüğünüz yerde en kodunu dil kodunuzla değiştirin. TR gibi.-->

[1]: https://github.com/RPTools-org/ThunderbirdPlus/releases/download/v4.9.5/thunderbirdPlus-4.9.5-TB102.nvda-addon

[2]: https://github.com/RPTools-org/ThunderbirdPlus/

[3]: https://www.rptools.org/?p=8610

[4]: https://www.rptools.org/NVDA-Thunderbird/get.php?pg=manual&lang=tr

[5]: https://www.rptools.org/NVDA-Thunderbird/get.php?pg=changes&lang=tr

[6]: https://www.rptools.org/NVDA-Thunderbird/toContact.html

[7]: https://www.rptools.org/NVDA-Thunderbird/get.php?pg=chichi&lang=en
