<script setup>
import { ref } from 'vue';
import axios from 'axios';
import PresentationSlides from './components/PresentationSlides.vue';

const features = ref([]);
const names = ref([]);
const result = ref(null);
const realLabel = ref(null);
const loading = ref(false);
const showData = ref(false);
const showPresentation = ref(true);

const API = '/api';

const startDemo = () => {
  showPresentation.value = false;
};

const carregarExemplo = async () => {
  loading.value = true;
  result.value = null;
  showData.value = false;
  try {
    const res = await axios.get(`${API}/get-sample`);
    features.value = res.data.features;
    names.value = res.data.feature_names;
    realLabel.value = res.data.real_class;
    showData.value = true;
  } catch (e) {
    alert("Erro ao conectar na API. O backend está rodando?");
  }
  loading.value = false;
};

const classificar = async () => {
  loading.value = true;
  try {
    const res = await axios.post(`${API}/predict`, { features: features.value });
    if (res.data.sucesso) result.value = res.data.mensagem;
  } catch (e) {
    alert("Erro na previsão.");
  }
  loading.value = false;
};
</script>

<template>
  <div v-if="showPresentation">
    <PresentationSlides>
      <template #exit-button>
        <button @click="startDemo" class="demo-btn">
          🚀 Ir para Demonstração
        </button>
      </template>
    </PresentationSlides>
  </div>

  <div v-else class="app-wrapper">
    <div class="header">
      <div class="header-content">
        <div class="icon-wrapper">
          <span class="icon">🏥</span>
        </div>
        <div>
          <h1>Sistema de Diagnóstico Inteligente</h1>
          <p class="subtitle">Análise de Risco de Câncer de Mama com Machine Learning (SVM)</p>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="welcome-card" v-if="!showData && !result">
        <div class="welcome-icon">🔬</div>
        <h2>Bem-vindo ao Sistema de Diagnóstico</h2>
        <p>Este sistema utiliza Machine Learning para auxiliar na análise de risco de câncer de mama.</p>
        <p class="info-text">Clique no botão abaixo para carregar dados de um paciente e iniciar a análise.</p>
      </div>

      <div class="actions">
        <button @click="carregarExemplo" :disabled="loading" class="btn btn-load">
          <span class="btn-icon">📂</span>
          <span>{{ loading ? 'Carregando...' : 'Carregar Dados do Paciente' }}</span>
        </button>
        <button
          @click="classificar"
          :disabled="features.length === 0 || loading"
          class="btn btn-analyze"
        >
          <span class="btn-icon">🔍</span>
          <span>{{ loading ? 'Analisando...' : 'Analisar Risco' }}</span>
        </button>
      </div>

      <transition name="slide-fade">
        <div v-if="result" class="result-card">
          <div :class="['result-header', result === 'Maligno' ? 'danger' : 'success']">
            <span class="result-icon">{{ result === 'Maligno' ? '⚠️' : '✅' }}</span>
            <div>
              <h2>Resultado da Análise</h2>
              <p class="result-status">{{ result }}</p>
            </div>
          </div>
          <div class="result-body">
            <div class="info-row">
              <span class="label">Diagnóstico Real (Histórico):</span>
              <span class="value">{{ realLabel }}</span>
            </div>
            <div class="accuracy-note">
              <span class="note-icon">ℹ️</span>
              <span>Este resultado é gerado por um modelo de Machine Learning e deve ser utilizado apenas como ferramenta de apoio.</span>
            </div>
          </div>
        </div>
      </transition>

      <transition name="slide-fade">
        <div v-if="showData && features.length > 0" class="data-section">
          <div class="section-header">
            <h3>📊 Dados do Paciente</h3>
            <p>Você pode ajustar os valores abaixo antes de realizar a análise</p>
          </div>

          <div class="features-grid">
            <div v-for="(val, i) in features" :key="i" class="feature-card">
              <label class="feature-label">{{ names[i] }}</label>
              <input
                type="number"
                v-model.number="features[i]"
                step="0.01"
                class="feature-input"
              >
            </div>
          </div>
        </div>
      </transition>
    </div>

    <div class="back-to-presentation">
      <button @click="showPresentation = true" class="btn-back">
        📊 Voltar para Apresentação
      </button>
    </div>
  </div>
</template>

<style scoped>
* {
  box-sizing: border-box;
}

.app-wrapper {
  min-height: 100vh;
  width: 100%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 0;
  margin: 0;
}

.header {
  background: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 2rem 0;
  margin-bottom: 2rem;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.icon-wrapper {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 1rem;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.icon {
  font-size: 3rem;
  display: block;
}

.header h1 {
  margin: 0;
  font-size: 2rem;
  color: #2d3748;
  font-weight: 700;
}

.subtitle {
  margin: 0.5rem 0 0 0;
  color: #718096;
  font-size: 1rem;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem 2rem 2rem;
}

.welcome-card {
  background: white;
  border-radius: 15px;
  padding: 3rem;
  text-align: center;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.welcome-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.welcome-card h2 {
  color: #2d3748;
  margin-bottom: 1rem;
  font-size: 1.8rem;
}

.welcome-card p {
  color: #718096;
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 0.5rem;
}

.info-text {
  color: #4a5568;
  font-weight: 500;
}

.actions {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 1rem 2rem;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-load {
  background: white;
  color: #667eea;
  border: 2px solid #667eea;
}

.btn-analyze {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn-icon {
  font-size: 1.2rem;
}

.result-card {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.result-header {
  padding: 2rem;
  color: white;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.result-header.success {
  background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
}

.result-header.danger {
  background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
}

.result-icon {
  font-size: 3rem;
}

.result-header h2 {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 500;
  opacity: 0.9;
}

.result-status {
  margin: 0.5rem 0 0 0;
  font-size: 2rem;
  font-weight: 700;
}

.result-body {
  padding: 2rem;
}

.info-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background: #f7fafc;
  border-radius: 8px;
  margin-bottom: 1rem;
}

.label {
  color: #4a5568;
  font-weight: 500;
}

.value {
  color: #2d3748;
  font-weight: 700;
  font-size: 1.1rem;
}

.accuracy-note {
  display: flex;
  gap: 0.75rem;
  padding: 1rem;
  background: #edf2f7;
  border-left: 4px solid #667eea;
  border-radius: 4px;
  color: #4a5568;
  font-size: 0.9rem;
  line-height: 1.5;
}

.note-icon {
  font-size: 1.2rem;
}

.data-section {
  background: white;
  border-radius: 15px;
  padding: 2rem;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
}

.section-header {
  margin-bottom: 2rem;
  text-align: center;
}

.section-header h3 {
  color: #2d3748;
  font-size: 1.5rem;
  margin: 0 0 0.5rem 0;
}

.section-header p {
  color: #718096;
  margin: 0;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

.feature-card {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.feature-label {
  color: #4a5568;
  font-weight: 500;
  font-size: 0.9rem;
}

.feature-input {
  padding: 0.75rem;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.feature-input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.3s ease-in;
}

.slide-fade-enter-from {
  transform: translateY(20px);
  opacity: 0;
}

.slide-fade-leave-to {
  transform: translateY(-20px);
  opacity: 0;
}

@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    text-align: center;
  }

  .header h1 {
    font-size: 1.5rem;
  }

  .actions {
    flex-direction: column;
  }

  .btn {
    width: 100%;
    justify-content: center;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }
}

.demo-btn {
  background: white;
  margin: 0 auto;
  color: #1e3c72;
  border: 2px solid white;
  padding: 1rem 2rem;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.demo-btn:hover {
  background: #f0f0f0;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
}

.back-to-presentation {
  text-align: center;
  padding: 2rem 0;
}

.btn-back {
  background: white;
  color: #667eea;
  border: 2px solid #667eea;
  padding: 1rem 2rem;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.btn-back:hover {
  background: #667eea;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}
</style>
