import os
import struct
import glob

def get_image_dimensions(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        if data[:2] == b'\xff\xd8':
            i = 2
            while i < len(data) - 9:
                if data[i] == 0xFF:
                    marker = data[i+1]
                    if marker in [0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF]:
                        height = struct.unpack('>H', data[i+5:i+7])[0]
                        width = struct.unpack('>H', data[i+7:i+9])[0]
                        return width, height
                    elif marker == 0xE0 or (marker >= 0xE1 and marker <= 0xEF):
                        segment_length = struct.unpack('>H', data[i+2:i+4])[0]
                        i += 2 + segment_length
                        continue
                    elif marker == 0xD8:
                        i += 2
                        continue
                    elif marker == 0xD9:
                        break
                i += 1
        elif data[:8] == b'\x89PNG\r\n\x1a\n':
            width = struct.unpack('>I', data[16:20])[0]
            height = struct.unpack('>I', data[20:24])[0]
            return width, height
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return 1000, 1000 # default

dirs = ['2026-home-coming', '2026-invited-talk', '2026-kcc']
for d in dirs:
    img_dir = f'assets/img/activities/{d}'
    md_file = f'_activities/{d}.md'
    images = glob.glob(f'{img_dir}/*')
    if not images:
        print(f'No images found in {img_dir}')
        continue
    
    title = d.replace('-', ' ').title().replace('Kcc', 'KCC')
    date = '2026-06-01' # default date
    
    md = f'''---
layout: post
title: "{title}"
date: {date}
description: "Photos from {title}"
img: /{img_dir}/{os.path.basename(images[0])}
importance: 1
category: event
images:
  photoswipe: true
---

<div class="pswp-gallery pswp-gallery--single-column" id="gallery-{d}">
'''
    for img in images:
        w, h = get_image_dimensions(img)
        fname = os.path.basename(img)
        md += f'''  <a href="/{img_dir}/{fname}"
    target="_blank" data-pswp-width="{w}" data-pswp-height="{h}">
    <img src="/{img_dir}/{fname}" alt="" />
  </a>
'''
    md += '</div>\n'
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f'Created {md_file} with {len(images)} images')
