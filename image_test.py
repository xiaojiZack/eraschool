import PIL.Image as image
layer1 = image.open("res\\image\\image_test\\add.png").convert('RGBA')
layer2 = image.open('res\\image\\image_test\\cut.png').convert('RGBA')

final = image.new('RGBA', layer1.size)
final = image.alpha_composite(final, layer1)
final = image.alpha_composite(final, layer2)

final = final.convert('RGB')
final = final.save('res\\image\\image_test\\test.png')