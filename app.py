
import streamlit as st

st.set_page_config(
    page_title="Calculadora VT",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Calculadora VT")
st.write("Calculadora com operações matemáticas.")

st.divider()

operacao = st.selectbox(
    "Escolha a operação:",
    [
        "Adição (+)",
        "Subtração (-)",
        "Multiplicação (×)",
        "Divisão (÷)",
        "Raiz Quadrada (√)",
        "Raiz Cúbica (∛)",
        "Potenciação (^)"
    ]
)

resultado = None

if operacao == "Adição (+)":
    n1 = st.number_input("Primeiro número", value=0.0)
    n2 = st.number_input("Segundo número", value=0.0)

    if st.button("Calcular"):
        resultado = n1 + n2

elif operacao == "Subtração (-)":
    n1 = st.number_input("Primeiro número", value=0.0)
    n2 = st.number_input("Segundo número", value=0.0)

    if st.button("Calcular"):
        resultado = n1 - n2

elif operacao == "Multiplicação (×)":
    n1 = st.number_input("Primeiro número", value=0.0)
    n2 = st.number_input("Segundo número", value=0.0)

    if st.button("Calcular"):
        resultado = n1 * n2

elif operacao == "Divisão (÷)":
    n1 = st.number_input("Primeiro número", value=0.0)
    n2 = st.number_input("Segundo número", value=0.0)

    if st.button("Calcular"):
        if n2 == 0:
            st.error("Não é possível dividir por zero!")
        else:
            resultado = n1 / n2

elif operacao == "Raiz Quadrada (√)":
    n1 = st.number_input("Digite um número", value=0.0)

    if st.button("Calcular"):
        if n1 < 0:
            st.error("Não existe raiz quadrada real de número negativo.")
        else:
            resultado = n1 ** 0.5

elif operacao == "Raiz Cúbica (∛)":
    n1 = st.number_input("Digite um número", value=0.0)

    if st.button("Calcular"):
        if n1 < 0:
            resultado = -((-n1) ** (1/3))
        else:
            resultado = n1 ** (1/3)

elif operacao == "Potenciação (^)":
    n1 = st.number_input("Digite a base", value=0.0)
    n2 = st.number_input("Digite o expoente", value=2.0)

    if st.button("Calcular"):
        try:
            if n1 == 0 and n2 < 0:
                st.error("Zero não pode ter expoente negativo.")
            else:
                resultado = n1 ** n2

        except (ValueError, OverflowError):
            st.error("Não foi possível calcular essa potência.")

if resultado is not None:
    st.success(f"Resultado: {resultado:.10g}")

st.divider()

st.caption("Calculadora VT | Desenvolvida em Python com Streamlit")
