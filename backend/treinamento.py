import pandas as pd
import pickle
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# 1. Carregamento dos dados (Breast Cancer - Já vem no scikit-learn, facilitando sua vida)
data = load_breast_cancer()
X = data.data
y = data.target

# Nomes das features para você usar no Frontend depois
print("Features esperadas:", data.feature_names)

# 2. Split de Dados (Treino e Teste) [cite: 25]
# O PDF pede pelo menos 100 tuplas[cite: 21], essa base tem 569.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Normalização (CRUCIAL para SVM)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Treinamento do Modelo SVM [cite: 9]
print("Treinando modelo SVM...")
svm_model = SVC(kernel='linear', C=1.0, random_state=42)
svm_model.fit(X_train_scaled, y_train)

# 5. Validação (Para colocar na sua apresentação) [cite: 31, 32]
y_pred = svm_model.predict(X_test_scaled)
print(f"Acurácia: {accuracy_score(y_test, y_pred):.4f}")
print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))

# 6. Exportação dos artefatos para a API
# Precisamos salvar o MODELO e o SCALER (para normalizar os dados que chegarem da API)
with open('modelo_svm.pkl', 'wb') as f:
    pickle.dump(svm_model, f)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("\nArquivos 'modelo_svm.pkl' e 'scaler.pkl' salvos com sucesso!")