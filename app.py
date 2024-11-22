# app.py
from flask import Flask, request, jsonify
from pdf_handler import download_pdf, extract_text_from_pdf
import ollama

app = Flask(__name__)

def ask_llama(question, pdf_text):
    prompt = f"Voici un extrait du document :\n\n{pdf_text}\n\nQuestion : {question}"
    response = ollama.chat(
        model="llama2", 
        prompt=prompt,
        temperature=0.7
    )
    return response['text']

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    file_path = data['file_path']
    question = data['question']
    
    download_pdf(file_path, 'file.pdf')
    
    pdf_text = extract_text_from_pdf('file.pdf')
    
    answer = ask_llama(question, pdf_text)
    
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
