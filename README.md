# Sistema de Diagnóstico Inteligente

Análise de Risco de Câncer de Mama com Machine Learning (SVM)

## 🎯 Sobre o Projeto

Sistema desenvolvido para auxiliar no diagnóstico de câncer de mama utilizando Support Vector Machine (SVM). O projeto inclui:
- Backend Flask com modelo SVM treinado
- Frontend Vue.js responsivo
- Apresentação de slides integrada para aulas
- Dashboard interativo para análise

## 📊 Dataset

- **Wisconsin Breast Cancer Dataset**
- 569 amostras de pacientes
- 30 características por amostra
- Classificação: Benigno ou Maligno

## 🚀 Tecnologias

### Backend
- Python 3.11
- Flask
- scikit-learn
- NumPy, Pandas

### Frontend
- Vue.js 3
- Vite
- Axios

## 💻 Executar Localmente

### Backend
```bash
cd backend
pip install -r requirements.txt
python treinamento.py  # Treinar o modelo
python app.py          # Iniciar API
```

### Frontend (Desenvolvimento)
```bash
cd frontend
npm install
npm run dev
```

### Deploy Unificado (Produção)
```powershell
.\build-frontend.ps1  # Compila e copia frontend para backend
cd backend
python app.py         # Serve API + Frontend
```

## 📈 Métricas do Modelo

- **Acurácia**: ~97%
- **Precisão**: ~96%
- **Recall**: ~98%
- **F1-Score**: ~97%

## 🔧 Deploy na Azure

### Pré-requisitos
1. Conta Azure
2. Azure CLI instalado
3. Repositório GitHub

### Opção 1: Deploy Manual
```bash
az login
az webapp up --resource-group rg-diagnostico --name app-diagnostico-ia --runtime "PYTHON:3.11"
```

### Opção 2: GitHub Actions (Automático)
1. Configure os secrets no GitHub:
   - `AZURE_WEBAPP_NAME`
   - `AZURE_WEBAPP_PUBLISH_PROFILE`
2. Push para branch `main`
3. Deploy automático via GitHub Actions

## 📝 Estrutura do Projeto

```
.
├── backend/
│   ├── app.py              # API Flask + Servidor estático
│   ├── treinamento.py      # Treina modelo SVM
│   ├── requirements.txt    # Dependências Python
│   └── dist/               # Frontend compilado (gerado)
├── frontend/
│   ├── src/
│   │   ├── App.vue         # Componente principal
│   │   └── components/
│   │       └── PresentationSlides.vue  # Slides da apresentação
│   └── package.json
├── build-frontend.ps1      # Script de build
└── .gitignore
```

## 🎓 Apresentação

O sistema inclui slides integrados cobrindo:
1. Introdução ao projeto
2. O problema resolvido
3. Dataset utilizado
4. Funcionamento do SVM
5. Resultados obtidos
6. Demonstração ao vivo

## 📄 Licença

Projeto acadêmico - Inteligência Artificial
