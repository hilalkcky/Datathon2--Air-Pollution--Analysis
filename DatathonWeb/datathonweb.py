import streamlit as st
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

rfc=joblib.load("deneme.pkl",mmap_mode=None)
def main():

    st.title("Hava Kirlilik İndeksini Hesaplama")
    pm10=st.number_input("pm10_(Âµg/m3) değerini giriniz:")
    so2=st.number_input("so2_(Âµg/m3) değerini giriniz:")
    co=st.number_input("co_(Âµg/m3) değerini giriniz:")
    no2=st.number_input("no2_(Âµg/m3) değerini giriniz:")
    nox=st.number_input("nox_(Âµg/m3) değerini giriniz:")
    o3=st.number_input("o3_(Âµg/m3) değerini giriniz:")



    def hesaplama(pm10,so2,co,no2,nox,o3):
        toplam=(pm10+so2+co+no2+nox+o3)/10
        return toplam


    predict=rfc.predict([[pm10,so2,co,no2,nox,o3]])[0]
    if predict==0:
        predict="İyi"
    if predict==1.0:
        predict="Orta"
    if predict==2.0:
        predict="Hassas"
    if predict==3.0:
        predict="Sağlıksız"
    if predict==4.0:
        predict="Kötü"
    if predict == 5.0:
        predict = "Tehlikeli"

    if st.button("Hesapla",type="primary"):
        st.title(predict)

if __name__=="__main__":
    main()