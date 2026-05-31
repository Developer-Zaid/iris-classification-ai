"""
Iris Flower Classification System

Week 2 AI Internship Project
DecodeLabs

Author: Zaid
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


def main() -> None:
    print("=" * 60)
    print("🌸 IRIS FLOWER CLASSIFICATION SYSTEM")
    print("=" * 60)

    # Load dataset
    iris = load_iris()

    X = iris.data
    y = iris.target

    print(f"\nDataset Size: {len(X)} samples")
    print(f"Features: {X.shape[1]}")
    print(f"Classes: {len(iris.target_names)}")

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        shuffle=True
    )

    print(f"\nTraining Samples: {len(X_train)}")
    print(f"Testing Samples: {len(X_test)}")

    # Feature Scaling
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # KNN Model
    model = KNeighborsClassifier(n_neighbors=5)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    # Evaluation
    accuracy = accuracy_score(y_test, predictions)

    print("\n" + "=" * 60)
    print("MODEL PERFORMANCE")
    print("=" * 60)

    print(f"\nAccuracy Score: {accuracy * 100:.2f}%")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=iris.target_names
        )
    )

if __name__ == "__main__":
    main()
