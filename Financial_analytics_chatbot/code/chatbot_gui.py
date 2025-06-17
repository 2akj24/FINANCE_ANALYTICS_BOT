import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from chatbot import ask_bot

class ChatbotGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("\U0001F4CA Financial Analytics Chatbot")
        self.geometry("700x600")
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.create_widgets()
        self.show_welcome()

    def create_widgets(self):
        # Configure main window colors
        self.configure(bg='#f0f0f0')
        
        # Chat area
        self.chat_area = scrolledtext.ScrolledText(self, font=("Helvetica", 12), wrap=tk.WORD)
        self.chat_area.config(state="disabled", bg='white', padx=10, pady=10)
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Input frame
        frame = tk.Frame(self, bg='#f0f0f0')
        frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.entry = tk.Entry(frame, font=("Helvetica", 12), bd=2, relief=tk.GROOVE)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,5))
        self.entry.bind("<Return>", self.on_send)
        self.entry.focus_set()

        # Buttons
        send_btn = tk.Button(frame, text="Send", command=self.on_send, bg='#4CAF50', fg='white')
        send_btn.pack(side=tk.LEFT)
        
        # Bottom buttons frame
        bottom_frame = tk.Frame(self, bg='#f0f0f0')
        bottom_frame.pack(fill=tk.X, padx=10, pady=(0,10))
        
        export_btn = tk.Button(bottom_frame, text="Export Chat", command=self.export_chat, bg='#2196F3', fg='white')
        export_btn.pack(side=tk.LEFT, padx=(0,5))
        
        clear_btn = tk.Button(bottom_frame, text="Clear Chat", command=self.clear_chat, bg='#f44336', fg='white')
        clear_btn.pack(side=tk.LEFT)
        
        exit_btn = tk.Button(bottom_frame, text="Exit", command=self.on_close, bg='#607D8B', fg='white')
        exit_btn.pack(side=tk.RIGHT)

    def show_welcome(self):
        self._display("\U0001F916 Welcome! Ask me about companies, metrics, trends, comparisons…")
        self._display("\U0001F916 Type 'help' to see example questions.")

    def _display(self, msg):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, msg + "\n\n")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)

    def on_send(self, event=None):
        q = self.entry.get().strip()
        if not q:
            return
            
        if q.lower() == 'exit':
            self.on_close()
            return
            
        self._display(f"\U0001F464 You: {q}")
        self.entry.delete(0, tk.END)
        
        try:
            ans = ask_bot(q)
            self._display(f"\U0001F916 Bot: {ans}")
        except Exception as e:
            self._display(f"\U0001F916 Bot: An error occurred: {str(e)}")

    def export_chat(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if path:
            try:
                with open(path, "w") as f:
                    f.write(self.chat_area.get("1.0", tk.END))
                self._display(f"\U0001F4D2 Chat exported to {path}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export chat: {str(e)}")

    def clear_chat(self):
        self.chat_area.config(state="normal")
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.config(state="disabled")
        self.show_welcome()

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to exit the chatbot?"):
            self.destroy()

if __name__ == "__main__":
    app = ChatbotGUI()
    app.mainloop()