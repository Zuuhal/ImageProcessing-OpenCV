# 🚗 Real-Time Vehicle Detection with YOLOv5 & OpenCV

Bu proje, **YOLOv5** derin öğrenme modelini ve **OpenCV** kütüphanesini kullanarak **gerçek zamanlı (webcam)** video akışları üzerinde araç tespiti yapmaktadır. Kamera üzerinden alınan görüntü anlık olarak işlenir, tespit edilen araçlar çerçevelenir ve tespit güven skorları gösterilir. Ayrıca, işlenen video akışı yerel olarak kaydedilir.

## 📁 Dosyalar

| Dosya Adı | Açıklama |
| :--- | :--- |
| **`main.py`** | Canlı kamera görüntüsü (webcam) üzerinde **YOLOv5** ile önceden eğitilmiş bir model kullanarak nesne tespiti yapar ve sonucu bir video dosyasına kaydeder. |
| **`train.ipynb`** | **YOLOv5** modelinin özel bir araç veri kümesi (Roboflow) üzerinde nasıl eğitildiğini gösteren adımları ve kodları içeren Colab/Jupyter defteri (içeriği eğitim çıktısını temsil ediyor). |

## 🛠️ Kullanılan Teknolojiler

  * **Python 3.8**
  * **OpenCV:** Video akışını yönetmek, görüntüleri işlemek ve sonuçları görselleştirmek için.
  * **PyTorch:** Derin öğrenme modeli altyapısı.
  * **YOLOv5:** Gerçek zamanlı nesne tespiti modeli.
  * **Roboflow:** Özel veri kümesi yönetimi ve indirilmesi.
  * **NumPy, Matplotlib**

-----

## 💻 Kurulum

Projeyi yerel olarak çalıştırmak ve bağımlılıkları yüklemek için aşağıdaki adımları izleyin.

### 1\. Python ve Kütüphaneler

Python 3.8+ gereklidir. Gerekli kütüphaneleri yüklemek için:

```bash
# PyTorch ve gerekli diğer bilimsel kütüphaneler
pip install torch numpy
# Görüntü işleme ve video kütüphanesi
pip install opencv-python
# YOLOv5'i PyTorch Hub'dan yüklemek için gerekli olabilir
pip install -U PyYAML requests
```

### 2\. Model Ağırlıklarını Hazırlama

`main.py` dosyasını çalıştırmadan önce, eğitilmiş **YOLOv5 model ağırlık dosyanızın** yerel yolunu belirtmeniz gerekir.

`main.py` dosyanızdaki `weights_path` değişkenini kendi dosya yolunuzla **güncelleyin**:

-----

## ▶️ Nasıl Çalıştırılır?

`main.py` dosyasını çalıştırarak gerçek zamanlı araç tespitini başlatabilirsiniz:

```bash
python main.py
```

### Özellikler

  * **Canlı Görüntüleme:** Web kameranızdan alınan akış anlık olarak bir pencerede gösterilir.
  * **Tespit ve Skor:** Tespit edilen her aracın etrafına bir kutu çizilir ve güven skoru (`score`) yazılır.
  * **Performans Takibi:** Görüntünün sol üst köşesinde anlık **FPS** (Kare/Saniye) değeri gösterilir.
  * **Video Kaydı:** Akış, tanımlanan video codec'i ve ayarları ile belirtilen yola (`kayit1.mp4`) otomatik olarak kaydedilir.
  * **Durdurma:** Görüntü penceresi aktifken **ESC** tuşuna basarak programı güvenli bir şekilde kapatabilirsiniz.

-----

## 🎓 Eğitim Kodları (`train.ipynb` / `train_ex` İçeriği)

`train.ipynb` dosyası (veya `train_ex` içeriği), özel araç veri kümesi kullanılarak **YOLOv5s** modelinin eğitim sürecini detaylandırır.

Eğitim adımları şunları içerir:

1.  **YOLOv5** deposunun klonlanması.
2.  **Roboflow** API ile veri kümesinin indirilmesi.
3.  Modelin **300 epoch** boyunca eğitilmesi (GPU üzerinde).
4.  Eğitim sonuçlarının incelenmesi ve en iyi model ağırlıklarının (`best.pt`) elde edilmesi.

Eğitim sonucunda elde edilen yüksek **mAP50** (0.995) ve **mAP50-95** (0.893) skorları, modelin veri kümesi üzerinde yüksek performans gösterdiğini teyit eder.

-----
## ⚠️ Önemli Notlar

Kullanacağınız işletim sistemine göre doysa yolu veya video codec'i gibi bazı bileşenlerde değişiklik yapmanız gerekebilir.
