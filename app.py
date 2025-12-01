import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Calculadora de Consumo A/C", page_icon="❄️")

# Título y descripción
st.title("🔧 Calculadora de Consumo Eléctrico de Aire Acondicionado")
st.markdown("""
Esta herramienta calcula el consumo anual de energía y costo de operación de un aire acondicionado basado en:
**Fórmula:** Consumo (kWh/año) = (BTU × Horas de uso) / (SEER × 1000)
""")

# Separador
st.markdown("---")

# Crear dos columnas para mejor organización
col1, col2 = st.columns(2)

with col1:
    st.subheader("⚙️ Parámetros del Equipo")
    
    # Entrada de datos con valores predeterminados
    capacidad_btu = st.number_input(
        "Capacidad del aire acondicionado (BTU):",
        min_value=5000,
        max_value=60000,
        value=24000,
        step=1000,
        help="Capacidad de enfriamiento en BTU/h"
    )
    
    seer = st.number_input(
        "SEER del equipo:",
        min_value=5.0,
        max_value=30.0,
        value=13.0,
        step=0.5,
        help="Índice de Eficiencia Energética Estacional (mayor = más eficiente)"
    )

with col2:
    st.subheader("📅 Patrón de Uso")
    
    horas_uso = st.number_input(
        "Horas de uso al año:",
        min_value=1,
        max_value=8760,
        value=1320,
        step=100,
        help="Horas totales de operación durante un año"
    )
    
    # Opciones para calcular horas de uso
    st.markdown("**O calcular por:**")
    
    col2a, col2b = st.columns(2)
    with col2a:
        horas_diarias = st.slider("Horas por día", 1, 24, 8)
    with col2b:
        dias_anuales = st.slider("Días por año", 1, 365, 165)
    
    if st.button("Aplicar cálculo automático"):
        horas_uso = horas_diarias * dias_anuales
        st.success(f"Horas de uso configuradas: {horas_uso} horas/año")
    
    precio_kwh = st.number_input(
        "Precio de electricidad ($/kWh):",
        min_value=0.01,
        max_value=2.0,
        value=0.15,
        step=0.01,
        help="Costo por kilowatt-hora en dólares"
    )

# Separador
st.markdown("---")

# Botón para calcular
if st.button("📊 Calcular Consumo", type="primary"):
    # Cálculos
    consumo_kwh = (capacidad_btu * horas_uso) / (seer * 1000)
    consumo_usd = consumo_kwh * precio_kwh
    
    # Mostrar resultados en métricas
    st.subheader("📈 Resultados del Cálculo")
    
    # Crear columnas para métricas
    col3, col4, col5 = st.columns(3)
    
    with col3:
        st.metric(
            label="Consumo Anual",
            value=f"{consumo_kwh:,.2f}",
            delta="kWh"
        )
    
    with col4:
        st.metric(
            label="Costo Anual",
            value=f"${consumo_usd:,.2f}",
            delta="USD"
        )
    
    with col5:
        # Calcular costo mensual aproximado
        costo_mensual = consumo_usd / 12
        st.metric(
            label="Costo Mensual",
            value=f"${costo_mensual:,.2f}",
            delta="USD/mes"
        )
    
    # Separador
    st.markdown("---")
    
    # Tabla resumen con formato mejorado
    st.subheader("📋 Resumen de Parámetros y Resultados")
    
    df = pd.DataFrame({
        "Parámetro": ["Capacidad (BTU)", "Horas de uso/año", "SEER", "Precio Electricidad", "Consumo Anual", "Costo Anual"],
        "Valor": [
            f"{capacidad_btu:,.0f}",
            f"{horas_uso:,.0f}",
            f"{seer}",
            f"${precio_kwh:.2f}/kWh",
            f"{consumo_kwh:,.2f} kWh",
            f"${consumo_usd:,.2f} USD"
        ],
        "Unidad": ["BTU/h", "horas", "", "", "kWh", "USD"]
    })
    
    # Estilizar la tabla
    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Parámetro": st.column_config.TextColumn(width="medium"),
            "Valor": st.column_config.TextColumn(width="medium"),
            "Unidad": st.column_config.TextColumn(width="small")
        }
    )
    
    # Sección de información adicional
    with st.expander("💡 Información Técnica y Consejos"):
        st.markdown("""
        ### ¿Qué es SEER?
        El **SEER** (Seasonal Energy Efficiency Ratio) es una medida de la eficiencia energética 
        de un sistema de aire acondicionado. Cuanto más alto sea el SEER, más eficiente será el equipo.
        
        ### Escalas comunes de SEER:
        - **Baja eficiencia:** 8-12 SEER
        - **Media eficiencia:** 13-16 SEER  
        - **Alta eficiencia:** 17-21 SEER
        - **Muy alta eficiencia:** 22+ SEER
        
        ### Consejos para reducir el consumo:
        1. **Mantenimiento regular:** Limpia los filtros cada 1-3 meses
        2. **Temperatura óptima:** Configura el termostato a 24-26°C
        3. **Sellado de espacios:** Evita fugas de aire frío
        4. **Uso programado:** Apaga el equipo cuando no haya nadie
        5. **Sombras externas:** Reduce la carga térmica con persianas o cortinas
        
        ### Referencias de capacidad:
        - **Habitación pequeña (12-20 m²):** 9,000-12,000 BTU
        - **Sala de estar (20-30 m²):** 12,000-18,000 BTU  
        - **Apartamento pequeño (30-50 m²):** 18,000-24,000 BTU
        - **Casa mediana (50-80 m²):** 24,000-36,000 BTU
        """)
    
    # Gráfico simple de comparación (opcional)
    with st.expander("📊 Comparación con otros SEER"):
        # Calcular consumo con diferentes valores de SEER
        seer_values = [10, 13, 16, 20, 25]
        consumos = [(capacidad_btu * horas_uso) / (seer_val * 1000) for seer_val in seer_values]
        costos = [consumo * precio_kwh for consumo in consumos]
        
        comp_df = pd.DataFrame({
            "SEER": seer_values,
            "Consumo (kWh)": consumos,
            "Costo Anual (USD)": costos
        })
        
        st.dataframe(comp_df.style.format({
            "Consumo (kWh)": "{:,.1f}",
            "Costo Anual (USD)": "${:,.2f}"
        }))

# Pie de página
st.markdown("---")
st.caption("""
⚠️ **Nota:** Este cálculo es una estimación. El consumo real puede variar según factores como:
instalación, mantenimiento, condiciones climáticas y hábitos de uso.
""")
