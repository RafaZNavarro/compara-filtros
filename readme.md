# Processamento de Imagens: Filtros Passa-Alta e High-Boost

Este código demonstra a aplicação de dois filtros de realce de imagens:
1. Filtro Passa-Alta para detecção de bordas
2. Filtro High-Boost para realce de detalhes finos

## Funcionalidades Principais

- Aplicação de filtro passa-alta com kernel 3x3
- Implementação do filtro high-boost com parâmetro ajustável
- Visualização comparativa dos resultados
- Processamento de imagens em tons de cinza

## Requisitos

- Python 3.6+
- Bibliotecas:
  - OpenCV (cv2)
  - NumPy
  - Matplotlib
  - Pillow (PIL)

Instale as dependências com:
pip install opencv-python numpy matplotlib pillow

## Como Usar

1. Coloque sua imagem na pasta do projeto
2. Modifique a variável 'path' no código para apontar para sua imagem
3. Execute o script

Exemplo:
path = 'imagem.jpg'  # Substitua pelo caminho da sua imagem

## Parâmetros Ajustáveis

- Filtro High-Boost:
  - A: Fator de realce (padrão=1.5)
  - Valores típicos: 1.0-2.0
  - Exemplo: high_boost(imagem, A=1.8)

## Saídas do Programa

Visualização comparativa contendo:
1. Imagem original em tons de cinza
2. Resultado do filtro passa-alta
3. Resultado do filtro high-boost

## Explicação Técnica

1. Filtro Passa-Alta:
   - Kernel utilizado:
     [-1, -1, -1]
     [-1,  8, -1]
     [-1, -1, -1]
   - Realça bordas e transições bruscas
   - Suprime áreas de intensidade constante

2. Filtro High-Boost:
   - Combina imagem original com sua máscara de alta frequência
   - Processo:
     1. Suavização da imagem (filtro média 3x3)
     2. Cálculo da máscara = original - suavizada
     3. Realce = original + A*máscara
   - Preserva detalhes finos enquanto realça bordas

## Aplicações Típicas

- Melhoria de imagens médicas
- Pré-processamento para visão computacional
- Realce de detalhes em fotografia
- Pré-processamento para OCR

## Observações

1. Para melhores resultados:
   - Use imagens com boa iluminação
   - Valores altos de A podem introduzir ruído
   
2. O código inclui proteção contra overflow:
   - np.clip garante valores entre 0-255