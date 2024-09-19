from rembg import remove
from PIL import Image
input_path = 'img.jpg'
output_path = 'img_.png'
aaa = Image.open(input_path)
output = remove(aaa)
output.show()