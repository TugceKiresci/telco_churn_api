📊 Telekom Müşteri Kaybı (Churn) Tahmin API'sı <br><br>
Bu proje, bir telekomünikasyon şirketindeki müşterilerin hizmeti terk etme (churn) olasılığını tahmin etmek amacıyla geliştirilmiş, uçtan uca bir makine öğrenmesi çözümüdür. Proje, veri temizlemeden model eğitimine, profesyonel bir API servisinden modelin canlı testine kadar tüm aşamaları kapsamaktadır.<br>

<br>🚀 Proje Özellikleri<br>
<br>Gelişmiş Modelleme: XGBoost ve CatBoost gibi sektör standardı güçlü algoritmalar kullanıldı.

Akıllı API: FastAPI framework'ü ile modern, hızlı ve otomatik dökümantasyona sahip (Swagger UI) bir servis oluşturuldu.

Türkçe Arayüz: API parametreleri ve yanıtları, projenin daha iyi anlaşılabilmesi için tamamen Türkçeleştirildi.

Hata Analizi: Sadece başarı oranı değil, Confusion Matrix (Hata Matrisi) ve Feature Importance (Özellik Önemi) analizleri yapıldı.

<br>🛠️ Kullanılan Teknolojiler<br>
<br>Veri Analizi: Pandas, NumPy

Makine Öğrenmesi: Scikit-Learn, XGBoost, CatBoost

API Geliştirme: FastAPI, Uvicorn, Pydantic

Model Saklama: Joblib

<br>📁 Proje Yapısı<br>
Plaintext<br>
├── main.py                  ( FastAPI uygulama kodu)<br>
├── churn_model.pkl          ( Eğitilmiş XGBoost modeli)<br>
├── scaler.pkl               ( Veri ölçeklendirme dosyası)<br>
├── requirements.txt         ( Gerekli kütüphaneler listesi)<br>
└── README.md                 ( Proje dökümantasyonu)<br>
<br>⚙️ Kurulum ve Çalıştırma<br>
Gerekli paketleri yükleyin:

<br>Bash
<br>pip install -r requirements.txt
API'yi başlatın:

<br>Bash
<br>python main.py<br>
<br>Test Etme:
<br>Tarayıcınızdan http://127.0.0.1:8000/docs adresine giderek, interaktif arayüz üzerinden farklı müşteri senaryolarını test edebilirsiniz.

<br>🔍 Model Analizi<br>
Model eğitilirken sadece doğruluğa (Accuracy) değil, verinin dengesiz yapısına da dikkat edilmiştir. Yapılan analizlerde müşterilerin Sözleşme Tipi (Contract) ve Müşterilik Süresi (Tenure) değişkenlerinin, ayrılma kararında en belirleyici faktörler olduğu saptanmıştır.
