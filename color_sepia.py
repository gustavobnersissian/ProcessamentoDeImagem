from lib2to3.pytree import convert
from PIL import Image

def calcula_paleta(branco):
    paleta = []
    r, g, b = branco
    for i in range(255):
        new_red = r * i // 255
        new_green = g * i // 255
        new_blue = b * i // 255
        paleta.extend((new_red, new_green, new_blue))
    return paleta

def converte_sepia(input, output):
    branco = (200, 1, 100)
    paleta = calcula_paleta(branco)

    imagem = Image.open(input)
    imagem = imagem.convert("L")
    imagem.putpalette(paleta)
    sepia = imagem.convert("RGB")

    sepia.save(output)

if __name__ == "__main__":
    converte_sepia("img.jpg", "pizza_sepia.png")