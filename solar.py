import streamlit as st
import math

def calcular_costo_proyecto():
    st.title("Calculadora Autónoma de Sistema Solar y Almacenamiento")
    st.subheader("Ingrese los siguientes valores:")

    consumo_promedio_mensual_kw = st.number_input("Consumo promedio mensual de energía (kWh)", min_value=0.0)

    if consumo_promedio_mensual_kw > 0:
        st.subheader("Ingrese los costos unitarios (en tu moneda local):")
        costo_panel = st.number_input("Costo por panel solar de alta eficiencia", min_value=0.0)
        costo_inversor_kw = st.number_input("Costo por kW de inversor híbrido", min_value=0.0)
        costo_bateria_kwh = st.number_input("Costo por kWh de batería de almacenamiento", min_value=0.0)
        costo_controlador = st.number_input("Costo del controlador de carga", min_value=0.0)
        costo_montaje_panel = st.number_input("Costo por estructura de montaje por panel", min_value=0.0)
        costo_cableado_protecciones = st.number_input("Costo estimado de cableado y protecciones", min_value=0.0)
        costo_medidor = st.number_input("Costo del medidor bidireccional", min_value=0.0)
        costo_mano_obra_kw = st.number_input("Costo de mano de obra por kW instalado", min_value=0.0)

        # --- Cálculos Estimados ---
        consumo_promedio_diario_kwh = consumo_promedio_mensual_kw / 30  # Aproximación
        # Asumiendo una generación promedio de 4 kWh por kWp de panel al día (puede variar significativamente)
        kwp_necesario = consumo_promedio_diario_kwh / 4
        numero_paneles = math.ceil(kwp_necesario / 0.5) # Asumiendo paneles de ~500W
        capacidad_inversor_kva = kwp_necesario * 1.25 # Margen para demanda pico
        capacidad_bateria_kwh = consumo_promedio_diario_kwh * 0.8 # Cubrir noche y días bajos

        costo_paneles_total = numero_paneles * costo_panel
        costo_inversor_total = capacidad_inversor_kva * costo_inversor_kw
        costo_baterias_total = capacidad_bateria_kwh * costo_bateria_kwh
        costo_montaje_total = numero_paneles * costo_montaje_panel
        costo_mano_obra_total = kwp_necesario * costo_mano_obra_kw

        costo_total_proyecto = (costo_paneles_total + costo_inversor_total +
                               costo_baterias_total + costo_controlador +
                               costo_montaje_total + costo_cableado_protecciones +
                               costo_medidor + costo_mano_obra_total)

        st.subheader("Estimación del Proyecto:")
        st.write(f"Consumo promedio diario estimado: {consumo_promedio_diario_kwh:.2f} kWh")
        st.write(f"Potencia pico de paneles solares necesaria (kWp): {kwp_necesario:.2f} kWp")
        st.write(f"Número estimado de paneles solares: {numero_paneles}")
        st.write(f"Capacidad estimada del inversor híbrido: {capacidad_inversor_kva:.2f} kVA")
        st.write(f"Capacidad estimada del banco de baterías: {capacidad_bateria_kwh:.2f} kWh")
        st.write(f"Costo estimado de los paneles solares: {costo_paneles_total:,.2f}")
        st.write(f"Costo estimado del inversor híbrido: {costo_inversor_total:,.2f}")
        st.write(f"Costo estimado del banco de baterías: {costo_baterias_total:,.2f}")
        st.write(f"Costo estimado del controlador de carga: {costo_controlador:,.2f}")
        st.write(f"Costo estimado del sistema de montaje: {costo_montaje_total:,.2f}")
        st.write(f"Costo estimado de cableado y protecciones: {costo_cableado_protecciones:,.2f}")
        st.write(f"Costo estimado del medidor bidireccional: {costo_medidor:,.2f}")
        st.write(f"Costo estimado de mano de obra: {costo_mano_obra_total:,.2f}")
        st.markdown(f"### Costo total estimado del proyecto: {costo_total_proyecto:,.2f}")

        # --- Estimación de Ahorro (Muy General) ---
        st.subheader("Estimación de Ahorro Mensual Potencial:")
        tarifa_promedio_kwh = st.number_input("Tarifa promedio por kWh de la energía eléctrica actual", min_value=0.0)
        ahorro_mensual_estimado = consumo_promedio_mensual_kw * tarifa_promedio_kwh
        st.write(f"Ahorro mensual estimado (sin considerar otros cargos): {ahorro_mensual_estimado:,.2f}")
        st.warning("Esta es una estimación muy general. El ahorro real dependerá de muchos factores.")

if __name__ == "__main__":
    calcular_costo_proyecto()