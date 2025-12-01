# AcEnergyConsumptionCalculator_1
Calculadora de consumo de energia para aires acondicionados. Uso exclusivo de FRIORECORD S.A. Autor principal Jhon Treyes. Co-Autor Margarita Treyes.

# Calculadora de Consumo Eléctrico de Aire Acondicionado

Aplicación web para calcular el consumo anual de energía y costo de operación de sistemas de aire acondicionado.

## Características
- Cálculo basado en capacidad BTU, SEER y horas de uso
- Estimación de costos en USD
- Comparación de eficiencia energética
- Interfaz intuitiva con Streamlit

## Fórmula
- Consumo (kWh/año) = (BTU × Horas de uso) / (SEER × 1000)

## Instalación local
```bash
pip install -r requirements.txt
streamlit run app.py
