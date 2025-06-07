# %%
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

# %%
def filtro_passa_alta(imagem):
    # Kernel passa-alta 3x3
    kernel = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ])
    return cv2.filter2D(imagem, -1, kernel)

def high_boost(imagem, A=1.5):
    altura, largura = imagem.shape
    imagem_suavizada = np.zeros_like(imagem, dtype=float)

    # Kernel média 3x3
    kernel = np.ones((3, 3)) / 9.0

    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            vizinhos = imagem[i-1:i+2, j-1:j+2]
            valor_suavizado = np.sum(vizinhos * kernel)
            imagem_suavizada[i, j] = valor_suavizado

    mascara = imagem - imagem_suavizada
    high_boost = imagem + A * mascara

    high_boost = np.clip(high_boost, 0, 255)
    return high_boost.astype(np.uint8)


# %%
path = 'imagem_256.jpg' # Substitua pelo caminho correto da sua imagem

# Abre a imagem e converte para tons de cinza
imagem_pil = Image.open(path).convert('L')
imagem_cinza_np = np.array(imagem_pil)



# %%
filtro_pa = filtro_passa_alta(imagem_cinza_np)
high_boost_img = high_boost(imagem_cinza_np, A=1.5)


# %%
plt.figure(figsize=(20, 6))

plt.subplot(1, 3, 1)
plt.imshow(imagem_cinza_np, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(filtro_pa, cmap='gray')
plt.title("Passa-Alta OpenCV")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(high_boost_img, cmap='gray')
plt.title("High-Boost")
plt.axis('off')

plt.tight_layout()
plt.show()


