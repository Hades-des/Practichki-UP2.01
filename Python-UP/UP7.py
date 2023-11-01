from PIL import Image, ImageDraw, ImageFont, ImageEnhance


image_path = '../other/image.png'
image = Image.open(image_path)


width, height = image.size


half_width = width // 2
half_image = image.crop((0, 0, half_width, height))

enhancer = ImageEnhance.Contrast(half_image)
enhanced_half_image = enhancer.enhance(2.0)

result_image = Image.new('RGB', (width, height))
result_image.paste(enhanced_half_image, (0, 0))
result_image.paste(image.crop((half_width, 0, width, height)), (half_width, 0))

draw = ImageDraw.Draw(result_image)
rectangle_coords = [(100, 50), (300, 150)]
draw.rectangle(rectangle_coords, outline='red')

font = ImageFont.load_default()
font_size = 20
font_color = 'white'
draw.text((120, 100), 'Zagrumnyj Phillipp', font=font, fill=font_color)
draw.text((100, 180), '8 Variant', font=font, fill=font_color)


result_image.save('result_image.png')
