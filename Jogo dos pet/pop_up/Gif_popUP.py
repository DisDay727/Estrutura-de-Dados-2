import pyautogui
from PIL import Image, ImageTk
import tkinter as tk
from playsound import playsound
import threading
# --- Função para gerenciar a animação do GIF ---
def carregar_gif(label_widget, caminho_gif, frame_index=0):
    try:
        # Abre a imagem GIF
        img_gif = Image.open(caminho_gif)
        
        # Pega o número total de quadros (frames)
        total_frames = img_gif.n_frames
        
        # Seleciona o quadro atual
        img_gif.seek(frame_index)
        
        # Redimensiona o quadro (opcional)
        img_redimensionada = img_gif.resize((200, 200), Image.Resampling.LANCZOS)
        
        # Converte para formato compatível com Tkinter
        gif_tk = ImageTk.PhotoImage(img_redimensionada)
        
        # Atualiza o Label com o novo quadro
        label_widget.config(image=gif_tk)
        label_widget.image = gif_tk # Evita que seja apagado pelo garbage collector

        # Define o próximo quadro e o tempo de espera (duração do frame em ms)
        proximo_frame = (frame_index + 1) % total_frames
        duracao_frame = img_gif.info.get('duration', 100) # Padrão 100ms se não achar info

        # Agenda a chamada do próximo quadro para criar a animação
        # IMPORTANTE: Só agenda se o widget ainda existir
        if label_widget.winfo_exists():
            # Armazena o ID do job para poder cancelar depois se fechar a janela
            label_widget.after_id = label_widget.after(duracao_frame, carregar_gif, label_widget, caminho_gif, proximo_frame)

    except Exception as e:
        print(f"Erro ao carregar GIF: {e}")
        label_widget.config(text="Erro no GIF")


def tocar_audio():
    try:
        # Coloque o caminho do seu arquivo MP3 aqui
        playsound("audio/cat-haha-cat.mp3")
    except Exception as e:
        print(f"Erro ao reproduzir áudio: {e}")

def mostrar_popup_mouse():
    # Pega a posição atual do mouse
    x, y = pyautogui.position()
    
    # Toca o áudio em uma thread separada para não congelar a interface
    thread_audio = threading.Thread(target=tocar_audio)
    thread_audio.start()
    
    # Cria a janela pop-up
    popup = tk.Toplevel()
    popup.overrideredirect(True) # Remove as bordas da janela
    
    # Cria o Label que vai conter a animação
    label_animado = tk.Label(popup)
    label_animado.pack()
    
    # --- Caminho do seu arquivo GIF ---
    caminho_do_gif = "img/cat-haha-cat.gif" 
    
    # Inicia a animação no label criado
    carregar_gif(label_animado, caminho_do_gif)
    
    # Posiciona a janela na localização exata do mouse
    popup.geometry(f"+{x + 10}+{y + 10}")
    
    # --- Função para fechar e cancelar a animação ---
    def fechar_popup():
        # Cancela o agendamento do próximo frame para evitar erros
        if hasattr(label_animado, 'after_id'):
            label_animado.after_cancel(label_animado.after_id)
        popup.destroy()

    # Fechar a janela se clicar nela
    popup.bind("<Button-1>", lambda event: fechar_popup())
    
    # Fecha automaticamente após 3 segundos (3000 ms) e cancela a animação
    popup.after(3000, fechar_popup)

# --- Interface principal ---
root = tk.Tk()
root.title("Controlador de Pop-up com GIF")
root.geometry("350x180")

instrucao = tk.Label(root, text="Pressione a tecla 'P' ou clique no botão", font=("Arial", 10))
instrucao.pack(pady=15)

btn_ativar = tk.Button(root, text="Ativar Pop-up + GIF", command=mostrar_popup_mouse, font=("Arial", 11, "bold"))
btn_ativar.pack(pady=5)

root.bind("<Key-p>", lambda event: mostrar_popup_mouse())
root.focus_set()

root.mainloop()
