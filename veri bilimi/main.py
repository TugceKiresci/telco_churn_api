from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np
from pydantic import BaseModel, Field
import xgboost as xgb

# 1. API Tanımlamalarını Türkçe Yapalım
app = FastAPI(
    title="Telekom Müşteri Kaybı Tahmin API",
    description="Müşteri bilgilerini kullanarak ayrılma riskini tahmin eden yapay zeka servisi.",
    version="1.0.0"
)

# Modelleri yükle
model = joblib.load('churn_model.pkl')
scaler = joblib.load('scaler.pkl')

# 2. Girdi Alanlarını Türkçe Açıklamalarla Tanımlayalım (Field kullanarak)
class MusteriVerisi(BaseModel):
    gender: int = Field(..., description="Cinsiyet (0: Kadın, 1: Erkek)")
    SeniorCitizen: int = Field(..., description="Yaşlı Vatandaş (0: Hayır, 1: Evet)")
    Partner: int = Field(..., description="Eşi/Partneri Var mı? (0: Hayır, 1: Evet)")
    Dependents: int = Field(..., description="Bakmakla Yükümlü Olduğu Kişi Var mı? (0: Hayır, 1: Evet)")
    tenure: int = Field(..., description="Müşterilik Süresi (Ay)")
    PhoneService: int = Field(..., description="Telefon Servisi (0: Yok, 1: Var)")
    MultipleLines: int = Field(..., description="Birden Fazla Hat (0: Yok, 1: Var)")
    InternetService: int = Field(..., description="İnternet Servis Tipi (0: DSL, 1: Fiber Optik, 2: Yok)")
    OnlineSecurity: int = Field(..., description="Çevrimiçi Güvenlik (0: Yok, 1: Var)")
    OnlineBackup: int = Field(..., description="Çevrimiçi Yedekleme (0: Yok, 1: Var)")
    DeviceProtection: int = Field(..., description="Cihaz Koruması (0: Yok, 1: Var)")
    TechSupport: int = Field(..., description="Teknik Destek (0: Yok, 1: Var)")
    StreamingTV: int = Field(..., description="TV Yayını (0: Yok, 1: Var)")
    StreamingMovies: int = Field(..., description="Film Yayını (0: Yok, 1: Var)")
    Contract: int = Field(..., description="Sözleşme Tipi (0: Aylık, 1: Bir Yıllık, 2: İki Yıllık)")
    PaperlessBilling: int = Field(..., description="Kağıtsız Fatura (0: Hayır, 1: Evet)")
    PaymentMethod: int = Field(..., description="Ödeme Yöntemi (0: Elektronik Çek, 1: Posta Çeki, 2: Banka Transferi, 3: Kredi Kartı)")
    MonthlyCharges: float = Field(..., description="Aylık Ödeme Tutarı")
    TotalCharges: float = Field(..., description="Toplam Ödeme Tutarı")

@app.get("/", tags=["Genel"])
def ana_sayfa():
    return {"mesaj": "Müşteri Kaybı Tahmin API'sine Hoş Geldiniz. Test için /docs adresine gidin."}

# 3. Tahmin Endpoint'ini ve Yanıtları Türkçe Yapalım
@app.post("/tahmin-et", tags=["Tahminleme"])
def tahmin_et(musteri: MusteriVerisi):
    # Veriyi DataFrame'e çevir
    data = musteri.dict()
    df_input = pd.DataFrame([data])
    
    # Ölçeklendirme (Scaling)
    scaled_data = scaler.transform(df_input)
    
    # Tahmin ve Olasılık
    tahmin = model.predict(scaled_data)[0]
    olasilik = model.predict_proba(scaled_data)[0][1]
    # Tahmini yaptıktan sonra şu satırı ekle/güncelle:
    olasilik_yuzde = f"%{round(float(olasilik) * 100, 2)}"

    return {
        "churn_prediction": "Yes" if tahmin == 1 else "No",
        "churn_probability": olasilik_yuzde, # Artık 0.2994 değil, %29.94 görünecek
        "status": "Müşteri yüksek riskli!" if olasilik > 0.5 else "Müşteri bağlılığı yüksek."
    }   
  

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)