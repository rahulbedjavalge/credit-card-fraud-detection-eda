"""
Create realistic test data for Credit Card Fraud Detection
"""
import pandas as pd
import numpy as np

def create_creditcard_dataset(n_samples=50000):
    """Create realistic credit card fraud dataset for testing"""
    
    print(f"Creating sample dataset with {n_samples:,} transactions...")
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Create realistic fraud rate (0.17% like real dataset)
    fraud_rate = 0.0017
    n_fraud = int(n_samples * fraud_rate)
    n_normal = n_samples - n_fraud
    
    # Generate time data (spanning 2 days)
    time_data = np.random.randint(0, 172800, n_samples)  # 2 days in seconds
    time_data = np.sort(time_data)  # Sort to make it realistic
    
    # Generate amount data with realistic distributions
    # Normal transactions: smaller amounts, log-normal distribution
    normal_amounts = np.random.lognormal(mean=3.0, sigma=1.5, size=n_normal)
    normal_amounts = np.clip(normal_amounts, 0, 25000)  # Reasonable max
    
    # Fraud transactions: often smaller amounts to avoid detection
    fraud_amounts = np.random.lognormal(mean=2.5, sigma=1.2, size=n_fraud)
    fraud_amounts = np.clip(fraud_amounts, 0, 10000)  # Usually smaller
    
    # Combine amounts and create labels
    amounts = np.concatenate([normal_amounts, fraud_amounts])
    labels = np.concatenate([np.zeros(n_normal), np.ones(n_fraud)])
    
    # Shuffle to mix normal and fraud transactions
    indices = np.random.permutation(n_samples)
    time_data = time_data[indices]
    amounts = amounts[indices]
    labels = labels[indices]
    
    # Generate V1-V28 PCA features
    # Make some features more discriminative for fraud
    pca_features = {}
    
    for i in range(1, 29):
        if i <= 5:  # First 5 features are more discriminative
            # Normal transactions centered around 0
            normal_vals = np.random.normal(0, 1, sum(labels == 0))
            # Fraud transactions shifted
            fraud_vals = np.random.normal(2.5, 1.8, sum(labels == 1))
            
            # Combine and shuffle
            combined = np.concatenate([normal_vals, fraud_vals])
            pca_features[f'V{i}'] = combined[np.argsort(indices)]
            
        elif i <= 14:  # Next features moderately discriminative
            normal_vals = np.random.normal(0, 1, sum(labels == 0))
            fraud_vals = np.random.normal(1.0, 1.5, sum(labels == 1))
            
            combined = np.concatenate([normal_vals, fraud_vals])
            pca_features[f'V{i}'] = combined[np.argsort(indices)]
            
        else:  # Remaining features less discriminative
            pca_features[f'V{i}'] = np.random.normal(0, 1, n_samples)
    
    # Create DataFrame
    data = {
        'Time': time_data,
        'Amount': amounts,
        'Class': labels.astype(int)
    }
    
    # Add PCA features
    data.update(pca_features)
    
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('creditcard.csv', index=False)
    
    # Print statistics
    fraud_count = df['Class'].sum()
    fraud_rate_actual = fraud_count / len(df) * 100
    
    print(f"✅ Dataset created successfully!")
    print(f"📊 Statistics:")
    print(f"   • Total transactions: {len(df):,}")
    print(f"   • Normal transactions: {len(df) - fraud_count:,}")
    print(f"   • Fraud transactions: {fraud_count:,}")
    print(f"   • Fraud rate: {fraud_rate_actual:.4f}%")
    print(f"   • Features: {len(df.columns)}")
    print(f"   • File size: ~{df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
    print(f"   • Time span: {df['Time'].max() / 3600:.1f} hours")
    print(f"   • Amount range: ${df['Amount'].min():.2f} - ${df['Amount'].max():.2f}")
    
    return df

if __name__ == "__main__":
    df = create_creditcard_dataset(50000)
    print(f"\n🎉 Sample data ready! You can now run: python main.py")
