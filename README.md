# Rasa Chatbot Integrasi dengan Web

## Langkah Instalasi

1. Buat Virtual Environment

   - Conda Environment

     - Membuat Environment
       `conda create -n rasa python=3.6`
     - Mengaktifkan Environment
       `conda activate rasa`

   - Python Virtual Envirinment
     - Membuat Environment
       `python -m venv .venv`
     - Mengaktifkan Environment
       `source .venv/Scripts/activate`

2. Instalasi Package

   - Update PIP
     `python -m pip install --upgrade pip`

   - Install Rasa
     `pip install rasa`

3. Jalankan Chatbot

   - Jalankan Action
     `rasa run actions`

   - Jalankan Rasa Chatbot
     `rasa run -m models --enable-api --cors "\*" --debug`

4. Buka Web
   - Buka file Index di Browser
     `<direktori_file>/rasa-chatbot/index.html`
