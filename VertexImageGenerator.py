import os
import vertexai
from vertexai.vision_models import ImageGenerationModel
from PIL import Image, ImageDraw, ImageFont

# Vertex AI yapılandırması
vertexai.init(
    project=os.getenv("VERTEX_PROJECT_ID", "YOUR_PROJECT_ID"),
    location=os.getenv("VERTEX_LOCATION", "us-central1")
)

def generateImage(num_characters, max_length, location, style, movie, dialogue):
    print("Generating image...")

    try:
        imagen_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")

        prompt_for_image = (
            f"Scene from the movie '{movie}', located at {location}, "
            f"with {num_characters} characters speaking up to {max_length} words each. "
            f"Render it in {style} style. Focus on atmosphere, setting, and character actions. "
            f"Dialogue context: {dialogue[:150]}"
        )

        response = imagen_model.generate_images(
            prompt=prompt_for_image,
            number_of_images=1,
            aspect_ratio='9:16'
        )

        image = response.images[0]
        image_path = "generated_image.png"
        image.save(image_path)

        # Diyalog yazdırma
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except:
            font = ImageFont.load_default()

        wrapped_text = "\n".join([dialogue[i:i+60] for i in range(0, len(dialogue), 60)])
        draw.text((20, 20), wrapped_text, fill="white", font=font)

        image_with_text_path = "generated_image_with_text.png"
        img.save(image_with_text_path)
        print("✅ Görsel + Diyalog başarıyla oluşturuldu ve kaydedildi.")

        return image_with_text_path

    except Exception as e:
        raise RuntimeError(f"[ERROR] Görsel üretilemedi: {str(e)}")
