📊 Telekom Müşteri Kaybı (Churn) Tahmin API'sı <br>
Bu proje, bir telekomünikasyon şirketindeki müşterilerin hizmeti terk etme (churn) olasılığını tahmin etmek amacıyla geliştirilmiş, uçtan uca bir makine öğrenmesi çözümüdür. Proje, veri temizlemeden model eğitimine, profesyonel bir API servisinden modelin canlı testine kadar tüm aşamaları kapsamaktadır.<br>

<br>🚀 Proje Özellikleri<br>
<br>Gelişmiş Modelleme: XGBoost ve CatBoost gibi sektör standardı güçlü algoritmalar kullanıldı.

<br>Akıllı API: FastAPI framework'ü ile modern, hızlı ve otomatik dökümantasyona sahip (Swagger UI) bir servis oluşturuldu.

<brTürkçe Arayüz: API parametreleri ve yanıtları, projenin daha iyi anlaşılabilmesi için tamamen Türkçeleştirildi.

<brHata Analizi: Sadece başarı oranı değil, Confusion Matrix (Hata Matrisi) ve Feature Importance (Özellik Önemi) analizleri yapıldı.

<br🛠️ Kullanılan Teknolojiler<br
<brVeri Analizi: Pandas, NumPy

<brMakine Öğrenmesi: Scikit-Learn, XGBoost, CatBoost

<brAPI Geliştirme: FastAPI, Uvicorn, Pydantic

<brModel Saklama: Joblib

<br📁 Proje Yapısı<br
Plaintext
├── main.py              # FastAPI uygulama kodu
├── churn_model.pkl      # Eğitilmiş XGBoost modeli
├── scaler.pkl           # Veri ölçeklendirme dosyası
├── requirements.txt     # Gerekli kütüphaneler listesi
└── README.md            # Proje dökümantasyonu
<br⚙️ Kurulum ve Çalıştırma<br
Gerekli paketleri yükleyin:

<brBash
<brpip install -r requirements.txt
<brAPI'yi başlatın:

<brBash
<brpython main.py
<brTest Etme:
<brTarayıcınızdan http://127.0.0.1:8000/docs adresine giderek, interaktif arayüz üzerinden farklı müşteri senaryolarını test edebilirsiniz.

<br🔍 Model Analizi<br
<brModel eğitilirken sadece doğruluğa (Accuracy) değil, verinin dengesiz yapısına da dikkat edilmiştir. Yapılan analizlerde müşterilerin Sözleşme Tipi (Contract) ve <brMüşterilik Süresi (Tenure) değişkenlerinin, ayrılma kararında en belirleyici faktörler olduğu saptanmıştır.
