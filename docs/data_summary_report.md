# Data Summary Report

## 1. Fontes de Dados Utilizadas

### 1.1. Fonte de Dados: Amazon
- **Tipo de Dados**:
  - Preços de livros (dados históricos e atuais) em valores inteiros.
  - Links dos livros.
  - Data da coleta.
- **Objetivo de Uso**:
  - Coletar dados de preços para análise e previsão.
  - Monitorar variações de preços ao longo do tempo para identificar padrões e oportunidades de desconto.

### 1.2. Fonte de Dados: APIs de Preços de Livros (se disponível)
- **Tipo de Dados**:
  - Informações adicionais sobre o livro (autor, título, ISBN, edição, etc.).
- **Objetivo de Uso**:
  - Obter informações detalhadas sobre os livros para complementar a análise de preços e melhorar a precisão das previsões e recomendações.

## 2. Objetivos do Uso dos Dados

1. **Previsão de Preços**:  
   Utilizar dados históricos e atuais para treinar modelos de machine learning que preverão futuros preços de livros, ajudando os usuários a identificar tendências de preços e possíveis oportunidades de desconto.

2. **Monitoramento de Preços**:  
   Acompanhar as variações de preços em tempo real para identificar quando os livros estão mais baratos e notificar os usuários sobre oportunidades de compra com desconto.

3. **Visualização de Dados**:  
   Criar dashboards e gráficos interativos que ajudem os usuários a visualizar tendências de preços ao longo do tempo e identificar os melhores momentos para comprar livros com desconto.

4. **Recomendação com LLMS**:  
   Criar um chat para realizar a recomendação de livros com base nas mensagens do usuário.