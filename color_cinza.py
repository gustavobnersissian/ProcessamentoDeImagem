from PIL import Image

def muda_para_cinza(imagem_entrada, imagem_saida):
    imagem = Image.open(imagem_entrada)
    imagem = imagem.convert("1")
    imagem.save(imagem_saida)

if __name__ == "__main__":
    muda_para_cinza("img.jpg", "blacknwhite.jpg")