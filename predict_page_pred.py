import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_pred_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_name = data["le_name"]
le_transmission = data["le_transmission"]
le_city = data["le_city"]

def show_predict_page():
    st.title("Used Car Price Prediction in Indonesia App")

    st.write("""### Information to predict used car""")

    name = (
        'Toyota Yaris', 'Toyota Fortuner', 'Honda Brio',
       'Honda HR-V', 'Suzuki Ertiga', 'Honda Mobilio', 'Honda Civic',
       'Datsun GO', 'Daihatsu Ayla', 'Toyota Avanza', 'BMW X1',
       'Toyota Kijang Innova', 'Mitsubishi Pajero Sport', 'BMW 330i',
       'Toyota Etios Valco', 'Suzuki Swift', 'Hyundai Accent',
       'Daihatsu Sirion', 'Honda Accord', 'Honda Stream',
       'Nissan X-Trail', 'Mercedes-Benz GLE400', 'Suzuki APV',
       'Volkswagen Golf',
       'Honda Jazz', 'Toyota Camry', 'Mazda 2', 'Toyota Alphard',
       'BMW 523i', 'BMW X5', 'Ford Escape', 'Hyundai H-1',
       'Nissan Elgrand', 'Suzuki Neo Baleno', 'Daihatsu Gran Max',
       'Mazda CX-7', 'Mercedes-Benz C230', 'Toyota Corolla Altis',
       'Mitsubishi Xpander', 'Hyundai Santa Fe', 'Mercedes-Benz E250',
       'Chevrolet Aveo', 'Mercedes-Benz B200', 'Toyota Calya',
       'Toyota Hilux', 'Nissan Serena', 'Toyota Sienta',
       'Nissan Grand Livina', 'Toyota Vellfire', 'BMW 320i',
       'Toyota Vios', 'Mazda CX-9', 'Honda Freed',
       'Mitsubishi Outlander Sport', 'Toyota Rush', 'Daihatsu Sigra',
       'Suzuki Baleno', 'Nissan Livina', 'Honda BR-V', 'Honda City',
       'Toyota Innova Venturer', 'BMW 335i', 'Toyota Agya', 'Honda CR-V',
       'Mazda Biante', 'Mazda CX-3', 'BMW X3', 'Daihatsu Terios',
       'Suzuki XL7', 'Nissan March', 'Mercedes-Benz AMG GT', 'Suzuki SX4',
       'Mercedes-Benz E300', 'Dodge Journey', 'Proton Neo',
       'Volkswagen Tiguan', 'KIA Picanto', 'Daihatsu Xenia',
       'Suzuki SX4 S-Cross', 'BMW 530i', 'Honda Odyssey',
       'Mercedes-Benz C250', 'Suzuki Ignis', 'Lexus LX570',
       'Toyota Corolla', 'Toyota Camry Hybrid', 'Chevrolet Trax',
       'Lexus RX270', 'Mercedes-Benz E260', 'Mazda CX-5',
       'Toyota Harrier', 'BMW 520i', 'Mercedes-Benz C200',
       'Mercedes-Benz CLA200', 'Rolls-Royce Phantom',
       'Lamborghini Aventador', 'Land Rover Range Rover Evoque',
       'Suzuki Jimny', 'Chevrolet Captiva', 'BMW 328i', 'BMW 520d',
       'Nissan Evalia', 'Maserati Ghibli', 'Jeep Grand Cherokee',
       'Suzuki Karimun Wagon R', 'Datsun GO+', 'Daihatsu Luxio',
       'Porsche Boxster', 'Toyota NAV1', 'Ford Fiesta',
       'Chevrolet Trailblazer', 'Toyota Kijang', 'Suzuki Katana',
       'Toyota Hiace', 'Suzuki Splash', 'Mitsubishi Triton',
       'Mercedes-Benz E280', 'Mitsubishi Mirage', 'Mercedes-Benz ML400',
       'Mercedes-Benz C180', 'Honda CR-Z', 'Wuling Almaz',
       'Wuling Cortez', 'Volkswagen Polo', 'Mazda 3',
       'Toyota Land Cruiser Prado', 'Mercedes-Benz ML350',
       'Mercedes-Benz S300 L', 'Toyota 86', 'Mazda 6', 'Isuzu Panther',
       'Mitsubishi Pajero', 'Isuzu Elf', 'Nissan Teana', 'Audi A6',
       'Chevrolet Orlando', 'Mercedes-Benz R300 L', 'Hino Ranger',
       'BMW 116i', 'BMW 318i', 'Mercedes-Benz CLS63 AMG',
       'Renault Duster', 'Chevrolet Spin', 'Ford EcoSport', 'KIA Rio',
       'Ford Mustang', 'Lexus RX350', 'Mercedes-Benz 300E',
       'Mitsubishi Kuda', 'KIA Sorento', 'Ford Everest',
       'Mercedes-Benz E200', 'Jeep CJ 7', 'Suzuki Carry',
       'Suzuki Grand Vitara', 'BMW 428i', 'Jeep Compass', 'Mazda 5',
       'Hyundai i20', 'Lexus RX300', 'Hyundai Avega',
       'Mercedes-Benz S450 L', 'Volkswagen Caravelle', 'Mazda RX-8',
       'Nissan Livina X-Gear', 'Mercedes-Benz SLK200', 'KIA Grand Sedona',
       'Nissan Terra', 'Hyundai Kona', 'Mercedes-Benz E230',
       'Isuzu D-Max', 'Suzuki Karimun', 'Isuzu MU-X',
       'Volkswagen Touareg', 'smart fortwo', 'Peugeot RCZ',
       'Toyota Soluna', 'Mitsubishi Grandis', 'Hyundai Grand Avega',
       'DFSK Super Cab', 'Suzuki Escudo', 'Suzuki Aerio',
       'Hyundai Grand i10', 'Toyota Starlet', 'DFSK Glory 560',
       'Ford Focus', 'Mercedes-Benz S320', 'Toyota Limo', 'Ford Ranger',
       'Audi Q5', 'Hyundai Sonata', 'DFSK Glory 580', 'Chevrolet Spark',
       'BMW X6', 'Mercedes-Benz A250', 'Mercedes-Benz SLC200',
       'Renault Koleos', 'Audi TT', 'Audi A3', 'Toyota Hardtop',
       'Isuzu Traga', 'Mitsubishi Galant', 'Land Rover Discovery',
       'KIA Sportage', 'Volkswagen Touran', 'Volkswagen Kombi',
       'Volkswagen Beetle', 'Hyundai Atoz', 'KIA Visto', 'Daihatsu Zebra',
       'Daihatsu Taruna', 'Datsun Cross', 'BMW 325i', 'Hyundai Trajet',
       'Opel Blazer', 'Proton Exora', 'Mazda E2000', 'Peugeot 3008',
       'Mercedes-Benz 200', 'Daihatsu Hi-Max', 'Mercedes-Benz 230E',
       'Toyota Wish', 'Volvo S80', 'KIA Carens', 'Peugeot 5008',
       'Chevrolet Zafira', 'Peugeot 206', 'Toyota RAV4', 'KIA Pregio',
       'Toyota Corona', 'Mazda MX-5', 'Suzuki Grand Escudo', 'KIA Seltos',
       'KIA Big Up', 'Renault Triber', 'Peugeot 806', 'Nissan Almera',
       'Land Rover Discovery 4', 'Aston Martin DB11'
    )

    transmission = (
        'Manual', 'Automatic'
    )
        
    

    city = (
        'DKI Jakarta','Jawa Barat','Banten','Kalimantan Barat', 'Jawa Timur', 
       'Yogyakarta', 'Jawa Tengah', 'Bali',
       'Nusa Tenggara Barat', 'Sumatera Utara',
       'Riau', 'Papua', 'Sulawesi Selatan', 'Kalimantan Timur',
       'Bengkulu', 'Lampung', 'Sulawesi Utara', 'Sumatera Selatan',
       'Sumatera Barat', 'Jambi', 'Kalimantan Tengah',
       'Kalimantan Selatan', 'Nangroe Aceh Darussalam', 'Kepulauan Riau',
       'Sulawesi Tengah', 'Bangka Belitung', 'Sulawesi Barat',
       'Irian Jaya Barat', 'Gorontalo', 'Sulawesi Tenggara',
       'Nusa Tenggara Timur', 'Maluku','Indonesia (Lainnya)',
    )

    car = st.selectbox("Car Type", name)
    transmisi = st.selectbox("Transmission", transmission)
    propinsi = st.selectbox("Province", city)

    year = st.slider("Fabrication Year", 1967, 2021, 2021)
    mileage = st.slider("Mileage", 500, 100000, 10000)

    ok = st.button("Calculate Price")

    if ok:
        X = np.array([[year, car, mileage, transmisi, propinsi]])
        X[:, 1] = le_name.transform(X[:, 1])
        X[:, 3] = le_transmission.transform(X[:, 3])
        X[:, 4] = le_city.transform(X[:, 4])
        X = X.astype(int)

        price = regressor.predict(X)
        st.subheader(f"The Estimated Price is IDR {price[0]:,.0f}")
