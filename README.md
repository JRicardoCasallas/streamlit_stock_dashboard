# 📊 Streamlit Stock Dashboard

Un **dashboard interactivo en Streamlit** para visualizar la evolución de precios de acciones en tiempo real usando `yfinance` y `plotly`.

---

## 🚀 Características
- Selección de varios **tickers populares**:  
  - IBM  
  - AAPL (Apple)  
  - MSFT (Microsoft)  
  - AMZN (Amazon)  
  - META (Meta / Facebook)  
  - SPY (S&P 500 ETF)  
- Visualización del precio de cierre con gráficos dinámicos.  
- Métricas clave: **precio actual, máximo y mínimo del día**.  
- Interfaz simple y rápida usando **Streamlit**.  

---

## 🛠️ Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/JRicardoCasallas/streamlit_stock_dashboard.git
   cd streamlit_stock_dashboard
   
   ```

2. Crea un entorno virtual e instala dependencias:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # En Windows
   # source venv/bin/activate  # En Linux/Mac

   pip install -r requirements.txt
   ```

---

## ▶️ Uso

Ejecuta el siguiente comando en tu terminal:

```bash
streamlit run app.py
```

Luego abre en tu navegador:

- Local: [http://localhost:8501](http://localhost:8501)  
- Red local: http://TU_IP:8501  

---

## 📂 Estructura del proyecto
```
streamlit_stock_dashboard/
│── app.py              # Código principal del dashboard
│── requirements.txt    # Dependencias del proyecto
│── .gitignore          # Archivos/carpetas ignoradas
│── README.md           # Documentación
│── venv/               # Entorno virtual (NO se sube a GitHub)
```

---

Tecnologías utilizadas

Python: https://www.python.org/

Streamlit: https://streamlit.io/

Plotly: https://plotly.com/python/

yfinance: https://pypi.org/project/yfinance/

pandas: https://pandas.pydata.org/

## 📜 Licencia
💡 Autor: Jose Ricardo Casallas
📅 Proyecto creado en 2025
