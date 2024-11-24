# Book-Looker

## Descrição do Projeto

### Resumo:
O projeto **Book-Looker** visa desenvolver um sistema de monitoramento e previsão de preços de livros. O sistema irá coletar dados de preços de livros específicos, realizar monitoramento diário e prever preços futuros com base em dados históricos. A aplicação ajudará os usuários a identificar oportunidades de compra com descontos significativos e estimulará o interesse por livros técnicos entre pessoas de classes baixas.

## Objetivos do Projeto

1. **Obter Descontos de Pelo Menos 15% em Livros**:  
   Desenvolver uma visualização de dados que permita aos usuários identificar livros com pelo menos 15% de desconto.

2. **Incentivar o Interesse por Livros Técnicos**:  
   Aumentar o interesse por livros técnicos entre pessoas de classes baixas.

## Escopo do Projeto

### Incluído:
- Desenvolvimento de modelos de machine learning para previsão de preços.
- Desenvolvimento de chatbot de recomendações
- Implementação de um scraper para coleta de preços da Amazon.
- Criação de uma interface de visualização de dados para usuários finais.

### Excluído:
- Desenvolvimento de recursos adicionais não relacionados à previsão e monitoramento de preços.

## Escolha do Modelo de Linguagem (LLM)

### Modelos Considerados:
- **Smol**: Um modelo de linguagem mais compacto e eficiente, ideal para tarefas simples e menos complexas. Embora seja eficiente em termos de custos e recursos, suas capacidades limitadas podem comprometer a qualidade das respostas em contextos mais sofisticados, como recomendações personalizadas ou análises complexas de dados históricos de preços.

- **ChatGPT-4**: Um modelo altamente sofisticado, bem conhecido por suas capacidades em conversação e entendimento geral. Embora tenha um bom desempenho em uma ampla gama de tarefas, ele pode não ser otimizado o suficiente para tarefas altamente técnicas e especializadas de previsão de preços e monitoramento de dados financeiros em tempo real, como é o caso do **Book-Looker**.

- **Gemini Pro**: A escolha ideal para o **Book-Looker**. O **Gemini Pro** se destaca pela sua capacidade avançada de entender contextos complexos e lidar com grandes volumes de dados. Ele é projetado para oferecer respostas mais precisas e detalhadas em tarefas que envolvem tanto análise de dados técnicos como interações mais sofisticadas, como a recomendação de livros com base em padrões de preços e interesses. Além disso, o **Gemini Pro** tem uma melhor capacidade de adaptação a cenários dinâmicos, como a previsão de preços de livros, onde a precisão e a velocidade de adaptação são cruciais.

### Justificativa para a Escolha do Gemini Pro:
1. **Desempenho em Contextos Técnicos**: O **Gemini Pro** tem um foco em proporcionar resultados de alta qualidade para tarefas que envolvem tanto análise de dados como geração de conteúdo técnico, como recomendações baseadas em preço e tendências de mercado.

2. **Capacidade de Personalização**: O modelo permite uma personalização mais profunda das respostas, algo essencial para fornecer recomendações de livros altamente específicas e contextualmente relevantes, alinhadas ao histórico de preços dos usuários e às flutuações de mercado.

3. **Escalabilidade e Performance**: Em um sistema que precisa lidar com um grande volume de dados e fornecer respostas baratas, como o **Book-Looker**, o **Gemini Pro** oferece melhor desempenho em termos de escalabilidade, latência, e preço.

### Conclusão:
A escolha do **Gemini Pro** para o projeto **Book-Looker** garante não apenas uma interação mais precisa e relevante, mas também suporta a complexidade do projeto, como a  recomendação de livros. Sua capacidade de lidar com tarefas técnicas avançadas e adaptar-se rapidamente a novos dados faz dele a melhor escolha em relação ao **Smol** e ao **ChatGPT-4**, que, apesar de suas qualidades, não oferecem a mesma profundidade para esse tipo de aplicação.

## Stakeholders do Projeto

- **Patrocinador**: Infnet
- **Gerente do Projeto**: Eu
- **Equipe de Desenvolvimento**: Eu
- **Usuários Finais**: Pessoas interessadas em livros técnicos (Eu)

## Riscos Principais

- **Dependência de Dados**: Falta de dados de qualidade pode comprometer a precisão das previsões.
- **Aceitação do Cliente**: Risco de baixa adoção das recomendações ou falta de percepção de valor.
