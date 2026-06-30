import random
import tkinter as tk
from tkinter import font as tkfont
from perguntas import perguntas

TEMPO_LIMITE = 10  # segundos por pergunta

COR_FUNDO = "#fff3d6"
COR_CARD = "#fffdf6"
COR_BORDA = "#b5651d"
COR_TEXTO = "#4a2e0c"
COR_SUBTITULO = "#8a6a3f"
COR_OPT_BG = "#fffaf0"
COR_OPT_BORDA = "#e0c79a"
COR_OPT_HOVER = "#fff0d2"
COR_CORRETO_BG = "#eaf3de"
COR_CORRETO_TXT = "#27500a"
COR_ERRADO_BG = "#fcebeb"
COR_ERRADO_TXT = "#791f1f"


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Arraiá do cumpadi python")
        self.root.configure(bg=COR_FUNDO)
        self.root.geometry("560x620")
        #self.root.resizable(False, False)

        self.font_titulo = tkfont.Font(family="Helvetica", size=18, weight="bold")
        self.font_subtitulo = tkfont.Font(family="Helvetica", size=10)
        self.font_pergunta = tkfont.Font(family="Helvetica", size=13, weight="bold")
        self.font_opt = tkfont.Font(family="Helvetica", size=11)
        self.font_timer = tkfont.Font(family="Helvetica", size=12, weight="bold")
        self.font_feedback = tkfont.Font(family="Helvetica", size=11, weight="bold")
        self.font_final_emoji = tkfont.Font(family="Helvetica", size=36)
        self.font_final_titulo = tkfont.Font(family="Helvetica", size=16, weight="bold")

        self.pontos = 0
        self.idx = 0
        self.respondeu = False
        self.tempo_restante = TEMPO_LIMITE
        self.timer_job = None
        self.perguntas_sorteadas = []
        self.botoes_opcoes = []

        self.montar_layout_base()
        self.iniciar_jogo()

    def montar_layout_base(self):
        tk.Label(
            self.root, text="🌽 Arraiá do cumpadi python 🌽",
            font=self.font_titulo, bg=COR_FUNDO, fg=COR_BORDA
        ).pack(pady=(20, 0))

        tk.Label(
            self.root, text="Vamos testar o seu conhecimento junino, sô!",
            font=self.font_subtitulo, bg=COR_FUNDO, fg=COR_SUBTITULO
        ).pack(pady=(0, 15))

        self.card = tk.Frame(
            self.root, bg=COR_CARD, highlightbackground=COR_BORDA,
            highlightthickness=2, bd=0
        )
        self.card.pack(padx=20, pady=10, fill="both", expand=True)

        self.top_row = tk.Frame(self.card, bg=COR_CARD)
        self.top_row.pack(fill="x", padx=20, pady=(20, 5))

        self.lbl_progresso = tk.Label(
            self.top_row, text="", font=self.font_subtitulo,
            bg=COR_CARD, fg=COR_SUBTITULO
        )
        self.lbl_progresso.pack(side="left")

        self.lbl_pontos = tk.Label(
            self.top_row, text="", font=self.font_subtitulo,
            bg=COR_CARD, fg=COR_SUBTITULO
        )
        self.lbl_pontos.pack(side="left", expand=True)

        self.lbl_timer = tk.Label(
            self.top_row, text="", font=self.font_timer,
            bg="#faece7", fg=COR_BORDA, padx=10, pady=2
        )
        self.lbl_timer.pack(side="right")

        self.canvas_barra = tk.Canvas(
            self.card, height=8, bg="#f0e0c0", highlightthickness=0
        )
        self.canvas_barra.pack(fill="x", padx=20, pady=(5, 15))
        self.barra_id = self.canvas_barra.create_rectangle(
            0, 0, 0, 8, fill="#639922", width=0
        )

        self.lbl_pergunta = tk.Label(
            self.card, text="", font=self.font_pergunta, bg=COR_CARD,
            fg=COR_TEXTO, wraplength=460, justify="left"
        )
        self.lbl_pergunta.pack(fill="x", padx=20, pady=(0, 15), anchor="w")

        self.frame_opcoes = tk.Frame(self.card, bg=COR_CARD)
        self.frame_opcoes.pack(fill="x", padx=20)

        self.lbl_feedback = tk.Label(
            self.card, text="", font=self.font_feedback, bg=COR_CARD
        )
        self.lbl_feedback.pack(pady=(10, 20))

        self.frame_final = tk.Frame(self.card, bg=COR_CARD)

    def iniciar_jogo(self):
        self.perguntas_sorteadas = random.sample(perguntas, 10)
        self.idx = 0
        self.pontos = 0
        self.frame_final.pack_forget()
        self.top_row.pack(fill="x", padx=20, pady=(20, 5))
        self.canvas_barra.pack(fill="x", padx=20, pady=(5, 15))
        self.lbl_pergunta.pack(fill="x", padx=20, pady=(0, 15), anchor="w")
        self.frame_opcoes.pack(fill="x", padx=20)
        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)

        if self.idx >= len(self.perguntas_sorteadas):
            self.mostrar_resultado_final()
            return

        self.respondeu = False
        self.tempo_restante = TEMPO_LIMITE
        p = self.perguntas_sorteadas[self.idx]

        self.lbl_progresso.config(text=f"Pergunta {self.idx + 1} de {len(self.perguntas_sorteadas)}")
        self.lbl_pontos.config(text=f"Pontos: {self.pontos}")
        self.lbl_pergunta.config(text=p["pergunta"])
        self.lbl_feedback.config(text="")

        for widget in self.frame_opcoes.winfo_children():
            widget.destroy()
        self.botoes_opcoes = []

        for i, alternativa in enumerate(p["alternativas"], start=1):
            btn = tk.Button(
                self.frame_opcoes,
                text=f"{i} - {alternativa}",
                font=self.font_opt,
                bg=COR_OPT_BG,
                fg=COR_TEXTO,
                activebackground=COR_OPT_HOVER,
                relief="flat",
                anchor="w",
                padx=12,
                pady=8,
                highlightbackground=COR_OPT_BORDA,
                highlightthickness=1,
                bd=0,
                cursor="hand2",
                command=lambda escolha=i: self.responder(escolha)
            )
            btn.pack(fill="x", pady=4)
            self.botoes_opcoes.append(btn)

        self.atualizar_timer_ui()
        self.timer_job = self.root.after(1000, self.tick_timer)

    def tick_timer(self):
        self.tempo_restante -= 1
        self.atualizar_timer_ui()
        if self.tempo_restante <= 0:
            self.responder(None)
        else:
            self.timer_job = self.root.after(1000, self.tick_timer)

    def atualizar_timer_ui(self):
        self.lbl_timer.config(text=f"{self.tempo_restante}s")
        if self.tempo_restante <= 3:
            self.lbl_timer.config(bg=COR_ERRADO_BG, fg=COR_ERRADO_TXT)
            cor_barra = "#e24b4a"
        else:
            self.lbl_timer.config(bg="#faece7", fg=COR_BORDA)
            cor_barra = "#639922"

        largura_total = self.canvas_barra.winfo_width() or 460
        proporcao = max(self.tempo_restante, 0) / TEMPO_LIMITE
        self.canvas_barra.coords(self.barra_id, 0, 0, largura_total * proporcao, 8)
        self.canvas_barra.itemconfig(self.barra_id, fill=cor_barra)

    def responder(self, escolha):
        if self.respondeu:
            return
        self.respondeu = True
        if self.timer_job:
            self.root.after_cancel(self.timer_job)

        p = self.perguntas_sorteadas[self.idx]
        correta_idx = p["resposta"] - 1

        for btn in self.botoes_opcoes:
            btn.config(state="disabled", cursor="arrow")

        if escolha is None:
            self.botoes_opcoes[correta_idx].config(bg=COR_CORRETO_BG, fg=COR_CORRETO_TXT)
            self.lbl_feedback.config(text="⏰ Tempo esgotado!", fg=COR_ERRADO_TXT)
        elif escolha == p["resposta"]:
            self.pontos += 10
            self.botoes_opcoes[escolha - 1].config(bg=COR_CORRETO_BG, fg=COR_CORRETO_TXT)
            self.lbl_feedback.config(text="✅ Acertou!", fg=COR_CORRETO_TXT)
        else:
            self.botoes_opcoes[escolha - 1].config(bg=COR_ERRADO_BG, fg=COR_ERRADO_TXT)
            self.botoes_opcoes[correta_idx].config(bg=COR_CORRETO_BG, fg=COR_CORRETO_TXT)
            self.lbl_feedback.config(text="❌ Errou!", fg=COR_ERRADO_TXT)

        self.lbl_pontos.config(text=f"Pontos: {self.pontos}")
        self.root.after(1300, self.avancar)

    def avancar(self):
        self.idx += 1
        self.mostrar_pergunta()

    def titulo_final(self):
        if self.pontos >= 90:
            return "🏆 Mestre Junino!"
        elif self.pontos >= 70:
            return "🌽 Arretado!"
        elif self.pontos >= 50:
            return "🎉 Dançarino!"
        else:
            return "🤠 Continue treinando!"

    def mostrar_resultado_final(self):
        self.top_row.pack_forget()
        self.canvas_barra.pack_forget()
        self.lbl_pergunta.pack_forget()
        self.frame_opcoes.pack_forget()
        self.lbl_feedback.config(text="")

        for widget in self.frame_final.winfo_children():
            widget.destroy()

        tk.Label(
            self.frame_final, text="🎊", font=self.font_final_emoji, bg=COR_CARD
        ).pack(pady=(30, 10))

        tk.Label(
            self.frame_final, text="Fim do jogo!", font=self.font_pergunta,
            bg=COR_CARD, fg=COR_TEXTO
        ).pack(pady=(0, 4))

        tk.Label(
            self.frame_final, text=f"Sua pontuação foi: {self.pontos}",
            font=self.font_subtitulo, bg=COR_CARD, fg=COR_SUBTITULO
        ).pack(pady=(0, 4))

        tk.Label(
            self.frame_final, text=self.titulo_final(),
            font=self.font_final_titulo, bg=COR_CARD, fg=COR_BORDA
        ).pack(pady=(0, 25))

        tk.Button(
            self.frame_final, text="Jogar de novo",
            font=self.font_opt, bg=COR_BORDA, fg="#fffaf0",
            activebackground="#993c1d", relief="flat",
            padx=20, pady=10, cursor="hand2",
            command=self.iniciar_jogo
        ).pack()

        self.frame_final.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
