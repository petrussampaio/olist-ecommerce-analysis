# 🛒 Brazilian E-Commerce Analysis — Olist Dataset

> Análise end-to-end de **100 mil pedidos reais** do maior marketplace B2B do Brasil,  
> cobrindo todo o ciclo: ingestão → limpeza → EDA → segmentação ML → dashboard BI.

---

## 📌 Principais Insights

| # | Insight | Impacto |
|---|---------|---------|
| 📈 | Receita cresceu **+320%** entre jan/2017 e ago/2018 | Crescimento acelerado e consistente |
| 🚚 | Atrasos na entrega reduzem a nota média em **1,8 pontos** | Logística é o maior driver de satisfação |
| 🗺️ | **SP concentra 42%** da receita; Norte tem maior ticket médio | Oportunidade de expansão regional |
| 👥 | K-Means identificou **4 segmentos** distintos de clientes | Base para estratégias de CRM personalizadas |
| 🛍️ | Cama/mesa/banho e informática lideram em receita | Categorias prioritárias para marketing |
| ⏰ | Pico de compras às **14–16h** em dias úteis | Ideal para envio de e-mails/notificações |

---

## 🗂️ Estrutura do Projeto

```
olist-ecommerce-analysis/
│
├── data/
│   ├── raw/                    ← CSVs originais do Kaggle (não versionados)
│   └── processed/              ← Dados tratados e figuras exportadas
│
├── notebooks/
│   ├── 01_eda.ipynb            ← Análise Exploratória (EDA) completa
│   ├── 02_rfm_segmentacao.ipynb ← Segmentação RFM + K-Means
│   └── 03_geo_analise.ipynb    ← Mapas interativos com Folium
│
├── src/
│   ├── load_data.py            ← ETL e merge das 9 tabelas
│   └── download_data.py        ← Download automático via Kaggle API
│
├── dashboard/
│   └── olist_dashboard.pbix    ← Dashboard Power BI
│
├── requirements.txt
└── README.md
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10+
- Power BI Desktop (para o dashboard)
- Conta no [Kaggle](https://www.kaggle.com) (gratuita)

### 1. Clone o repositório

```bash
git clone https://github.com/<seu-usuario>/olist-ecommerce-analysis.git
cd olist-ecommerce-analysis
```

### 2. Crie o ambiente virtual e instale dependências

```bash
python -m venv .venv

# Linux/Mac
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

### 3. Configure as credenciais do Kaggle

1. Acesse [kaggle.com/settings](https://www.kaggle.com/settings) → **API** → **Create New Token**
2. Mova o arquivo `kaggle.json` para:
   - **Linux/Mac:** `~/.kaggle/kaggle.json`
   - **Windows:** `C:\Users\<usuario>\.kaggle\kaggle.json`

### 4. Baixe os dados

```bash
python src/download_data.py
```

### 5. Execute os notebooks em ordem

```bash
jupyter notebook
```

Abra e execute célula a célula:

1. `notebooks/01_eda.ipynb` — EDA + exporta CSVs para Power BI
2. `notebooks/02_rfm_segmentacao.ipynb` — Segmentação de clientes
3. `notebooks/03_geo_analise.ipynb` — Mapas interativos

### 6. Abra o dashboard no Power BI

1. Abra `dashboard/olist_dashboard.pbix`
2. Clique em **Transformar Dados → Editar Parâmetros** e aponte para a pasta `data/processed/`
3. Clique em **Atualizar**

---

## 🛠️ Stack Tecnológica

| Ferramenta | Uso |
|---|---|
| **Python 3.11** | Linguagem principal |
| **Pandas / NumPy** | Manipulação e limpeza de dados |
| **Matplotlib / Seaborn** | Visualizações estáticas |
| **Folium** | Mapas interativos |
| **Scikit-learn** | K-Means, StandardScaler, Silhouette |
| **Power BI** | Dashboard executivo |

---

## 📊 Dataset

**[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)**  
Licença: CC BY-NC-SA 4.0

| Tabela | Registros | Descrição |
|---|---|---|
| orders | 99.441 | Pedidos e status |
| order_items | 112.650 | Itens por pedido |
| payments | 103.886 | Forma e valor de pagamento |
| reviews | 99.224 | Avaliações dos clientes |
| customers | 99.441 | Dados dos compradores |
| products | 32.951 | Catálogo de produtos |
| sellers | 3.095 | Dados dos vendedores |
| geolocation | 1.000.163 | CEPs e coordenadas |

---

## 👤 Autor

**[Petrus Sampaio]**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/petrus-sampaio-6b3b8924a/)
[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/petrussampaio)

---

*Projeto desenvolvido para portfólio de Análise de Dados.*
