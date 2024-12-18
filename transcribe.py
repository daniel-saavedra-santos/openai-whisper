from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)

# Carregar o modelo Whisper uma vez para reutilizá-lo
model = whisper.load_model("base")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "Nenhum arquivo de áudio enviado"}), 400
    
    audio_file = request.files['audio']
    audio_path = os.path.join("temp_audio", audio_file.filename)
    os.makedirs("temp_audio", exist_ok=True)
    audio_file.save(audio_path)

    # Transcrever o áudio
    result = model.transcribe(audio_path)
    transcription = result.get("text", "")

    # Limpeza do arquivo temporário
    os.remove(audio_path)

    return jsonify({"transcription": transcription})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
