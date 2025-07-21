# Credit Card Fraud Detection - Exploratory Data Analysis (EDA)

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A comprehensive Exploratory Data Analysis (EDA) project for Credit Card Fraud Detection using Python, Pandas, Matplotlib, Seaborn, and Scikit-learn.

## 🎯 Project Overview

This project provides an in-depth analysis of credit card fraud detection data, featuring:

- **Advanced Statistical Analysis**: Comprehensive statistical tests and hypothesis testing
- **Temporal Pattern Analysis**: Time-based fraud detection patterns
- **Feature Engineering**: PCA component analysis and feature importance ranking
- **Clustering Analysis**: K-means clustering for transaction patterns
- **Dimensionality Reduction**: PCA and t-SNE visualizations
- **Business Insights**: Actionable recommendations for fraud detection systems

## 📊 Key Features

### 🔍 **Analysis Components**

1. **Class Distribution Analysis**: Detailed fraud vs normal transaction statistics
2. **Temporal Pattern Analysis**: Time-based fraud detection patterns
3. **Amount Pattern Deep Dive**: Transaction amount analysis by fraud class
4. **PCA Feature Analysis**: Analysis of V1-V28 anonymized features
5. **Statistical Testing**: Hypothesis testing for fraud detection
6. **Clustering Analysis**: K-means clustering for pattern detection
7. **Dimensionality Reduction**: PCA and t-SNE visualizations
8. **Advanced Pattern Detection**: Sequential fraud patterns and combinations
9. **Comprehensive Insights**: Business recommendations and modeling suggestions

### 📈 **Visualizations**

- Transaction volume analysis by time
- Fraud rate temporal patterns
- Amount distribution comparisons
- Feature correlation heatmaps
- Clustering visualizations
- Dimensionality reduction plots

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **Scikit-learn**: Machine learning and preprocessing
- **SciPy**: Statistical functions
- **Jupyter Notebook**: Interactive analysis

## 📁 Project Structure

```
credit-card-fraud-detection-eda/
│
├── main.py                    # Comprehensive EDA script
├── EDA.IPYNB                  # Jupyter notebook for interactive analysis
├── create_test_data.py        # Generate realistic test dataset
├── requirements.txt           # Python dependencies
├── creditcard.csv            # Dataset (generated or original)
└── README.md                 # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rahulbedjavalge/credit-card-fraud-detection-eda.git
   cd credit-card-fraud-detection-eda
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate test dataset** (if you don't have the original)
   ```bash
   python create_test_data.py
   ```

5. **Run the analysis**
   ```bash
   python main.py
   ```

### Alternative: Jupyter Notebook

```bash
jupyter notebook EDA.IPYNB
```

## 📊 Dataset Information

### Original Dataset
The project is designed to work with the **Credit Card Fraud Detection** dataset from Kaggle, which contains:
- **284,807 transactions**
- **31 features** (Time, Amount, V1-V28, Class)
- **0.17% fraud rate** (highly imbalanced)
- **PCA-transformed features** (V1-V28) for privacy

### Test Dataset
If you don't have access to the original dataset, run `create_test_data.py` to generate a realistic synthetic dataset with:
- **50,000 transactions**
- **Same structure** as original
- **Realistic fraud patterns**
- **Statistical properties** similar to real data

## 🎯 Key Insights

### 📈 **Fraud Characteristics**
- Extremely low fraud rate (~0.17%)
- Fraud transactions have different amount distributions
- Temporal patterns exist but are subtle
- PCA features contain most discriminative information

### 🕐 **Temporal Patterns**
- Fraud rates vary by hour of day
- Sequential fraud patterns detectable
- Time-based features provide additional insights

### 💰 **Financial Impact**
- Fraud amounts vs normal transaction analysis
- Risk assessment by transaction amount ranges
- Cost-benefit analysis for detection systems

### 🎯 **Modeling Recommendations**
- Use stratified sampling for training
- Focus on precision metrics for fraud class
- Implement cost-sensitive learning
- Consider ensemble methods
- Use cross-validation with temporal awareness

## 📋 Requirements

```txt
certifi==2025.7.14
charset-normalizer==3.4.2
contourpy==1.3.2
cycler==0.12.1
fonttools==4.59.0
kiwisolver==1.4.8
matplotlib==3.10.3
numpy==2.3.1
packaging==25.0
pandas==2.3.1
pillow==11.3.0
pyparsing==3.2.3
python-dateutil==2.9.0.post0
pytz==2025.2
scipy==1.16.0
seaborn==0.13.2
scikit-learn==1.6.1
six==1.17.0
tzdata==2025.2
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Rahul Bedjavalge**
- GitHub: [@rahulbedjavalge](https://github.com/rahulbedjavalge)
- Location: Berlin

## 🙏 Acknowledgments

- Credit Card Fraud Detection dataset from Kaggle
- Open source community for amazing libraries
- Python data science ecosystem

## 📞 Support

If you have any questions or run into issues, please open an issue on GitHub.

---

**⭐ Star this repository if you find it helpful!**