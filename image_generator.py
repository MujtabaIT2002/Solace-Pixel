from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def generate_post(image_path, quote, reference, output_path="output.png"):
    canvas_width, canvas_height = 1080, 1350
    image_max_height = 1080
    bg_color = (0, 0, 0)
    padding = 30

    quote_font_size = 70
    ref_font_size = 38

    quote_font = ImageFont.truetype("fonts/PPNeueBit-Bold.otf", quote_font_size)
    ref_font = ImageFont.truetype("fonts/PPMondwest-Regular.otf", ref_font_size)

    original = Image.open(image_path).convert("RGB")
    aspect_ratio = original.width / original.height
    new_width = canvas_width
    new_height = int(canvas_width / aspect_ratio)
    resized = original.resize((new_width, new_height), Image.LANCZOS)

    canvas = Image.new("RGB", (canvas_width, canvas_height), bg_color)

    if new_height > image_max_height:
        top_crop = (new_height - image_max_height) // 2
        cropped = resized.crop((0, top_crop, new_width, top_crop + image_max_height))
        paste_y = 0
        canvas.paste(cropped, (0, paste_y))
    else:
        paste_y = 0
        canvas.paste(resized, (0, paste_y))

    draw = ImageDraw.Draw(canvas)

    wrapped_quote = textwrap.fill(quote, width=40)
    quote_bbox = draw.textbbox((0, 0), wrapped_quote, font=quote_font)
    ref_bbox = draw.textbbox((0, 0), reference, font=ref_font)

    total_text_height = (quote_bbox[3] - quote_bbox[1]) + padding + (ref_bbox[3] - ref_bbox[1])
    text_space_start = paste_y + image_max_height
    text_space_end = canvas_height
    available_space = text_space_end - text_space_start
    text_block_y = text_space_start + (available_space - total_text_height) // 2

    quote_x = (canvas_width - quote_bbox[2]) // 2
    draw.text((quote_x, text_block_y), wrapped_quote, font=quote_font, fill="white")

    ref_x = (canvas_width - ref_bbox[2]) // 2
    ref_y = text_block_y + (quote_bbox[3] - quote_bbox[1]) + padding
    draw.text((ref_x, ref_y), reference, font=ref_font, fill="white")

    canvas.save(output_path)
    return output_path
