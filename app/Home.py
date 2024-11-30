import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Book Looker - Recomendações e Análises de Preços de Livros",
    layout="wide",
    page_icon="🌟"
)



st.title("📚 Book Looker")
st.subheader("Encontre os melhores preços e receba recomendações personalizadas de livros!")

# Introdução
st.markdown(
    """
    Bem-vindo ao **Book Looker**! 
    Aqui você pode:
    - 📊 Ver análises detalhadas sobre preços.
    - 🌟 Obter recomendações baseadas nos seus interesses.
    """
)

# Seções principais
st.header("📖 Comparar Preços")
st.text("Veja preços atualizados de livros em lojas populares.")

st.header("🌟 Recomendações")
st.text("Descubra livros baseados nas suas preferências.")
with st.expander("Como funciona?"):
    st.markdown(
        """
        - Converse com a nossa bilibotecaria!.
        - Receba recomendações baseadas em tópicos e assuntos de suas preferencias
        """
    )

st.header("📊 Análises de Preços")
st.text("Visualize tendências de preços e avaliações de livros.")
with st.expander("Gráficos e insights"):
    st.markdown(
        """
        - Explore gráficos de preços históricos.
        """
    )
# Rodapé
st.markdown("---")
st.markdown(
    """
    © 2024 **Book Looker**. Todos os direitos reservados.
    """
)
