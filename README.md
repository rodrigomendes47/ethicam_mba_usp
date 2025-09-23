# Ethicam
[ENGLISH BELOW]
Ethicam é um projeto de anonimização de vídeos, inicialmente batizado como a junção das palavras **Ethic** e **Camera**. O projeto oferece um serviço de backend que processa vídeos e borra o rosto de pessoas, garantindo a privacidade.
<img width="945" height="647" alt="image" src="https://github.com/user-attachments/assets/e132d3b7-e637-4933-8e19-aa02c8a2865c" />

## Frontend

O frontend da aplicação serve como uma interface para que os usuários possam testar o serviço de anonimização. Foi desenvolvido em Python, utilizando a biblioteca **Streamlit**, o que facilitou a criação de uma interface web simples e interativa.

Os usuários podem fazer o upload de vídeos nos formatos MP4, MOV, AVI e MKV. O frontend então envia o vídeo para o serviço de backend através de uma API REST, construída com a biblioteca **FastAPI**. Após o processamento, o vídeo anonimizado pode ser baixado.

A solução frontend está hospedada na plataforma **Render**, em uma instância com 512 MB de RAM e 0,1 CPU. A aplicação está disponível publicamente em **https://anonimization-front.onrender.com**.
<img width="760" height="426" alt="image" src="https://github.com/user-attachments/assets/ca9507d5-c558-4d16-b2e6-aebff5e5207d" />

## Backend

O backend do projeto foi implementado em uma instância do **Google Colab**, utilizando uma GPU NVIDIA Tesla T4 com 16 GB de VRAM para processar vídeos de forma eficiente.

O processo de anonimização ocorre da seguinte forma:
1. O vídeo recebido é processado **frame a frame** com a biblioteca **OpenCV**.
2. É aplicado um **filtro de blur gaussiano** (`GaussianBlur()`) nas regiões onde pessoas são detectadas, borrando-as de forma eficaz.
3. Este tipo de filtro cria um desfoque mais natural e suave, preservando as bordas e contornos da imagem.

O backend é um servidor **API REST**, desenvolvido com **FastAPI**, que recebe vídeos de entrada e retorna o vídeo processado. Para acesso público durante o desenvolvimento, a ferramenta **Ngrok** foi usada para expor o servidor do Colab à internet.

---

## Ferramentas Auxiliares

* **Streamlit:** Biblioteca open-source em Python para criar aplicativos web interativos de forma simples e rápida, ideal para projetos de ciência de dados e machine learning.
* **Render:** Plataforma de nuvem unificada que simplifica a implantação e o gerenciamento de aplicações, bancos de dados e serviços web.
* **Ngrok:** Ferramenta de tunelamento que cria uma URL pública e segura para um servidor local, expondo-o à internet.

---

## Resultados e Discussão

Para validar a eficácia da ferramenta, uma série de vídeos de exemplo foi submetida à plataforma.

### Imagens de exemplo

O projeto consegue anonimizar os rostos, preservando o contexto das imagens.
<img width="897" height="242" alt="image" src="https://github.com/user-attachments/assets/22d60dcd-0320-440a-9ed7-0ebd6c0aa369" />
<img width="938" height="306" alt="image" src="https://github.com/user-attachments/assets/216d0d92-66b1-4fe0-923e-427e23bcbf95" />
<img width="927" height="260" alt="image" src="https://github.com/user-attachments/assets/fee5b43b-c40e-481c-8cd8-3266ced6ed62" />

* Fonte original das imagens: Pixabay
* Fonte censurada: Autor

### Performance

A taxa de quadros por segundo (FPS) varia entre 15 e 30, dependendo de fatores como a duração e qualidade do vídeo, e o número de detecções de rostos.

### Preservação de Contexto

Um dos objetivos principais do projeto é anonimizar as imagens com a menor perda possível de contexto. Para validar isso, um modelo de inteligência artificial generativa, o **Gemini 2.5 Flash**, foi utilizado para analisar um frame anonimizado.

* **Prompt de entrada:** Descreva a imagem. O que ela retrata?
  <img width="860" height="500" alt="image" src="https://github.com/user-attachments/assets/b2705af4-a4eb-44dd-a451-308b93716b43" />


* **Resposta gerada pelo modelo:**
    > "Devido ao desfoque dos rostos, a imagem provavelmente foi editada para proteger a privacidade das pessoas retratadas. A situação, com as pessoas posando em fila em frente a um cenário de escritório, sugere um registro de momento profissional ou educacional, como:
    >
    > * Uma foto de equipe: É comum que grupos de trabalho tirem fotos para registrar a equipe ou para serem usadas em materiais internos.
    >
    > * Um evento de networking: O registro pode ser de um encontro ou workshop.
    >
    > * Uma foto de classe ou grupo de estudos: A disposição das pessoas pode indicar que são colegas de um curso ou faculdade.
    >
    > O objetivo da imagem parece ser documentar a presença dessas pessoas juntas, mas com a preocupação de não expor suas identidades individuais."

A análise do Gemini 2.5 Flash confirma que, mesmo com a anonimização, o contexto geral da imagem foi preservado, atingindo o objetivo do projeto.

---

# Ethicam

Ethicam is a video anonymization project, initially named as a combination of the words **Ethic** and **Camera**. The project provides a backend service that processes videos and blurs people's faces, ensuring their privacy.
<img width="945" height="647" alt="image" src="https://github.com/user-attachments/assets/e132d3b7-e637-4933-8e19-aa02c8a2865c" />

## Frontend

The application's frontend serves as an interface for users to test the anonymization service. It was developed in Python, using the **Streamlit** library, which made it easy to create a simple and interactive web interface.

Users can upload videos in MP4, MOV, AVI, and MKV formats. The frontend then sends the video to the backend service via a REST API, built with the **FastAPI** library. After processing, the anonymized video can be downloaded.

The frontend solution is hosted on the **Render** platform, in an instance with 512 MB of RAM and 0.1 CPU. The application is publicly available at **https://anonimization-front.onrender.com**.
<img width="760" height="426" alt="image" src="https://github.com/user-attachments/assets/ca9507d5-c558-4d16-b2e6-aebff5e5207d" />

## Backend

The project's backend was implemented on a **Google Colab** instance, using an NVIDIA Tesla T4 GPU with 16 GB of VRAM to process videos efficiently.

The anonymization process works as follows:
1. The received video is processed **frame by frame** with the **OpenCV** library.
2. A **Gaussian blur filter** (`GaussianBlur()`) is applied to the regions where people are detected, effectively blurring them.
3. This type of filter creates a more natural and smooth blur, preserving the image's edges and contours.

The backend is a **REST API** server, developed with **FastAPI**, which receives input videos and returns the processed video. For public access during development, the **Ngrok** tool was used to expose the Colab server to the internet.

---

## Auxiliary Tools

* **Streamlit:** An open-source Python library for creating interactive web applications simply and quickly, ideal for data science and machine learning projects.
* **Render:** A unified cloud platform that simplifies the deployment and management of applications, databases, and web services.
* **Ngrok:** A tunneling tool that creates a secure public URL for a local server, exposing it to the internet.

---

## Results and Discussion

To validate the tool's effectiveness, a series of example videos were submitted to the platform.

### Example Images

The project successfully anonymizes faces while preserving the images' context.
<img width="897" height="242" alt="image" src="https://github.com/user-attachments/assets/22d60dcd-0320-440a-9ed7-0ebd6c0aa369" />
<img width="938" height="306" alt="image" src="https://github.com/user-attachments/assets/216d0d92-66b1-4fe0-923e-427e23bcbf95" />
<img width="927" height="260" alt="image" src="https://github.com/user-attachments/assets/fee5b43b-c40e-481c-8cd8-3266ced6ed62" />

* Original image source: Pixabay
* Censored source: Author

### Performance

The frames per second (FPS) rate varies between 15 and 30, depending on factors such as video length and quality, and the number of face detections.

### Context Preservation

One of the project's main goals is to anonymize images with the least possible loss of context. To validate this, a generative AI model, **Gemini 2.5 Flash**, was used to analyze an anonymized frame.

* **Input prompt:** Describe the image. What does it portray?
  <img width="860" height="500" alt="image" src="https://github.com/user-attachments/assets/b2705af4-a4eb-44dd-a451-308b93716b43" />


* **Model-generated response:**
    > "Due to the blurred faces, the image was likely edited to protect the privacy of the people shown. The situation, with people posing in a line in front of an office background, suggests a professional or educational moment, such as:
    >
    > * A team photo: It's common for work groups to take photos to document the team or for internal use.
    >
    > * A networking event: The photo could be from a meeting or workshop.
    >
    > * A class or study group photo: The arrangement of the people may indicate that they are colleagues from a course or college.
    >
    > The image's purpose seems to be to document the presence of these people together, but with the concern of not exposing their individual identities."

The Gemini 2.5 Flash analysis confirms that even with anonymization, the general context of the image was preserved, achieving the project's objective.
