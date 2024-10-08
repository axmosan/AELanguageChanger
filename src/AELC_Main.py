import os
from tkinter import Tk, Button

# ドキュメントフォルダのパス
documents_path = os.path.expanduser("~/Documents")
japanese_file = os.path.join(documents_path, "ae_force_japanese.txt")
english_file = os.path.join(documents_path, "ae_force_english.txt")

# Japaneseボタンが押されたときの処理
def set_japanese():
    if not os.path.exists(japanese_file):
        # "ae_force_japanese.txt"が無ければ作成
        open(japanese_file, 'w').close()
    if os.path.exists(english_file):
        # "ae_force_english.txt"があれば削除して日本語ファイルを作成
        os.remove(english_file)
        open(japanese_file, 'w').close()
    root.destroy()  # ウィンドウを正しく終了

# Englishボタンが押されたときの処理
def set_english():
    if not os.path.exists(english_file):
        # "ae_force_english.txt"が無ければ作成
        open(english_file, 'w').close()
    if os.path.exists(japanese_file):
        # "ae_force_japanese.txt"があれば削除して英語ファイルを作成
        os.remove(japanese_file)
        open(english_file, 'w').close()
    root.destroy()  # ウィンドウを正しく終了

# メインウィンドウの設定
root = Tk()
root.title("Adobe After Effects Language Changer")
root.geometry("300x100")

# ボタンの配置
btn_japanese = Button(root, text="Japanese", command=set_japanese)
btn_japanese.pack(pady=10)

btn_english = Button(root, text="English", command=set_english)
btn_english.pack(pady=10)

# GUIのループを開始
root.mainloop()
