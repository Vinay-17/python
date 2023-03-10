{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNS3PWPS3DYKRd0MIY7jukC",
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
        "<a href=\"https://colab.research.google.com/github/Vinay-17/python/blob/main/upperandlowercase.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yogzpBBW8HeQ"
      },
      "outputs": [],
      "source": [
        "def count_case(string):\n",
        "    upper_count = 0\n",
        "    lower_count = 0\n",
        "    for char in string:\n",
        "        if char.isupper():\n",
        "            upper_count += 1\n",
        "        elif char.islower():\n",
        "            lower_count += 1\n",
        "    return upper_count, lower_count\n",
        "string=input(\"Enter your string:\")\n",
        "upper_count, lower_count = count_case(string)\n",
        "print(\"The number of uppercase letters is:\", upper_count)\n",
        "print(\"The number of lowercase letters is:\", lower_count)\n",
        "output:\n",
        "Enter your string:'The quick Brow Fox'\n",
        "\n",
        "\n",
        "The number of uppercase letters is: 3\n",
        "The number of lowercase letters is: 12\n",
        "> "
      ]
    }
  ]
}