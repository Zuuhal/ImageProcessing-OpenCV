# Real-Time Vehicle Detection with YOLOv5 & OpenCV

Bu proje, OpenCV ve YOLOv5 kullanarak gerçek zamanlı araç tespiti yapmaktadır. Kamera üzerinden görüntü alınır, tespit edilen araçlar üzerinde sınıf ve güven skorları gösterilir ve video kaydı yapılabilir.

## Dosyalar
- `main.py` : Canlı kamera görüntüsü ile nesne tespiti ve video kaydı.
- `train_ex.py` : Önceden eğitilmiş YOLOv5 modeli ile model training.
- `train/` : Model eğitimi ve dataset kullanımı için örnek kodlar.

## Kullanılan Teknolojiler
- Python 3.8
- OpenCV
- PyTorch
- YOLOv5 (v4, v5, v8 denendi)
- Roboflow (dataset yönetimi)
- NumPy, Matplotlib

## Kurulum
Python 3.8+ gereklidir. Gerekli kütüphaneler:

```bash
pip install torch torchvision torchaudio
pip install opencv-python
pip install matplotlib
pip install numpy
pip install roboflow
