import requests
import streamlit as st

st.title("Кредитная карта Premium")
st.write("Новая кредитная карта с мгновенным одобрением")

API_URL = "http://127.0.0.1:8000/score" 

with st.form("Подать заявку"):
    age = st.number_input("Ваш возраст", min_value=18)
    income = st.number_input("Ваш доход в тысячах рублей", min_value=0)
    education = st.checkbox("У меня есть высшее образование")
    work = st.checkbox("У меня есть стабильная работа")
    car = st.checkbox("У меня есть автомобиль")
    submit = st.form_submit_button("Подать заявку")

if submit:
    data = {
        "age": age, 
        "income": income, 
        "education": education, 
        "work": work, 
        "car": car
    }
    
    try:
        # Отправляем запрос на API скоринга
        response = requests.post(API_URL, json=data)
        
        # Проверяем статус ответа
        if response.status_code == 200:
            result = response.json()
            if result.get("approved"):
                st.success("Поздравляем, ваша заявка одобрена!")
            else:
                st.info("Подобрали для вас альтернативу — дебетовая карта с 3% кэшбеком.")
        else:
            st.error(f"Ошибка сервера: {response.status_code}. Текст: {response.text}")
            
    except requests.exceptions.ConnectionError:
        st.error("Не удалось подключиться к сервису скоринга. Убедитесь, что он запущен на порту 8000.")
    except Exception as e:
        st.error(f"Произошла ошибка: {e}")