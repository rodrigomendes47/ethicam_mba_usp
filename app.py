import streamlit as st
import requests

# API_ENDPOINT = "http://127.0.0.1:8000"
API_ENDPOINT = "https://known-phoenix-specially.ngrok-free.app"

st.set_page_config(
    page_title="Video Uploader",
    page_icon="📹",
    layout="centered"
)

st.title("📹 Ethicam")
st.markdown(
    """
    Tecnologia e Ética: Desenvolvimento de um Serviço para Anonimização de Imagens em Conformidade com a LGPD
    """
)
try:
    health = requests.get(API_ENDPOINT)
    if health.status_code == 200:
        st.success("Serviço backend online!")
    else:
        st.error("Serviço backend offline")
except:
    st.error("Serviço backend offline")

# Widget para upload do arquivo
uploaded_file = st.file_uploader(
    "Escolha um arquivo de vídeo",
    type=["mp4", "mov", "avi", "mkv"],
    help="Formatos suportados: MP4, MOV, AVI, MKV"
)

# Criar duas colunas para exibir o vídeo original e o processado

if uploaded_file is not None:
    # --- Coluna 1: Vídeo Original ---
    # st.header("Vídeo Original")
    # # Exibir o vídeo original que o usuário carregou
    # st.video(uploaded_file)

    # Botão para iniciar o processamento
    if st.button("Upload", use_container_width=True, type="primary"):
        with st.spinner("Aguarde... Enviando e processando o vídeo. Isso pode levar alguns minutos."):
            try:
                # Preparar o arquivo para a requisição POST
                files = {
                    'video_file': (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
                }

                # Fazer a requisição POST para a API.
                # Aumentamos o timeout, pois o processamento de vídeo pode ser demorado.
                response = requests.post(API_ENDPOINT+"/upload_video/", files=files) # Timeout de 3 minutos
                print(type(response.content))
                # Verificar a resposta do servidor
                if response.status_code == 200:
                    st.success("✅ Vídeo processado com sucesso!")
                    # Armazenar os bytes do vídeo recebido no estado da sessão
                    st.session_state.processed_video = response.content
                else:
                    st.error(f"❌ Falha no processamento. O servidor retornou o código: {response.status_code}")
                    # Limpar vídeo anterior se houver erro
                    if 'processed_video' in st.session_state:
                        del st.session_state.processed_video
                    try:
                        st.json(response.json()) # Tenta mostrar o erro em JSON, se houver
                    except requests.exceptions.JSONDecodeError:
                        st.text(response.text)

            except requests.exceptions.RequestException as e:
                st.error(f"🔌 Ocorreu um erro ao tentar conectar-se à API.")
                st.error(f"Detalhes do erro: {e}")
                st.info(f"Verifique se sua API está rodando em `{API_ENDPOINT}`.")
                del st.session_state.processed_video
            
            if st.session_state.get('processed_video'):
                st.download_button("Downlaod video",st.session_state.processed_video, "output.mp4")


else:
    st.info("Por favor, carregue um arquivo de vídeo para começar.")

