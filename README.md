📊 Telekom Müşteri Kaybı (Churn) Tahmin API'sı
Bu proje, bir telekomünikasyon şirketindeki müşterilerin hizmeti terk etme (churn) olasılığını tahmin etmek amacıyla geliştirilmiş, uçtan uca bir makine öğrenmesi çözümüdür. Proje, veri temizlemeden model eğitimine, profesyonel bir API servisinden modelin canlı testine kadar tüm aşamaları kapsamaktadır.

🚀 Proje Özellikleri
Gelişmiş Modelleme: XGBoost ve CatBoost gibi sektör standardı güçlü algoritmalar kullanıldı.

Akıllı API: FastAPI framework'ü ile modern, hızlı ve otomatik dökümantasyona sahip (Swagger UI) bir servis oluşturuldu.

Türkçe Arayüz: API parametreleri ve yanıtları, projenin daha iyi anlaşılabilmesi için tamamen Türkçeleştirildi.

Hata Analizi: Sadece başarı oranı değil, Confusion Matrix (Hata Matrisi) ve Feature Importance (Özellik Önemi) analizleri yapıldı.

🛠️ Kullanılan Teknolojiler
Veri Analizi: Pandas, NumPy

Makine Öğrenmesi: Scikit-Learn, XGBoost, CatBoost

API Geliştirme: FastAPI, Uvicorn, Pydantic

Model Saklama: Joblib

📁 Proje Yapısı
Plaintext
├── main.py              # FastAPI uygulama kodu
├── churn_model.pkl      # Eğitilmiş XGBoost modeli
├── scaler.pkl           # Veri ölçeklendirme dosyası
├── requirements.txt     # Gerekli kütüphaneler listesi
└── README.md            # Proje dökümantasyonu
⚙️ Kurulum ve Çalıştırma
Gerekli paketleri yükleyin:

Bash
pip install -r requirements.txt
API'yi başlatın:

Bash
python main.py
Test Etme:
Tarayıcınızdan http://127.0.0.1:8000/docs adresine giderek, interaktif arayüz üzerinden farklı müşteri senaryolarını test edebilirsiniz.

🔍 Model Analizi
Model eğitilirken sadece doğruluğa (Accuracy) değil, verinin dengesiz yapısına da dikkat edilmiştir. Yapılan analizlerde müşterilerin Sözleşme Tipi (Contract) ve Müşterilik Süresi (Tenure) değişkenlerinin, ayrılma kararında en belirleyici faktörler olduğu saptanmıştır.
