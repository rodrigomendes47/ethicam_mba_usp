import cv2
import numpy as np
from ultralytics import YOLO
import tempfile
import os


def _censor_frame(frame, yolo_model):
    """
    Função auxiliar para censurar pessoas em um único quadro (frame).
    Recebe um quadro e o modelo YOLO já carregado.
    """
    if yolo_model is None:
        print("Modelo YOLO não está carregado. Ignorando a censura.")
        return frame

    # Fazer a predição com o YOLO no quadro
    results = yolo_model.predict(source=frame, conf=0.25, verbose=False)

    # Obter as detecções (caixas delimitadoras)
    detections = results[0].boxes.data

    for detection in detections:
        x1, y1, x2, y2, conf, cls = detection
        if int(cls) == 0:
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])

            # Garantir que as coordenadas não saiam dos limites da imagem
            y1, y2 = max(0, y1), min(frame.shape[0], y2)
            x1, x2 = max(0, x1), min(frame.shape[1], x2)

            # Se a caixa delimitadora for válida
            if y1 < y2 and x1 < x2:
                # Extrair a região da pessoa
                person_region = frame[y1:y2, x1:x2]

                # Aplicar o filtro de desfoque (blur)
                # O tamanho do kernel (ex: (51, 51)) deve ser ímpar
                blurred_region = cv2.GaussianBlur(person_region, (71, 71), 30)

                # Substituir a região original pela desfocada
                frame[y1:y2, x1:x2] = blurred_region

    return frame

def censor_video_from_bytes(video_bytes: bytes) -> bytes:
    try:
        model = YOLO("yolo11s.pt").to("cuda")
    except Exception as e:
        print(f"Erro ao carregar o modelo YOLO. {e}")
        model = None

    if model is None:
        raise RuntimeError("O modelo YOLO não pôde ser carregado. A função não pode continuar.")

    # Usamos arquivos temporários para manipular os dados do vídeo com o OpenCV
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_input_file:
        temp_input_file.write(video_bytes)
        input_video_path = temp_input_file.name

    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_output_file:
        output_video_path = temp_output_file.name

    try:
        # Abrir o vídeo de entrada
        cap = cv2.VideoCapture(input_video_path)
        if not cap.isOpened():
            raise IOError("Não foi possível abrir o vídeo a partir dos bytes fornecidos.")

        # Obter propriedades do vídeo para criar o vídeo de saída
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Codec de vídeo - 'mp4v' é amplamente compatível
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

        # Processar quadro a quadro
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Censurar o quadro atual
            censored_frame = _censor_frame(frame, model)

            # Escrever o quadro processado no arquivo de saída
            out.write(censored_frame)

        # Liberar os recursos
        cap.release()
        out.release()

        # Ler os bytes do vídeo processado para retornar
        with open(output_video_path, 'rb') as f:
            processed_video_bytes = f.read()
        return processed_video_bytes

    finally:
        # Limpar os arquivos temporários
        if os.path.exists(input_video_path):
            os.remove(input_video_path)
        if os.path.exists(output_video_path):
            os.remove(output_video_path)

