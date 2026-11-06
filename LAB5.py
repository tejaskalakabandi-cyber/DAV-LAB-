{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "sVdjLHDgY-7O"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data={\n",
        "    \"Student\":[\"A\",\"B\",\"C\",\"D\",\"E\",\"F\",\"G\",\"H\",\"I\",\"J\"],\n",
        "    \"Marks\":[50,55,60,62,65,68,70,72,75,150]\n",
        "}\n",
        "df=pd.DataFrame(data)"
      ],
      "metadata": {
        "id": "TsZETcUigZsr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Original Dataset\")\n",
        "print(df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "41uE_hJlg_Bz",
        "outputId": "31509227-81f4-4828-8ba8-f23344875553"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original Dataset\n",
            "  Student  Marks\n",
            "0       A     50\n",
            "1       B     55\n",
            "2       C     60\n",
            "3       D     62\n",
            "4       E     65\n",
            "5       F     68\n",
            "6       G     70\n",
            "7       H     72\n",
            "8       I     75\n",
            "9       J    150\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Q1=df[\"Marks\"].quantile(0.25)\n",
        "print(Q1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mlX24fKohIrs",
        "outputId": "ca5a938c-ec45-4622-aab4-0c82db091943"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "60.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Q3=df[\"Marks\"].quantile(0.75)\n",
        "print(Q3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gsmqjih0hXnJ",
        "outputId": "e907218a-d736-4200-af81-027a52221040"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "71.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "IQR=Q3-Q1\n",
        "print(IQR)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "If6V8jhqheKh",
        "outputId": "27fffec9-7723-4cbc-f6d6-ded9e355c861"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "11.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lower_limit=Q1-1.5*IQR\n",
        "upper_limit=Q3+1.5*IQR\n",
        "print(lower_limit)\n",
        "print(upper_limit)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kw1xCeKLhmVg",
        "outputId": "bbb84044-10db-4680-a78b-b5edd41d46fb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "44.0\n",
            "88.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "outliers=df[\n",
        "    (df[\"Marks\"]<lower_limit)|(df[\"Marks\"]>upper_limit)\n",
        "    ]\n",
        "print(\"\\nOutliers using IQR method\")\n",
        "print(outliers)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J4pm5P6TiEWE",
        "outputId": "cbd0a785-1bd4-484a-b575-bae0c726e26e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Outliers using IQR method\n",
            "  Student  Marks\n",
            "9       J    150\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Marks_Treated\"]=np.where(\n",
        "    df[\"Marks\"]>upper_limit,\n",
        "    upper_limit,\n",
        "    np.where(\n",
        "    df[\"Marks\"]<lower_limit,\n",
        "    lower_limit,\n",
        "    df[\"Marks\"]\n",
        "    )\n",
        "  )\n",
        "print(df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "ohY6l7I4jpPj",
        "outputId": "12a007fa-501b-4f02-a8cb-3e9e413342c3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  Student  Marks  Marks_Treated\n",
            "0       A     50           50.0\n",
            "1       B     55           55.0\n",
            "2       C     60           60.0\n",
            "3       D     62           62.0\n",
            "4       E     65           65.0\n",
            "5       F     68           68.0\n",
            "6       G     70           70.0\n",
            "7       H     72           72.0\n",
            "8       I     75           75.0\n",
            "9       J    150           88.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Capping\n",
        "df_capped=df.copy()\n",
        "df_capped[\"Marks\"]=df_capped[\"Marks\"].clip(lower=lower_limit,upper=upper_limit)\n",
        "print(df)\n",
        "print(\"\\nAfter Capping:\")\n",
        "print(df_capped)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "9owLBxp-lpkk",
        "outputId": "b5898e80-d567-42d8-9c91-77fe38b61d0e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  Student  Marks  Marks_Treated\n",
            "0       A     50           50.0\n",
            "1       B     55           55.0\n",
            "2       C     60           60.0\n",
            "3       D     62           62.0\n",
            "4       E     65           65.0\n",
            "5       F     68           68.0\n",
            "6       G     70           70.0\n",
            "7       H     72           72.0\n",
            "8       I     75           75.0\n",
            "9       J    150           88.0\n",
            "\n",
            "After Capping:\n",
            "  Student  Marks  Marks_Treated\n",
            "0       A     50           50.0\n",
            "1       B     55           55.0\n",
            "2       C     60           60.0\n",
            "3       D     62           62.0\n",
            "4       E     65           65.0\n",
            "5       F     68           68.0\n",
            "6       G     70           70.0\n",
            "7       H     72           72.0\n",
            "8       I     75           75.0\n",
            "9       J     88           88.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from scipy.stats import zscore"
      ],
      "metadata": {
        "id": "0Od6aMfllz8x"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data={\n",
        "    \"Student\":[\"A\",\"B\",\"C\",\"D\",\"E\",\"F\",\"G\",\"H\",\"I\",\"J\",\n",
        "               \"K\",\"L\",\"M\",\"N\",\"O\",\"P\",\"Q\",\"R\",\"S\",\"T\"],\n",
        "    \"Marks\":[50,52,54,55,56,58,60,61,62,63,64,65,66,68,70,71,72,73,75,200]\n",
        "}\n",
        "df=pd.DataFrame(data)"
      ],
      "metadata": {
        "id": "FGBve2dvnB2N"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Z_Score\"]=zscore(df[\"Marks\"])\n",
        "print(\"\\nZ-Scores for each value:\")\n",
        "print(df)"
      ],
      "metadata": {
        "id": "bSgqWWp_n7e_",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1101e218-ee66-40b1-a9a4-89a3eb542e63"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Z-Scores for each value:\n",
            "   Student  Marks   Z_Score\n",
            "0        A     50 -0.643187\n",
            "1        B     52 -0.578054\n",
            "2        C     54 -0.512921\n",
            "3        D     55 -0.480355\n",
            "4        E     56 -0.447788\n",
            "5        F     58 -0.382655\n",
            "6        G     60 -0.317523\n",
            "7        H     61 -0.284956\n",
            "8        I     62 -0.252390\n",
            "9        J     63 -0.219823\n",
            "10       K     64 -0.187257\n",
            "11       L     65 -0.154691\n",
            "12       M     66 -0.122124\n",
            "13       N     68 -0.056991\n",
            "14       O     70  0.008142\n",
            "15       P     71  0.040708\n",
            "16       Q     72  0.073274\n",
            "17       R     73  0.105841\n",
            "18       S     75  0.170974\n",
            "19       T    200  4.241777\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "outliers=df[abs(df[\"Z_Score\"])>3]\n",
        "print(\"\\n Outliers using Z_score:\")\n",
        "print(outliers)"
      ],
      "metadata": {
        "id": "eI2ACFuVog_o",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a1b95033-4678-4f49-a740-897c1ac36478"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            " Outliers using Z_score:\n",
            "   Student  Marks   Z_Score\n",
            "19       T    200  4.241777\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mean=df[\"Marks\"].mean()"
      ],
      "metadata": {
        "id": "LjyAbOrTpK_G"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "std=df[\"Marks\"].std(ddof=0)"
      ],
      "metadata": {
        "id": "qPwTouJTpXVB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "lower_limit=mean-(3*std)\n",
        "upper_limit=mean+(3*std)"
      ],
      "metadata": {
        "id": "0vMAZj8Gpe1H"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\nMean:\",mean)\n",
        "print(\"\\nStandard Deviation:\",std)\n",
        "print(\"\\nLower_limit:\",lower_limit)\n",
        "print(\"\\nUpper_limit:\",upper_limit)"
      ],
      "metadata": {
        "id": "lovZ3_TCpz5Y",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e9df875e-0f8a-4498-9e57-a16919c76bba"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Mean: 69.75\n",
            "\n",
            "Standard Deviation: 30.70647325890748\n",
            "\n",
            "Lower_limit: -22.369419776722438\n",
            "\n",
            "Upper_limit: 161.86941977672245\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[\"Marks_Treated\"]=df[\"Marks\"].clip(\n",
        "    lower=lower_limit,\n",
        "    upper=upper_limit\n",
        ")"
      ],
      "metadata": {
        "id": "UQsGZzwLqLyn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\nAfter Z_Score capping:\")\n",
        "print(df)"
      ],
      "metadata": {
        "id": "i7EFJeo_qif7",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "da9215fa-ac68-443f-ee10-9a6e33012957"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "After Z_Score capping:\n",
            "   Student  Marks   Z_Score  Marks_Treated\n",
            "0        A     50 -0.643187       50.00000\n",
            "1        B     52 -0.578054       52.00000\n",
            "2        C     54 -0.512921       54.00000\n",
            "3        D     55 -0.480355       55.00000\n",
            "4        E     56 -0.447788       56.00000\n",
            "5        F     58 -0.382655       58.00000\n",
            "6        G     60 -0.317523       60.00000\n",
            "7        H     61 -0.284956       61.00000\n",
            "8        I     62 -0.252390       62.00000\n",
            "9        J     63 -0.219823       63.00000\n",
            "10       K     64 -0.187257       64.00000\n",
            "11       L     65 -0.154691       65.00000\n",
            "12       M     66 -0.122124       66.00000\n",
            "13       N     68 -0.056991       68.00000\n",
            "14       O     70  0.008142       70.00000\n",
            "15       P     71  0.040708       71.00000\n",
            "16       Q     72  0.073274       72.00000\n",
            "17       R     73  0.105841       73.00000\n",
            "18       S     75  0.170974       75.00000\n",
            "19       T    200  4.241777      161.86942\n"
          ]
        }
      ]
    }
  ]
}