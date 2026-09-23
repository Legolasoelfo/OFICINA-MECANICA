"""
Sistema de Controle de Ocupação de Boxes - Oficina Mecânica
Projeto acadêmico - UEMG
Paradigma: PROCEDURAL PURO (sem classes/objetos personalizados)
Interface: tkinter + tkinter.ttk (ttk.Style)

Equipe: Victor Silva Granja, Davi da Silva Fonseca Vilete, Eurico
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ============================================================
# CONSTANTES (UPPER_CASE) - parâmetros fixos do domínio
# ============================================================
TOTAL_BOXES = 8      # Quantidade fixa de boxes/elevadores da oficina
BOX_VAZIO = 0        # Estado: box livre
BOX_OCUPADO = 1      # Estado: box em uso

# ============================================================
# VARIÁVEIS GLOBAIS - estado da aplicação (sem classes/objetos)
# ============================================================
vetorBoxes = [BOX_VAZIO] * TOTAL_BOXES

totalCarrosAtendidos = 0       
expedienteEncerrado = False    

# Referências aos widgets, preenchidas na construção da tela
botoesBox = []
labelOcupados = None
labelAtendidos = None
labelStatusExpediente = None

frameTelaInicial = None
frameSistema = None

# ============================================================
# FUNÇÕES DE LÓGICA (procedurais)
# ============================================================

def contarOcupados():
    return sum(vetorBoxes)

def alternarBox(indice):
    global totalCarrosAtendidos

    if expedienteEncerrado:
        messagebox.showwarning(
            "Expediente encerrado",
            "Não é possível alterar boxes após o encerramento do expediente."
        )
        return

    if vetorBoxes[indice] == BOX_VAZIO:
        vetorBoxes[indice] = BOX_OCUPADO
        totalCarrosAtendidos += 1
    else:
        vetorBoxes[indice] = BOX_VAZIO

    atualizarInterface()

def encerrarExpediente():
    global expedienteEncerrado

    if expedienteEncerrado:
        messagebox.showinfo("Expediente encerrado", "O expediente já foi encerrado.")
        return

    resposta = messagebox.askyesno(
        "Encerrar expediente",
        "Confirma o encerramento do expediente?\nOs boxes serão bloqueados para novas alterações."
    )
    if not resposta:
        return

    expedienteEncerrado = True
    atualizarInterface()
    messagebox.showinfo(
        "Resumo do expediente",
        f"Total de carros atendidos no expediente: {totalCarrosAtendidos}"
    )

def atualizarInterface():
    ocupados = contarOcupados()

    for i in range(TOTAL_BOXES):
        botao = botoesBox[i]

        if vetorBoxes[i] == BOX_OCUPADO:
            botao.configure(text=f"Box {i + 1}\nOCUPADO", style="Ocupado.TButton")
        else:
            botao.configure(text=f"Box {i + 1}\nLIVRE", style="Livre.TButton")

        if expedienteEncerrado:
            botao.state(["disabled"])
        else:
            botao.state(["!disabled"])

    labelOcupados.configure(text=f"Boxes ocupados: {ocupados}/{TOTAL_BOXES}")
    labelAtendidos.configure(text=f"Carros atendidos no expediente: {totalCarrosAtendidos}")

    if expedienteEncerrado:
        labelStatusExpediente.configure(text="EXPEDIENTE ENCERRADO", foreground="#B00020")
    else:
        labelStatusExpediente.configure(text="Expediente em andamento", foreground="#1B5E20")

def exibirTelaSistema():
    frameTelaInicial.pack_forget()
    frameSistema.pack(fill="both", expand=True)

# ============================================================
# CONSTRUÇÃO DA INTERFACE (SEQUÊNCIA)
# ============================================================

def construirInterface():
    global botoesBox, labelOcupados, labelAtendidos, labelStatusExpediente
    global frameTelaInicial, frameSistema

    janela = tk.Tk()
    janela.title("Sistema de Controle de Boxes - Oficina Mecânica")
    janela.geometry("600x600")
    janela.resizable(False, False)
    
    # --- Estilo nativo (ttk.Style) melhorado ---
    estilo = ttk.Style(janela)
    estilo.theme_use("clam")
    
    corFundo = "#F4F6F8"
    janela.configure(bg=corFundo)
    
    estilo.configure("TFrame", background=corFundo)
    estilo.configure("TLabel", background=corFundo)
    
    estilo.configure("Livre.TButton", background="#4CAF50", foreground="white", font=("Segoe UI", 11, "bold"), padding=10)
    estilo.map("Livre.TButton", background=[("active", "#45a049")])
    
    estilo.configure("Ocupado.TButton", background="#F44336", foreground="white", font=("Segoe UI", 11, "bold"), padding=10)
    estilo.map("Ocupado.TButton", background=[("active", "#d32f2f")])
    
    estilo.configure("Acao.TButton", background="#2196F3", foreground="white", font=("Segoe UI", 12, "bold"), padding=10)
    estilo.map("Acao.TButton", background=[("active", "#1976d2")])
    
    estilo.configure("Titulo.TLabel", font=("Segoe UI", 20, "bold"), foreground="#333333")
    estilo.configure("SubTitulo.TLabel", font=("Segoe UI", 12), foreground="#666666")
    estilo.configure("Info.TLabel", font=("Segoe UI", 12))

    # ==========================================
    # 1. TELA INICIAL
    # ==========================================
    frameTelaInicial = ttk.Frame(janela)
    
    frameCentro = ttk.Frame(frameTelaInicial)
    frameCentro.pack(expand=True)
    
    ttk.Label(frameCentro, text="Bem-vindo(a) ao Sistema", style="Titulo.TLabel").pack(pady=(0, 5))
    ttk.Label(frameCentro, text="Controle de Ocupação de Boxes - Oficina Mecânica", style="SubTitulo.TLabel").pack(pady=(0, 30))
    
    ttk.Label(frameCentro, text="Equipe:\nVictor Silva Granja\nDavi da Silva Fonseca Vilete\nEurico", justify="center", style="Info.TLabel").pack(pady=(0, 40))
    
    ttk.Button(frameCentro, text="ENTRAR NO SISTEMA", style="Acao.TButton", command=exibirTelaSistema, cursor="hand2").pack(ipadx=20)


    # ==========================================
    # 2. TELA DO SISTEMA PRINCIPAL
    # ==========================================
    frameSistema = ttk.Frame(janela)

    frameTitulo = ttk.Frame(frameSistema, padding=20)
    frameTitulo.pack(fill="x")
    ttk.Label(frameTitulo, text="Painel de Controle dos Boxes", style="Titulo.TLabel").pack()

    frameBoxes = ttk.Frame(frameSistema, padding=10)
    frameBoxes.pack()

    for i in range(TOTAL_BOXES):
        botao = ttk.Button(
            frameBoxes,
            text=f"Box {i + 1}\nLIVRE",
            style="Livre.TButton",
            width=12,
            cursor="hand2",
            command=lambda indice=i: alternarBox(indice)
        )
        linha = i // 4
        coluna = i % 4
        botao.grid(row=linha, column=coluna, padx=8, pady=8, ipady=15)
        botoesBox.append(botao)

    frameInfo = ttk.Frame(frameSistema, padding=20)
    frameInfo.pack(fill="x")

    labelOcupados = ttk.Label(frameInfo, text="", style="Info.TLabel")
    labelOcupados.pack(anchor="w")

    labelAtendidos = ttk.Label(frameInfo, text="", style="Info.TLabel")
    labelAtendidos.pack(anchor="w")

    labelStatusExpediente = ttk.Label(frameInfo, text="", style="Info.TLabel", font=("Segoe UI", 12, "bold"))
    labelStatusExpediente.pack(anchor="w", pady=(10, 0))

    frameAcoes = ttk.Frame(frameSistema, padding=20)
    frameAcoes.pack(fill="x", side="bottom")
    ttk.Button(frameAcoes, text="Encerrar Expediente", style="Acao.TButton", command=encerrarExpediente, cursor="hand2").pack(fill="x")
    ttk.Button(frameAcoes, text="Sair do Sistema", style="Acao.TButton", command=janela.destroy, cursor="hand2").pack(fill="x", pady=(10, 0))

    frameTelaInicial.pack(fill="both", expand=True)

    atualizarInterface()
    janela.mainloop()

if __name__ == "__main__":
    construirInterface()
