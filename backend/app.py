from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import numpy as np
import random
import os
from sklearn.datasets import load_breast_cancer

app = Flask(__name__, static_folder='dist', static_url_path='')
CORS(app)

# --- CARREGAMENTO DO MODELO ---
try:
    with open('modelo_svm.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    print("Modelo carregado com sucesso!")
except FileNotFoundError:
    print("AVISO: Execute 'python treinamento.py' primeiro!")
    model = None
    scaler = None

# Carrega dados brutos para o botão "Exemplo Aleatório"
data_raw = load_breast_cancer()

# --- ROTAS DA API ---
@app.route('/api/get-sample', methods=['GET'])
def get_sample():
    """Retorna um paciente aleatório do banco de dados"""
    idx = random.randint(0, len(data_raw.data) - 1)
    return jsonify({
        'features': data_raw.data[idx].tolist(),
        'real_class': "Maligno" if data_raw.target[idx] == 0 else "Benigno",
        'feature_names': data_raw.feature_names.tolist()
    })

@app.route('/api/predict', methods=['POST'])
def predict():
    """Recebe os dados e classifica"""
    if not model: return jsonify({'sucesso': False, 'erro': 'Modelo não encontrado'})
    
    try:
        dados = request.get_json()
        features = np.array([dados['features']])
        
        # Normaliza e prevê
        features_scaled = scaler.transform(features)
        pred = model.predict(features_scaled)
        
        return jsonify({
            'sucesso': True,
            'mensagem': "Maligno" if pred[0] == 0 else "Benigno"
        })
    except Exception as e:
        return jsonify({'sucesso': False, 'erro': str(e)})

# --- SERVIR O FRONTEND ---
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)