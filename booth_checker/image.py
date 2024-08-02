from PIL import Image, ImageFont, ImageDraw

# font = ImageFont.truetype('NanumSquareNeo-bRg.ttf', size=16)
font_size = 16

def font_init(size):
    global font, font_size

    font_size = size
    font = ImageFont.truetype("JetBrainsMono-Bold.ttf", size)

def print_line(img, order, status, current_string):
    global font

    # status 
    # 1 = Added
    # 2 = Deleted
    # 3 = Changed 

    line_color = 'rgb(255, 255, 255)'
    if status == 1:
        line_color = 'rgb(29, 66, 37)'
    elif status == 2:
        line_color = 'rgb(84, 35, 35)'
    elif status == 3:
        line_color = 'rgb(28, 63, 113)'

    draw = ImageDraw.Draw(img)
    draw.text((0, get_line_yoffset(order)), current_string, font=font, fill=line_color)
    

def make_image(x, y):
    image = Image.new('RGB', (x, y), color = 'rgb(15, 18, 22)')
    return image


def make_pathinfo_line(img, path_list):
    current_order = 0
    for pathinfo in path_list:
        print_line(img, current_order, pathinfo['status'], pathinfo['line_str'])
        current_order += 1

def get_line_yoffset(count):
    global font_size
    
    # x_offset = 64 * level
    y_offset = (font_size + 4) * count
    return y_offset

def get_image_size(level, count):
    x_offset = 64 * level
    y_offset = (font_size + 4) * count
    return (x_offset, y_offset)