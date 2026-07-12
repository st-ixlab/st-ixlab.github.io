---
name: create_activity_post
description: Use this skill when the user asks to create an activity post or gallery from a folder of images. It ensures correct image dimensions (including EXIF rotation) are calculated and used for the Photoswipe gallery.
---

# Create Activity Post Workflow

When the user asks you to create an activity post (e.g., "Make an activity post for 2026-icml") using photos they uploaded:

1. Identify the image directory. Usually, it is located at `d:\lab-web\st-ixlab.github.io\assets\img\activities\<event-name>`.
2. Run the helper PowerShell script to extract correct image sizes (including EXIF rotation) to ensure portrait photos are not squished or stretched in the UI:
   `powershell -ExecutionPolicy Bypass -File .agents\skills\create_activity_post\scripts\get_image_sizes.ps1 -DirectoryPath "assets\img\activities\<event-name>"`
3. Use the output of the script to correctly set `data-pswp-width` and `data-pswp-height` for each image.
4. Create the `_activities/<event-name>.md` markdown file. The Markdown file format should match existing activity posts exactly, leveraging `<div class="pswp-gallery pswp-gallery--single-column" id="gallery-<event-name>">` and having an `images: photoswipe: true` frontmatter property.
