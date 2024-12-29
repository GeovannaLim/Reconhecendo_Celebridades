import boto3

# Inicializa o cliente do Rekognition
rekognition = boto3.client('rekognition')

def reconhecer_celebridades(imagem_path):
    # Lê a imagem localmente
    with open(imagem_path, 'rb') as image_file:
        image_bytes = image_file.read()

    # Chama o serviço do Rekognition para identificar celebridades
    response = rekognition.recognize_celebrities(
        Image={'Bytes': image_bytes}
    )
    
    # Verifica se há celebridades reconhecidas
    if 'CelebrityFaces' in response and len(response['CelebrityFaces']) > 0:
        print("Celebrities found:")
        for celebrity in response['CelebrityFaces']:
            print(f"Name: {celebrity['Name']}")
            print(f"Confidence: {celebrity['Confidence']:.2f}%")
            print(f"Bounding Box: {celebrity['BoundingBox']}")
    else:
        print("No celebrities found.")

# Caminho para a imagem que será analisada
imagem_path = 'caminho/para/sua/imagem.jpg'

# Chama a função para reconhecer celebridades na imagem
reconhecer_celebridades(imagem_path)
