# 📊 Análise de Dados de Diabetes

Este repositório contém códigos Python para análise de dados de um conjunto de dados de diabetes. As principais funcionalidades incluem:

✅ Geração de **Boxplot** para visualizar distribuição e outliers.  
✅ Identificação de **outliers** na coluna **Age**.  
✅ Exportação do gráfico gerado como imagem.

---

## 📂 Estrutura do Projeto

```
📁 ML
│── 📜 diabetes_dataset_with_notes.csv  # Conjunto de dados de diabetes
│── 📜 python_boxplot_diabetes.py       # Código para gerar Boxplot da coluna Age
│── 📜 README.md                         # Documentação do projeto
```

---

## 🚀 Como Executar o Projeto

### 1️⃣ **Instalar dependências**
Certifique-se de ter o Python 3.x instalado e execute o comando abaixo para instalar as bibliotecas necessárias:
```bash
pip install pandas seaborn matplotlib
```

### 2️⃣ **Executar o script**
Abra o terminal na pasta do projeto e execute:
```bash
python python_boxplot_diabetes.py
```

Isso gerará um **boxplot** da coluna **age** e salvará como **boxplot_age_outliers.png**.

---

## 📌 Código Principal
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('diabetes_dataset_with_notes.csv')

# Selecionar apenas a coluna "age"
df_age = df[['age']].dropna()

# Criar o gráfico Boxplot com destaque para os outliers
plt.figure(figsize=(8, 6))
sns.boxplot(y=df_age['age'], color="skyblue", width=0.3, fliersize=8, flierprops={"marker": "o", "markerfacecolor": "red", "markeredgecolor": "black"})

# Configurações do gráfico
plt.title('Boxplot da Coluna Age (com Outliers)', fontsize=14)
plt.ylabel('Idade', fontsize=12)

# Salvar a imagem como PNG
plt.savefig("boxplot_age_outliers.png", dpi=300)

# Exibir o gráfico
plt.show()
```

---

## 🛠 Possíveis Problemas
🔹 **Arquivo não encontrado**: Certifique-se de que o arquivo `diabetes_dataset_with_notes.csv` está no mesmo diretório do script.  
🔹 **Módulo não encontrado**: Execute `pip install pandas seaborn matplotlib` antes de rodar o código.  


---

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar. 😊

