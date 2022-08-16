from PIL import Image

def img_converter(input_file, output_file, format):
    image = Image.open(input_file)
    image.save(output_file, format = format)

def img_format(input_file):
    imagem = Image.open(input_file)
    print(f"Formato: >>{imagem.format_description}<<")

if __name__ == "__main__":
    img_converter("img.jpg", "pizza.teste", "PNG")
    img_format("img.jpg")
    img_format("pizza.png")
    img_format("pizza.teste")
