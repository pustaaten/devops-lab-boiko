{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMjQKzj4fQf1abxG1j7hzjZ"
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
        "id": "_ZK42AHsrrSP"
      },
      "outputs": [],
      "source": [
        "from flask import Flask\n",
        " app = Flask(__name__)\n",
        "\n",
        " @app.route('/')\n",
        " def hello():\n",
        "    return \"Hello from Docker!\"\n",
        "\n",
        " if __name__ == '__main__':\n",
        "    app.run(host='0.0.0.0', port=5000)"
      ]
    }
  ]
}