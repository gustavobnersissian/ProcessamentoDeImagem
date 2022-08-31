from PIL import Image
from lib2to3.pytree import convert

def muda_para_cinza(imagem_entrada, imagem_saida):
    imagem = Image.open(imagem_entrada)
    imagem = imagem.convert("P", palette= Image.Palette.ADAPTIVE, colors = 4)
    imagem.save(imagem_saida)

if __name__ == "__main__":
    muda_para_cinza("img.jpg", "blacknwhite.png")