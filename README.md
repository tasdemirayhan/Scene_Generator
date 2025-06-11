# SceneGen 🎬✨

**SceneGen** is a Python-based AI-powered tool that generates cinematic **scene dialogues** and **corresponding visuals** based on user-provided parameters.

## Features 🚀

✅ Generate film dialogues and descriptions using **Gemini (LLM)**  
✅ Generate corresponding **scene visuals** using **Vertex AI Imagen**  
✅ Customize:
- Number of characters  
- Max dialogue length  
- Location  
- Visual style  

✅ Combine dialogue + image  
✅ Interactive **GUI (Tkinter)**  
✅ Save dialogue and visual locally

## How it works 🛠️

1️⃣ User selects a movie or provides a prompt  
2️⃣ Provides parameters:
- Number of characters  
- Max dialogue length  
- Location  
- Style  

3️⃣ **Scene dialogue and description** generated with **Gemini**  
4️⃣ **Scene visual** generated with **Vertex AI Imagen**  
5️⃣ Dialogue is embedded on the visual  
6️⃣ Output is saved locally

## Technologies used 🖥️

- Python 🐍  
- Tkinter (GUI)  
- Google Vertex AI  
  - Gemini LLM  
  - Imagen 3.0 image generation  
- BeautifulSoup & Requests (for IMDb scraping)

## Example Output 🎬🖼️

_(Here you can add example screenshots from your project - generated dialogue + image)_

## Disclaimer ℹ️

This repository contains only the **source code of the SceneGen project**.  
Due to API key security and quota limitations, my **Vertex AI / Gemini project keys are not shared** in this repository.  
👉 Please configure your own Google Cloud Project and API keys to run the application successfully.

## Why SceneGen?

SceneGen was developed as part of a course project to demonstrate how **Generative AI** can be used in **creative storytelling**, film prototyping, and multimedia applications.

---

**Türkçe:**  
Bu repository yalnızca **SceneGen** projesinin kaynak kodunu içermektedir.  
**Google Cloud API keyleri / Servis Hesap Anahtarları güvenlik nedeniyle paylaşılmamaktadır.**  
Uygulamayı çalıştırmak için kendi Google Cloud projenizi oluşturup gerekli API keylerini yapılandırmanız gerekmektedir.

---

## License

MIT License
