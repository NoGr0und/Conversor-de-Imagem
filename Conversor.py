import os
from tkinter import Tk, Label, Button, StringVar, OptionMenu, messagebox
from PIL import Image

# Pastas fixas
pasta_origem = "para converter"
pasta_destino = "ja convertido"

def converter_imagens():
    formato = formato_saida.get().upper()

    if not formato:
        messagebox.showwarning("Aviso", "Escolha o formato de saída.")
        return

    try:
        arquivos_convertidos = 0
        os.makedirs(pasta_destino, exist_ok=True)

        for arquivo in os.listdir(pasta_origem):
            extensao = os.path.splitext(arquivo)[1].lower()
            if extensao in [".webp", ".png", ".jpg", ".jpeg", ".bmp", ".tiff"]:
                caminho_completo = os.path.join(pasta_origem, arquivo)
                nome_base = os.path.splitext(arquivo)[0]
                novo_caminho = os.path.join(pasta_destino, nome_base + "." + formato.lower())

                with Image.open(caminho_completo) as img:
                    if formato == "JPG":
                        img.convert("RGB").save(novo_caminho, "JPEG")
                    else:
                        img.save(novo_caminho, format=formato)

                os.remove(caminho_completo)
                arquivos_convertidos += 1

        if arquivos_convertidos > 0:
            messagebox.showinfo("Sucesso", f"{arquivos_convertidos} imagem(ns) convertida(s) com sucesso!\nSalvas em: '{pasta_destino}'")
        else:
            messagebox.showwarning("Aviso", "Nenhuma imagem válida foi encontrada em 'para converter'.")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro:\n{str(e)}")

# Interface Gráfica
janela = Tk()
janela.title("Conversor de Imagens (WEBP → outro)")
janela.geometry("400x200")

formato_saida = StringVar(value="JPG")

Label(janela, text="Convertendo imagens de: 'para converter'").pack(pady=5)
Label(janela, text="Para pasta: 'ja convertido'").pack(pady=2)
Label(janela, text="Escolha o formato de saída:").pack(pady=10)

opcoes_formatos = ["JPG", "PNG", "WEBP", "BMP", "TIFF"]
OptionMenu(janela, formato_saida, *opcoes_formatos).pack(pady=5)

Button(janela, text="Converter Imagens", bg="#4CAF50", fg="white", command=converter_imagens).pack(pady=15)

janela.mainloop()