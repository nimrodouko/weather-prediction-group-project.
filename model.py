{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP1L6Gp0676DP4YthNf0BWj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/nimrodouko/weather-prediction-group-project./blob/main/model.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 43,
      "metadata": {
        "id": "-fH0XQ-Sp-Gi"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "from imblearn.over_sampling import SMOTE\n",
        "\n",
        "data  = pd.read_csv(\"weather_train.csv\")\n",
        "def classify_temprature(temp):\n",
        "  if temp < 17:\n",
        "    return \"cold\"\n",
        "  else:\n",
        "    return \"hot\"\n",
        "\n",
        "# Apply the function to the temperature column\n",
        "data['temprature'] = data['temprature'].apply(classify_temprature)\n",
        "from sklearn.model_selection import train_test_split\n",
        "from imblearn.over_sampling import RandomOverSampler\n",
        "\n",
        "# Split the data into training and test sets, stratifying the target variable\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
        "from sklearn.naive_bayes import GaussianNB\n",
        "model = GaussianNB()\n",
        "\n",
        "# Train the model on the training data\n",
        "model.fit(X_train, y_train)\n",
        "y_pred = model.predict(X_test)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import classification_report\n",
        "\n",
        "\n",
        "print(classification_report(y_test, y_pred))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MoF8ro3U5nYG",
        "outputId": "4a67fba9-5eb4-415b-da6f-1269abd6beaa"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "      cloudy       0.44      0.80      0.57         5\n",
            "       rainy       0.60      0.60      0.60         5\n",
            "       snowy       1.00      1.00      1.00         2\n",
            "       sunny       1.00      0.50      0.67         8\n",
            "\n",
            "    accuracy                           0.65        20\n",
            "   macro avg       0.76      0.72      0.71        20\n",
            "weighted avg       0.76      0.65      0.66        20\n",
            "\n"
          ]
        }
      ]
    }
  ]
}