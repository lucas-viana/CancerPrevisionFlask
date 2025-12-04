<script setup>
import { ref } from 'vue';

const currentSlide = ref(0);

const slides = [
  {
    id: 0,
    title: 'Sistema de Diagnóstico Inteligente',
    subtitle: 'Análise de Risco de Câncer de Mama com Machine Learning',
    icon: '🏥',
    content: [
      'Trabalho Final - Inteligência Artificial',
      'Implementação de SVM (Support Vector Machine)',
      'Dataset: Wisconsin Breast Cancer'
    ]
  },
  {
    id: 1,
    title: 'O Problema Resolvido',
    icon: '🎯',
    content: [
      '📊 Diagnóstico de Câncer de Mama',
      '• Segundo tipo de câncer mais comum em mulheres',
      '• Detecção precoce aumenta chances de cura em até 95%',
      '',
      '🔬 Desafio:',
      '• Classificar tumores como benignos ou malignos',
      '• Auxiliar médicos na tomada de decisão',
      '• Reduzir tempo de análise e aumentar precisão'
    ]
  },
  {
    id: 2,
    title: 'Conjunto de Dados Utilizado',
    icon: '📁',
    content: [
      '📊 Wisconsin Breast Cancer Dataset',
      '',
      '✓ 569 amostras de pacientes',
      '✓ 30 características (features) por amostra',
      '✓ Medidas extraídas de imagens digitalizadas',
      '',
      '📏 Características incluem:',
      '• Raio médio do núcleo celular',
      '• Textura (variação de escala de cinza)',
      '• Perímetro e área',
      '• Suavidade e compacidade',
      '• Concavidade e pontos côncavos',
      '• Simetria e dimensão fractal'
    ]
  },
  {
    id: 3,
    title: 'Funcionamento do Algoritmo SVM',
    icon: '🧮',
    content: [
      '🤖 Support Vector Machine (SVM)',
      '',
      '1️⃣ Princípio Básico:',
      '• Encontra o hiperplano que melhor separa as classes',
      '• Maximiza a margem entre os pontos mais próximos',
      '',
      '2️⃣ Vantagens:',
      '• Eficiente em espaços de alta dimensão (30 features)',
      '• Robusto contra overfitting',
      '• Funciona bem com dados não-lineares (kernel trick)',
      '',
      '3️⃣ Implementação:',
      '• Kernel RBF (Radial Basis Function)',
      '• Normalização dos dados',
      '• Validação cruzada para otimização'
    ]
  },
  {
    id: 4,
    title: 'Resultados Obtidos',
    icon: '📈',
    content: [
      '🎯 Métricas de Performance',
      '',
      '✅ Acurácia: ~97%',
      '• Percentual de predições corretas',
      '',
      '🎯 Precisão: ~96%',
      '• Quando prevê "Maligno", está correto em 96% dos casos',
      '',
      '🔍 Recall (Sensibilidade): ~98%',
      '• Detecta 98% dos casos realmente malignos',
      '',
      '⚖️ F1-Score: ~97%',
      '• Média harmônica entre precisão e recall',
      '',
      '💡 Resultado: Modelo altamente confiável para uso como ferramenta de apoio médico'
    ]
  },
  {
    id: 5,
    title: 'Demonstração do Sistema',
    icon: '💻',
    content: [
      '🖥️ Funcionalidades do Sistema',
      '',
      '1️⃣ Carregar Dados do Paciente',
      '• Busca um caso aleatório do dataset de teste',
      '• Exibe os 30 parâmetros medidos',
      '',
      '2️⃣ Análise em Tempo Real',
      '• Permite edição manual dos valores',
      '• Classificação instantânea via API',
      '',
      '3️⃣ Resultado Visual',
      '• Comparação: Predição vs. Diagnóstico Real',
      '• Interface intuitiva com feedback visual',
      '',
      '➡️ Vamos à demonstração prática!'
    ]
  }
];

const nextSlide = () => {
  if (currentSlide.value < slides.length - 1) {
    currentSlide.value++;
  }
};

const prevSlide = () => {
  if (currentSlide.value > 0) {
    currentSlide.value--;
  }
};

const goToSlide = (index) => {
  currentSlide.value = index;
};
</script>

<template>
  <div class="presentation-wrapper">
    <div class="slide-container">
      <transition name="slide-fade" mode="out-in">
        <div :key="currentSlide" class="slide">
          <div class="slide-header">
            <div class="slide-icon">{{ slides[currentSlide].icon }}</div>
            <h1>{{ slides[currentSlide].title }}</h1>
            <p v-if="slides[currentSlide].subtitle" class="slide-subtitle">
              {{ slides[currentSlide].subtitle }}
            </p>
          </div>

          <div class="slide-content">
            <p v-for="(line, index) in slides[currentSlide].content" :key="index" class="content-line">
              {{ line }}
            </p>
          </div>

          <div class="slide-footer">
            <div class="slide-counter">
              {{ currentSlide + 1 }} / {{ slides.length }}
            </div>
          </div>
        </div>
      </transition>
    </div>

    <div class="navigation">
      <button
        @click="prevSlide"
        :disabled="currentSlide === 0"
        class="nav-btn"
      >
        ← Anterior
      </button>

      <div class="dots">
        <button
          v-for="(slide, index) in slides"
          :key="index"
          @click="goToSlide(index)"
          :class="['dot', { active: currentSlide === index }]"
          :aria-label="`Ir para slide ${index + 1}`"
        />
      </div>

      <button
        @click="nextSlide"
        :disabled="currentSlide === slides.length - 1"
        class="nav-btn"
      >
        Próximo →
      </button>
    </div>

    <div class="exit-presentation">
      <slot name="exit-button"></slot>
    </div>
  </div>
</template>

<style scoped>
.presentation-wrapper {
  min-height: 100vh;
  background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  position: relative;
}

.slide-container {
  width: 100%;
  max-width: 1200px;
  min-height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.slide {
  background: white;
  border-radius: 20px;
  padding: 3rem;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  width: 100%;
  min-height: 500px;
  display: flex;
  flex-direction: column;
}

.slide-header {
  text-align: center;
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 3px solid #f0f0f0;
}

.slide-icon {
  font-size: 5rem;
  margin-bottom: 1rem;
}

.slide-header h1 {
  color: #2d3748;
  font-size: 2.5rem;
  margin: 0 0 0.5rem 0;
  font-weight: 700;
}

.slide-subtitle {
  color: #718096;
  font-size: 1.3rem;
  margin: 0;
  font-weight: 500;
}

.slide-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.5rem;
}

.content-line {
  color: #4a5568;
  font-size: 1.3rem;
  line-height: 1.8;
  margin: 0.3rem 0;
  font-weight: 400;
}

.content-line:empty {
  height: 0.5rem;
}

.slide-footer {
  text-align: center;
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 2px solid #f0f0f0;
}

.slide-counter {
  color: #718096;
  font-size: 1.1rem;
  font-weight: 600;
}

.navigation {
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-top: 2rem;
}

.nav-btn {
  background: white;
  color: #2d3748;
  border: none;
  padding: 1rem 2rem;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.nav-btn:hover:not(:disabled) {
  background: #f7fafc;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.nav-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.dots {
  display: flex;
  gap: 0.8rem;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.4);
  border: 2px solid white;
  cursor: pointer;
  transition: all 0.3s ease;
  padding: 0;
}

.dot:hover {
  background: rgba(255, 255, 255, 0.7);
  transform: scale(1.2);
}

.dot.active {
  background: white;
  transform: scale(1.3);
}

.exit-presentation {
  margin: 1% auto;
  position: relative;
  top: 2rem;
}

.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.3s ease;
}

.slide-fade-enter-from {
  opacity: 0;
  transform: translateX(30px);
}

.slide-fade-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}

@media (max-width: 768px) {
  .presentation-wrapper {
    padding: 1rem;
  }

  .slide {
    padding: 2rem 1.5rem;
    min-height: 400px;
  }

  .slide-icon {
    font-size: 3rem;
  }

  .slide-header h1 {
    font-size: 1.8rem;
  }

  .slide-subtitle {
    font-size: 1rem;
  }

  .content-line {
    font-size: 1rem;
  }

  .navigation {
    flex-direction: column;
    gap: 1rem;
  }

  .nav-btn {
    width: 100%;
    padding: 0.8rem 1.5rem;
  }

  .exit-presentation {
    position: static;
    margin-top: 1rem;
  }
}

@media (max-width: 480px) {
  .slide-header h1 {
    font-size: 1.5rem;
  }

  .content-line {
    font-size: 0.9rem;
  }
}
</style>
