from PIL import Image, ImageOps

def image_to_ascii(image_path: str, width: int, height: int, noletters: bool):
    image = Image.open(image_path)
    image = image.resize((width, height))

    image = image.convert("RGB")
    grayscale_image = ImageOps.grayscale(image)

    pixels=grayscale_image.getdata()
    if noletters is True:
        grayRamp = '$@%8&#*|(){}[]?-_+~<>!;:,"^`\'.'
    else:
        grayRamp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft\|()1{}[]?-_+~<>i!lI;:,^`."
    
    rampsize = len(grayRamp)

    for y in range(height):
        for x in range(width):
            r,g,b = image.getdata()[(y*width)+x]
            brightness = pixels[(y*width)+x]
            value = round(((rampsize/255)*brightness)-1)
            print(f"\033[38;2;{r};{g};{b}m",grayRamp[value], end="")
        print()

image = input ("Enter Path :") 
image_to_ascii(image, 128, 64, False)

