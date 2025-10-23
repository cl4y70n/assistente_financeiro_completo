# 💰 Assistente Financeiro Inteligente (RAG + LangChain + Automação)

## 🧠 Visão Geral

O **Assistente Financeiro Inteligente** é um sistema de análise e previsão financeira automatizado que utiliza **LangChain**, **Hugging Face** e **Google Sheets API** para ajudar pessoas e empresas a compreenderem melhor suas finanças.

Ele analisa receitas e despesas, gera relatórios automáticos, prevê fluxo de caixa e dispara alertas em casos de despesas anormais — tudo isso de forma leve e personalizável.

---

## 🚀 Principais Funcionalidades

✅ **Análise Automática de Finanças**
- Classifica receitas e despesas automaticamente.
- Gera um resumo financeiro em tempo real.

📈 **Previsão de Fluxo de Caixa**
- Usa regressão linear (Machine Learning) para prever ganhos e gastos dos próximos 30 dias.

⚠️ **Alertas Inteligentes**
- Detecta despesas anormais (como contas muito altas) e exibe notificações automáticas.

📊 **Integração com Planilhas**
- Permite importar e analisar arquivos CSV exportados do Google Sheets.

📦 **Dashboard Interativo**
- Interface amigável e leve construída com **Streamlit**.
- Mostra gráficos e estatísticas em tempo real.

---

## 🧩 Tecnologias Utilizadas

| Tecnologia | Função |
|-------------|--------|
| **Python 3.10+** | Linguagem principal do projeto |
| **LangChain** | Gerenciamento de fluxos de linguagem e automação |
| **Hugging Face Transformers** | Modelos de linguagem e NLP |
| **Google Sheets API** | Integração com planilhas |
| **Streamlit** | Interface web leve e interativa |
| **Scikit-learn** | Modelagem preditiva (regressão linear) |
| **Pandas / NumPy** | Manipulação e análise de dados |
| **Matplotlib** | Visualização de gráficos |

---

## 🧱 Estrutura do Projeto

```

assistente_financeiro_completo/
│
├── data/
│   └── exemplo.csv                # Planilha exemplo para teste
│
├── src/
│   ├── dashboard/
│   │   └── app.py                 # Interface principal do projeto (Streamlit)
│   │
│   └── utils/
│       ├── data_loader.py         # Função para carregar dados
│       ├── analysis.py            # Funções de análise e previsão
│       └── alerts.py              # Sistema de alertas automáticos
│
├── requirements.txt               # Dependências do projeto
└── README.md                      # Documentação completa

````

---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/assistente-financeiro-inteligente.git
cd assistente-financeiro-inteligente
````

### 2️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Executar o dashboard

```bash
streamlit run src/dashboard/app.py
```

Acesse no navegador:
👉 `http://localhost:8501`

---

## 📂 Exemplo de Planilha (CSV)

Você pode criar um arquivo com o formato abaixo:

```csv
Data,Tipo,Valor,Descrição
2025-01-01,Receita,5000,Salário
2025-01-05,Despesa,1200,Aluguel
2025-01-10,Despesa,300,Internet
2025-01-15,Receita,800,Freelancer
2025-01-20,Despesa,150,Transporte
2025-01-25,Despesa,200,Alimentação
```

---

## 🧮 Como Funciona o Modelo Preditivo

O sistema utiliza **regressão linear** (via `scikit-learn`) para analisar o comportamento histórico de valores financeiros e prever os próximos 30 dias de fluxo de caixa.
Essa abordagem é leve, interpretável e ideal para aplicações simples de previsão financeira.

---

## 🔗 Integração com Google Sheets (Opcional)

Se desejar, você pode integrar o projeto com o **Google Sheets API** para importar dados automaticamente.

Etapas:

1. Crie um projeto no [Google Cloud Console](https://console.cloud.google.com/).
2. Ative a API do Google Sheets.
3. Gere um arquivo `credentials.json`.
4. Adicione-o na pasta raiz do projeto.
5. No `data_loader.py`, ajuste para ler diretamente da planilha usando `gspread`.

---

## 🧰 Recursos Avançados (opcionais)

* 🔍 **LangChain Agents**: podem ser usados para criar agentes financeiros que respondem perguntas sobre seus gastos.
* 💬 **Modelos Hugging Face**: podem interpretar descrições e categorizar despesas automaticamente.
* 🤖 **Automação Corporativa**: integração com Slack/Telegram para alertas automáticos de finanças.

---

## 🖼️ Sugestão de Prints para o README

* 📸 Tela principal do Streamlit com gráfico de fluxo de caixa.
* 📸 Exemplo de alerta de despesa alta.
* 📸 Tabela com resumo de receitas e despesas.

---

## 📚 Roadmap de Melhorias Futuras

* [ ] Integração total com Google Sheets API
* [ ] Adição de categorização automática via NLP (Hugging Face)
* [ ] Exportação de relatórios PDF
* [ ] Notificações automáticas via Telegram
* [ ] Painel corporativo com múltiplos usuários

---

## 🪪 Licença

Este projeto está sob a licença **MIT** — sinta-se livre para usar, modificar e distribuir.

---

## ⭐ Contribuição

Contribuições são bem-vindas!
Se quiser melhorar o projeto, faça um **fork**, crie uma **branch**, implemente suas mudanças e envie um **pull request**.

```bash
git checkout -b minha-feature
git commit -m "Adicionei nova funcionalidade X"
git push origin minha-feature
```

---

