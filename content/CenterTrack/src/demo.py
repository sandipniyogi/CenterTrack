{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "startfile12.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "mount_file_id": "1iBT7q9U2iAxPy5Hae5oYhqa8N9HP500W",
      "authorship_tag": "ABX9TyM/eMZfw1sq6PbC7q9IFcRh",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sandipniyogi/CenterTrack/blob/main/content/CenterTrack/src/demo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3ccOcU5tvgoZ",
        "outputId": "376459e0-5711-4c1a-d288-7421b42f68cd"
      },
      "source": [
        "!pip install cython; pip install -U 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'\n",
        "!git clone --recursive https://github.com/sandipniyogi/CenterTrack.git\n",
        "\n"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: cython in /usr/local/lib/python3.7/dist-packages (0.29.22)\n",
            "Collecting git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI\n",
            "  Cloning https://github.com/cocodataset/cocoapi.git to /tmp/pip-req-build-7e1oxob7\n",
            "  Running command git clone -q https://github.com/cocodataset/cocoapi.git /tmp/pip-req-build-7e1oxob7\n",
            "Requirement already satisfied, skipping upgrade: setuptools>=18.0 in /usr/local/lib/python3.7/dist-packages (from pycocotools==2.0) (54.0.0)\n",
            "Requirement already satisfied, skipping upgrade: cython>=0.27.3 in /usr/local/lib/python3.7/dist-packages (from pycocotools==2.0) (0.29.22)\n",
            "Requirement already satisfied, skipping upgrade: matplotlib>=2.1.0 in /usr/local/lib/python3.7/dist-packages (from pycocotools==2.0) (3.2.2)\n",
            "Requirement already satisfied, skipping upgrade: cycler>=0.10 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=2.1.0->pycocotools==2.0) (0.10.0)\n",
            "Requirement already satisfied, skipping upgrade: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=2.1.0->pycocotools==2.0) (2.4.7)\n",
            "Requirement already satisfied, skipping upgrade: python-dateutil>=2.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=2.1.0->pycocotools==2.0) (2.8.1)\n",
            "Requirement already satisfied, skipping upgrade: numpy>=1.11 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=2.1.0->pycocotools==2.0) (1.19.5)\n",
            "Requirement already satisfied, skipping upgrade: kiwisolver>=1.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=2.1.0->pycocotools==2.0) (1.3.1)\n",
            "Requirement already satisfied, skipping upgrade: six in /usr/local/lib/python3.7/dist-packages (from cycler>=0.10->matplotlib>=2.1.0->pycocotools==2.0) (1.15.0)\n",
            "Building wheels for collected packages: pycocotools\n",
            "  Building wheel for pycocotools (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pycocotools: filename=pycocotools-2.0-cp37-cp37m-linux_x86_64.whl size=263917 sha256=11b119eb6ac714c9ce1bb4c87c0e78d43ee9d2bd2b9f2f5810707f34a166c270\n",
            "  Stored in directory: /tmp/pip-ephem-wheel-cache-9t_i8u11/wheels/90/51/41/646daf401c3bc408ff10de34ec76587a9b3ebfac8d21ca5c3a\n",
            "Successfully built pycocotools\n",
            "\u001b[31mERROR: nuscenes-devkit 1.1.2 has requirement pycocotools>=2.0.1, but you'll have pycocotools 2.0 which is incompatible.\u001b[0m\n",
            "Installing collected packages: pycocotools\n",
            "  Found existing installation: pycocotools 2.0.2\n",
            "    Uninstalling pycocotools-2.0.2:\n",
            "      Successfully uninstalled pycocotools-2.0.2\n",
            "Successfully installed pycocotools-2.0\n",
            "Cloning into 'CenterTrack'...\n",
            "remote: Enumerating objects: 199, done.\u001b[K\n",
            "remote: Counting objects: 100% (199/199), done.\u001b[K\n",
            "remote: Compressing objects: 100% (160/160), done.\u001b[K\n",
            "remote: Total 199 (delta 36), reused 192 (delta 34), pack-reused 0\u001b[K\n",
            "Receiving objects: 100% (199/199), 14.91 MiB | 25.71 MiB/s, done.\n",
            "Resolving deltas: 100% (36/36), done.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rldwg_Jvxk3g",
        "outputId": "319cafb6-5876-4076-fcf4-c29ea9ac2b41"
      },
      "source": [
        "!cp -r /content/drive/MyDrive/ColabNotebooks/ .\n",
        "!cd CenterTrack; pip install -r requirements.txt\n",
        "!cd CenterTrack/src/lib/model/networks/;git clone https://github.com/lbin/DCNv2.git;\n",
        "! cd CenterTrack/src/lib/model/networks/DCNv2;chmod +x make.sh;./make.sh"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: opencv-python in /usr/local/lib/python3.7/dist-packages (from -r requirements.txt (line 1)) (4.1.2.30)\n",
            "Requirement already satisfied: Cython in /usr/local/lib/python3.7/dist-packages (from -r requirements.txt (line 2)) (0.29.22)\n",
            "Requirement already satisfied: numba in /usr/local/lib/python3.7/dist-packages (from -r requirements.txt (line 3)) (0.51.2)\n",
            "Collecting progress\n",
            "  Downloading https://files.pythonhosted.org/packages/38/ef/2e887b3d2b248916fc2121889ce68af8a16aaddbe82f9ae6533c24ff0d2b/progress-1.5.tar.gz\n",
            "Requirement already satisfied: matplotlib in /usr/local/lib/python3.7/dist-packages (from -r requirements.txt (line 5)) (3.2.2)\n",
            "Requirement already satisfied: easydict in /usr/local/lib/python3.7/dist-packages (from -r requirements.txt (line 6)) (1.9)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.7/dist-packages (from -r requirements.txt (line 7)) (1.4.1)\n",
            "Collecting pyquaternion\n",
            "  Downloading https://files.pythonhosted.org/packages/49/b3/d8482e8cacc8ea15a356efea13d22ce1c5914a9ee36622ba250523240bf2/pyquaternion-0.9.9-py3-none-any.whl\n",
            "Collecting nuscenes-devkit\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/08/2f/8738468c899c92733466574d700d9ab9f4f745948847b85c7ecfec4e336f/nuscenes_devkit-1.1.2-py3-none-any.whl (282kB)\n",
            "\u001b[K     |████████████████████████████████| 286kB 7.5MB/s \n",
            "\u001b[?25hRequirement already satisfied: pyyaml in /usr/local/lib/python3.7/dist-packages (from -r requirements.txt (line 10)) (3.13)\n",
            "Collecting motmetrics\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/9c/28/9c3bc8e2a87f4c9e7b04ab72856ec7f9895a66681a65973ffaf9562ef879/motmetrics-1.2.0-py3-none-any.whl (151kB)\n",
            "\u001b[K     |████████████████████████████████| 153kB 11.5MB/s \n",
            "\u001b[?25hCollecting scikit-learn==0.22.2\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/71/b0/471bfdb7741523dfbddd038cb5f7cc9e21d8aaa1987839af6f17238254c0/scikit_learn-0.22.2-cp37-cp37m-manylinux1_x86_64.whl (7.1MB)\n",
            "\u001b[K     |████████████████████████████████| 7.1MB 12.9MB/s \n",
            "\u001b[?25hRequirement already satisfied: numpy>=1.14.5 in /usr/local/lib/python3.7/dist-packages (from opencv-python->-r requirements.txt (line 1)) (1.19.5)\n",
            "Requirement already satisfied: llvmlite<0.35,>=0.34.0.dev0 in /usr/local/lib/python3.7/dist-packages (from numba->-r requirements.txt (line 3)) (0.34.0)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.7/dist-packages (from numba->-r requirements.txt (line 3)) (54.0.0)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib->-r requirements.txt (line 5)) (2.8.1)\n",
            "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib->-r requirements.txt (line 5)) (1.3.1)\n",
            "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib->-r requirements.txt (line 5)) (2.4.7)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.7/dist-packages (from matplotlib->-r requirements.txt (line 5)) (0.10.0)\n",
            "Requirement already satisfied: Pillow in /usr/local/lib/python3.7/dist-packages (from nuscenes-devkit->-r requirements.txt (line 9)) (7.0.0)\n",
            "Requirement already satisfied: cachetools in /usr/local/lib/python3.7/dist-packages (from nuscenes-devkit->-r requirements.txt (line 9)) (4.2.1)\n",
            "Requirement already satisfied: Shapely in /usr/local/lib/python3.7/dist-packages (from nuscenes-devkit->-r requirements.txt (line 9)) (1.7.1)\n",
            "Collecting pycocotools>=2.0.1\n",
            "  Downloading https://files.pythonhosted.org/packages/de/df/056875d697c45182ed6d2ae21f62015896fdb841906fe48e7268e791c467/pycocotools-2.0.2.tar.gz\n",
            "Requirement already satisfied: jupyter in /usr/local/lib/python3.7/dist-packages (from nuscenes-devkit->-r requirements.txt (line 9)) (1.0.0)\n",
            "Collecting fire\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/11/07/a119a1aa04d37bc819940d95ed7e135a7dcca1c098123a3764a6dcace9e7/fire-0.4.0.tar.gz (87kB)\n",
            "\u001b[K     |████████████████████████████████| 92kB 13.8MB/s \n",
            "\u001b[?25hRequirement already satisfied: descartes in /usr/local/lib/python3.7/dist-packages (from nuscenes-devkit->-r requirements.txt (line 9)) (1.1.0)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.7/dist-packages (from nuscenes-devkit->-r requirements.txt (line 9)) (4.41.1)\n",
            "Collecting xmltodict>=0.12.0\n",
            "  Downloading https://files.pythonhosted.org/packages/28/fd/30d5c1d3ac29ce229f6bdc40bbc20b28f716e8b363140c26eff19122d8a5/xmltodict-0.12.0-py2.py3-none-any.whl\n",
            "Collecting flake8\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/d4/ca/3971802ee6251da1abead1a22831d7f4743781e2f743bd266bdd2f46c19b/flake8-3.8.4-py2.py3-none-any.whl (72kB)\n",
            "\u001b[K     |████████████████████████████████| 81kB 11.0MB/s \n",
            "\u001b[?25hRequirement already satisfied: pytest in /usr/local/lib/python3.7/dist-packages (from motmetrics->-r requirements.txt (line 11)) (3.6.4)\n",
            "Collecting flake8-import-order\n",
            "  Downloading https://files.pythonhosted.org/packages/ab/52/cf2d6e2c505644ca06de2f6f3546f1e4f2b7be34246c9e0757c6048868f9/flake8_import_order-0.18.1-py2.py3-none-any.whl\n",
            "Collecting pytest-benchmark\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/e7/1e/180579ad3bc53fe3181ef3843f0602f4db77f3609e5e5069a0ec194ff213/pytest_benchmark-3.2.3-py2.py3-none-any.whl (49kB)\n",
            "\u001b[K     |████████████████████████████████| 51kB 9.1MB/s \n",
            "\u001b[?25hRequirement already satisfied: pandas>=0.23.1 in /usr/local/lib/python3.7/dist-packages (from motmetrics->-r requirements.txt (line 11)) (1.1.5)\n",
            "Requirement already satisfied: joblib>=0.11 in /usr/local/lib/python3.7/dist-packages (from scikit-learn==0.22.2->-r requirements.txt (line 12)) (1.0.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.1->matplotlib->-r requirements.txt (line 5)) (1.15.0)\n",
            "Requirement already satisfied: ipykernel in /usr/local/lib/python3.7/dist-packages (from jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (4.10.1)\n",
            "Requirement already satisfied: qtconsole in /usr/local/lib/python3.7/dist-packages (from jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (5.0.2)\n",
            "Requirement already satisfied: jupyter-console in /usr/local/lib/python3.7/dist-packages (from jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (5.2.0)\n",
            "Requirement already satisfied: notebook in /usr/local/lib/python3.7/dist-packages (from jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (5.3.1)\n",
            "Requirement already satisfied: ipywidgets in /usr/local/lib/python3.7/dist-packages (from jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (7.6.3)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.7/dist-packages (from jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (5.6.1)\n",
            "Requirement already satisfied: termcolor in /usr/local/lib/python3.7/dist-packages (from fire->nuscenes-devkit->-r requirements.txt (line 9)) (1.1.0)\n",
            "Requirement already satisfied: importlib-metadata; python_version < \"3.8\" in /usr/local/lib/python3.7/dist-packages (from flake8->motmetrics->-r requirements.txt (line 11)) (3.7.0)\n",
            "Collecting pyflakes<2.3.0,>=2.2.0\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/69/5b/fd01b0c696f2f9a6d2c839883b642493b431f28fa32b29abc465ef675473/pyflakes-2.2.0-py2.py3-none-any.whl (66kB)\n",
            "\u001b[K     |████████████████████████████████| 71kB 12.0MB/s \n",
            "\u001b[?25hCollecting mccabe<0.7.0,>=0.6.0\n",
            "  Downloading https://files.pythonhosted.org/packages/87/89/479dc97e18549e21354893e4ee4ef36db1d237534982482c3681ee6e7b57/mccabe-0.6.1-py2.py3-none-any.whl\n",
            "Collecting pycodestyle<2.7.0,>=2.6.0a1\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/10/5b/88879fb861ab79aef45c7e199cae3ef7af487b5603dcb363517a50602dd7/pycodestyle-2.6.0-py2.py3-none-any.whl (41kB)\n",
            "\u001b[K     |████████████████████████████████| 51kB 9.8MB/s \n",
            "\u001b[?25hRequirement already satisfied: more-itertools>=4.0.0 in /usr/local/lib/python3.7/dist-packages (from pytest->motmetrics->-r requirements.txt (line 11)) (8.7.0)\n",
            "Requirement already satisfied: atomicwrites>=1.0 in /usr/local/lib/python3.7/dist-packages (from pytest->motmetrics->-r requirements.txt (line 11)) (1.4.0)\n",
            "Requirement already satisfied: py>=1.5.0 in /usr/local/lib/python3.7/dist-packages (from pytest->motmetrics->-r requirements.txt (line 11)) (1.10.0)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.7/dist-packages (from pytest->motmetrics->-r requirements.txt (line 11)) (20.3.0)\n",
            "Requirement already satisfied: pluggy<0.8,>=0.5 in /usr/local/lib/python3.7/dist-packages (from pytest->motmetrics->-r requirements.txt (line 11)) (0.7.1)\n",
            "Collecting py-cpuinfo\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/f6/f5/8e6e85ce2e9f6e05040cf0d4e26f43a4718bcc4bce988b433276d4b1a5c1/py-cpuinfo-7.0.0.tar.gz (95kB)\n",
            "\u001b[K     |████████████████████████████████| 102kB 15.8MB/s \n",
            "\u001b[?25hRequirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.23.1->motmetrics->-r requirements.txt (line 11)) (2018.9)\n",
            "Requirement already satisfied: traitlets>=4.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (5.0.5)\n",
            "Requirement already satisfied: jupyter-client in /usr/local/lib/python3.7/dist-packages (from ipykernel->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (5.3.5)\n",
            "Requirement already satisfied: ipython>=4.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (5.5.0)\n",
            "Requirement already satisfied: tornado>=4.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (5.1.1)\n",
            "Requirement already satisfied: jupyter-core in /usr/local/lib/python3.7/dist-packages (from qtconsole->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (4.7.1)\n",
            "Requirement already satisfied: ipython-genutils in /usr/local/lib/python3.7/dist-packages (from qtconsole->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (0.2.0)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from qtconsole->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (2.6.1)\n",
            "Requirement already satisfied: pyzmq>=17.1 in /usr/local/lib/python3.7/dist-packages (from qtconsole->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (22.0.3)\n",
            "Requirement already satisfied: qtpy in /usr/local/lib/python3.7/dist-packages (from qtconsole->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (1.9.0)\n",
            "Requirement already satisfied: prompt-toolkit<2.0.0,>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-console->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (1.0.18)\n",
            "Requirement already satisfied: nbformat in /usr/local/lib/python3.7/dist-packages (from notebook->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (5.1.2)\n",
            "Requirement already satisfied: terminado>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from notebook->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (0.9.2)\n",
            "Requirement already satisfied: Send2Trash in /usr/local/lib/python3.7/dist-packages (from notebook->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (1.5.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.7/dist-packages (from notebook->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (2.11.3)\n",
            "Requirement already satisfied: jupyterlab-widgets>=1.0.0; python_version >= \"3.6\" in /usr/local/lib/python3.7/dist-packages (from ipywidgets->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (1.0.0)\n",
            "Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (3.5.1)\n",
            "Requirement already satisfied: entrypoints>=0.2.2 in /usr/local/lib/python3.7/dist-packages (from nbconvert->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (0.3)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (0.6.0)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (3.3.0)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (0.8.4)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (1.4.3)\n",
            "Requirement already satisfied: testpath in /usr/local/lib/python3.7/dist-packages (from nbconvert->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (0.4.4)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata; python_version < \"3.8\"->flake8->motmetrics->-r requirements.txt (line 11)) (3.4.0)\n",
            "Requirement already satisfied: typing-extensions>=3.6.4; python_version < \"3.8\" in /usr/local/lib/python3.7/dist-packages (from importlib-metadata; python_version < \"3.8\"->flake8->motmetrics->-r requirements.txt (line 11)) (3.7.4.3)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython>=4.0.0->ipykernel->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (4.4.2)\n",
            "Requirement already satisfied: simplegeneric>0.8 in /usr/local/lib/python3.7/dist-packages (from ipython>=4.0.0->ipykernel->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (0.8.1)\n",
            "Requirement already satisfied: pexpect; sys_platform != \"win32\" in /usr/local/lib/python3.7/dist-packages (from ipython>=4.0.0->ipykernel->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (4.8.0)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython>=4.0.0->ipykernel->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (0.7.5)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit<2.0.0,>=1.0.0->jupyter-console->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (0.2.5)\n",
            "Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in /usr/local/lib/python3.7/dist-packages (from nbformat->notebook->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (2.6.0)\n",
            "Requirement already satisfied: ptyprocess; os_name != \"nt\" in /usr/local/lib/python3.7/dist-packages (from terminado>=0.8.1->notebook->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (0.7.0)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from jinja2->notebook->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (1.1.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (20.9)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->jupyter->nuscenes-devkit->-r requirements.txt (line 9)) (0.5.1)\n",
            "Building wheels for collected packages: progress, pycocotools, fire, py-cpuinfo\n",
            "  Building wheel for progress (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for progress: filename=progress-1.5-cp37-none-any.whl size=8074 sha256=bfe0e95c28356b57fb89b58541cca10d7263dfc9ccfb84494ff50da0b23763e0\n",
            "  Stored in directory: /root/.cache/pip/wheels/6c/c8/80/32a294e3041f006c661838c05a411c7b7ffc60ff939d14e116\n",
            "  Building wheel for pycocotools (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for pycocotools: filename=pycocotools-2.0.2-cp37-cp37m-linux_x86_64.whl size=263988 sha256=b05c0f84111cf5a540f6df771251c7ab50975e23f153cb4f4a9cdc02de78a80c\n",
            "  Stored in directory: /root/.cache/pip/wheels/68/a5/e7/56401832f23d0b2db351c5b682e466cb4841960b086da65e4e\n",
            "  Building wheel for fire (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for fire: filename=fire-0.4.0-py2.py3-none-any.whl size=115928 sha256=b98bc873a04a1c8c71003b818b7138667d8bdb0443183458f9d259a3fb4c66a4\n",
            "  Stored in directory: /root/.cache/pip/wheels/af/19/30/1ea0cad502dcb4e66ed5a690279628c827aea38bbbab75d5ed\n",
            "  Building wheel for py-cpuinfo (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for py-cpuinfo: filename=py_cpuinfo-7.0.0-cp37-none-any.whl size=20070 sha256=9125b3445f35dc2e13df90734a5fbb1261c9247234dbe8e31be52ffad97f92bb\n",
            "  Stored in directory: /root/.cache/pip/wheels/f1/93/7b/127daf0c3a5a49feb2fecd468d508067c733fba5192f726ad1\n",
            "Successfully built progress pycocotools fire py-cpuinfo\n",
            "\u001b[31mERROR: pytest-benchmark 3.2.3 has requirement pytest>=3.8, but you'll have pytest 3.6.4 which is incompatible.\u001b[0m\n",
            "Installing collected packages: progress, pyquaternion, pycocotools, fire, scikit-learn, nuscenes-devkit, xmltodict, pyflakes, mccabe, pycodestyle, flake8, flake8-import-order, py-cpuinfo, pytest-benchmark, motmetrics\n",
            "  Found existing installation: pycocotools 2.0\n",
            "    Uninstalling pycocotools-2.0:\n",
            "      Successfully uninstalled pycocotools-2.0\n",
            "  Found existing installation: scikit-learn 0.22.2.post1\n",
            "    Uninstalling scikit-learn-0.22.2.post1:\n",
            "      Successfully uninstalled scikit-learn-0.22.2.post1\n",
            "Successfully installed fire-0.4.0 flake8-3.8.4 flake8-import-order-0.18.1 mccabe-0.6.1 motmetrics-1.2.0 nuscenes-devkit-1.1.2 progress-1.5 py-cpuinfo-7.0.0 pycocotools-2.0.2 pycodestyle-2.6.0 pyflakes-2.2.0 pyquaternion-0.9.9 pytest-benchmark-3.2.3 scikit-learn-0.22.2 xmltodict-0.12.0\n",
            "Cloning into 'DCNv2'...\n",
            "remote: Enumerating objects: 23, done.\u001b[K\n",
            "remote: Counting objects: 100% (23/23), done.\u001b[K\n",
            "remote: Compressing objects: 100% (17/17), done.\u001b[K\n",
            "remote: Total 263 (delta 9), reused 12 (delta 6), pack-reused 240\u001b[K\n",
            "Receiving objects: 100% (263/263), 1.44 MiB | 6.06 MiB/s, done.\n",
            "Resolving deltas: 100% (151/151), done.\n",
            "running build\n",
            "running build_ext\n",
            "/usr/local/lib/python3.7/dist-packages/torch/utils/cpp_extension.py:352: UserWarning: Attempted to use ninja as the BuildExtension backend but we could not find ninja.. Falling back to using the slow distutils backend.\n",
            "  warnings.warn(msg.format('we could not find ninja.'))\n",
            "building '_ext' extension\n",
            "creating build\n",
            "creating build/temp.linux-x86_64-3.7\n",
            "creating build/temp.linux-x86_64-3.7/content\n",
            "creating build/temp.linux-x86_64-3.7/content/CenterTrack\n",
            "creating build/temp.linux-x86_64-3.7/content/CenterTrack/src\n",
            "creating build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib\n",
            "creating build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model\n",
            "creating build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks\n",
            "creating build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2\n",
            "creating build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src\n",
            "creating build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cpu\n",
            "creating build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cuda\n",
            "g++ -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fdebug-prefix-map=/build/python3.7-a56wZI/python3.7-3.7.10=. -fstack-protector-strong -Wformat -Werror=format-security -g -fdebug-prefix-map=/build/python3.7-a56wZI/python3.7-3.7.10=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DWITH_CUDA -I/content/CenterTrack/src/lib/model/networks/DCNv2/src -I/usr/local/lib/python3.7/dist-packages/torch/include -I/usr/local/lib/python3.7/dist-packages/torch/include/torch/csrc/api/include -I/usr/local/lib/python3.7/dist-packages/torch/include/TH -I/usr/local/lib/python3.7/dist-packages/torch/include/THC -I/usr/local/cuda/include -I/usr/include/python3.7m -c /content/CenterTrack/src/lib/model/networks/DCNv2/src/vision.cpp -o build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/vision.o -fopenmp -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -DTORCH_EXTENSION_NAME=_ext -D_GLIBCXX_USE_CXX11_ABI=0 -std=c++14\n",
            "g++ -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fdebug-prefix-map=/build/python3.7-a56wZI/python3.7-3.7.10=. -fstack-protector-strong -Wformat -Werror=format-security -g -fdebug-prefix-map=/build/python3.7-a56wZI/python3.7-3.7.10=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DWITH_CUDA -I/content/CenterTrack/src/lib/model/networks/DCNv2/src -I/usr/local/lib/python3.7/dist-packages/torch/include -I/usr/local/lib/python3.7/dist-packages/torch/include/torch/csrc/api/include -I/usr/local/lib/python3.7/dist-packages/torch/include/TH -I/usr/local/lib/python3.7/dist-packages/torch/include/THC -I/usr/local/cuda/include -I/usr/include/python3.7m -c /content/CenterTrack/src/lib/model/networks/DCNv2/src/cpu/dcn_v2_psroi_pooling_cpu.cpp -o build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cpu/dcn_v2_psroi_pooling_cpu.o -fopenmp -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -DTORCH_EXTENSION_NAME=_ext -D_GLIBCXX_USE_CXX11_ABI=0 -std=c++14\n",
            "g++ -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fdebug-prefix-map=/build/python3.7-a56wZI/python3.7-3.7.10=. -fstack-protector-strong -Wformat -Werror=format-security -g -fdebug-prefix-map=/build/python3.7-a56wZI/python3.7-3.7.10=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DWITH_CUDA -I/content/CenterTrack/src/lib/model/networks/DCNv2/src -I/usr/local/lib/python3.7/dist-packages/torch/include -I/usr/local/lib/python3.7/dist-packages/torch/include/torch/csrc/api/include -I/usr/local/lib/python3.7/dist-packages/torch/include/TH -I/usr/local/lib/python3.7/dist-packages/torch/include/THC -I/usr/local/cuda/include -I/usr/include/python3.7m -c /content/CenterTrack/src/lib/model/networks/DCNv2/src/cpu/dcn_v2_cpu.cpp -o build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cpu/dcn_v2_cpu.o -fopenmp -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -DTORCH_EXTENSION_NAME=_ext -D_GLIBCXX_USE_CXX11_ABI=0 -std=c++14\n",
            "g++ -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fdebug-prefix-map=/build/python3.7-a56wZI/python3.7-3.7.10=. -fstack-protector-strong -Wformat -Werror=format-security -g -fdebug-prefix-map=/build/python3.7-a56wZI/python3.7-3.7.10=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -DWITH_CUDA -I/content/CenterTrack/src/lib/model/networks/DCNv2/src -I/usr/local/lib/python3.7/dist-packages/torch/include -I/usr/local/lib/python3.7/dist-packages/torch/include/torch/csrc/api/include -I/usr/local/lib/python3.7/dist-packages/torch/include/TH -I/usr/local/lib/python3.7/dist-packages/torch/include/THC -I/usr/local/cuda/include -I/usr/include/python3.7m -c /content/CenterTrack/src/lib/model/networks/DCNv2/src/cpu/dcn_v2_im2col_cpu.cpp -o build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cpu/dcn_v2_im2col_cpu.o -fopenmp -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -DTORCH_EXTENSION_NAME=_ext -D_GLIBCXX_USE_CXX11_ABI=0 -std=c++14\n",
            "/usr/local/cuda/bin/nvcc -DWITH_CUDA -I/content/CenterTrack/src/lib/model/networks/DCNv2/src -I/usr/local/lib/python3.7/dist-packages/torch/include -I/usr/local/lib/python3.7/dist-packages/torch/include/torch/csrc/api/include -I/usr/local/lib/python3.7/dist-packages/torch/include/TH -I/usr/local/lib/python3.7/dist-packages/torch/include/THC -I/usr/local/cuda/include -I/usr/include/python3.7m -c /content/CenterTrack/src/lib/model/networks/DCNv2/src/cuda/dcn_v2_im2col_cuda.cu -o build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cuda/dcn_v2_im2col_cuda.o -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options '-fPIC' -DCUDA_HAS_FP16=1 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -DTORCH_EXTENSION_NAME=_ext -D_GLIBCXX_USE_CXX11_ABI=0 -gencode=arch=compute_75,code=sm_75 -ccbin g++ -std=c++14\n",
            "/usr/local/cuda/bin/nvcc -DWITH_CUDA -I/content/CenterTrack/src/lib/model/networks/DCNv2/src -I/usr/local/lib/python3.7/dist-packages/torch/include -I/usr/local/lib/python3.7/dist-packages/torch/include/torch/csrc/api/include -I/usr/local/lib/python3.7/dist-packages/torch/include/TH -I/usr/local/lib/python3.7/dist-packages/torch/include/THC -I/usr/local/cuda/include -I/usr/include/python3.7m -c /content/CenterTrack/src/lib/model/networks/DCNv2/src/cuda/dcn_v2_psroi_pooling_cuda.cu -o build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cuda/dcn_v2_psroi_pooling_cuda.o -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options '-fPIC' -DCUDA_HAS_FP16=1 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -DTORCH_EXTENSION_NAME=_ext -D_GLIBCXX_USE_CXX11_ABI=0 -gencode=arch=compute_75,code=sm_75 -ccbin g++ -std=c++14\n",
            "/usr/local/cuda/bin/nvcc -DWITH_CUDA -I/content/CenterTrack/src/lib/model/networks/DCNv2/src -I/usr/local/lib/python3.7/dist-packages/torch/include -I/usr/local/lib/python3.7/dist-packages/torch/include/torch/csrc/api/include -I/usr/local/lib/python3.7/dist-packages/torch/include/TH -I/usr/local/lib/python3.7/dist-packages/torch/include/THC -I/usr/local/cuda/include -I/usr/include/python3.7m -c /content/CenterTrack/src/lib/model/networks/DCNv2/src/cuda/dcn_v2_cuda.cu -o build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cuda/dcn_v2_cuda.o -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options '-fPIC' -DCUDA_HAS_FP16=1 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ -DTORCH_API_INCLUDE_EXTENSION_H -DPYBIND11_COMPILER_TYPE=\"_gcc\" -DPYBIND11_STDLIB=\"_libstdcpp\" -DPYBIND11_BUILD_ABI=\"_cxxabi1011\" -DTORCH_EXTENSION_NAME=_ext -D_GLIBCXX_USE_CXX11_ABI=0 -gencode=arch=compute_75,code=sm_75 -ccbin g++ -std=c++14\n",
            "creating build/lib.linux-x86_64-3.7\n",
            "x86_64-linux-gnu-g++ -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fdebug-prefix-map=/build/python3.7-a56wZI/python3.7-3.7.10=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/vision.o build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cpu/dcn_v2_psroi_pooling_cpu.o build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cpu/dcn_v2_cpu.o build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cpu/dcn_v2_im2col_cpu.o build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cuda/dcn_v2_im2col_cuda.o build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cuda/dcn_v2_psroi_pooling_cuda.o build/temp.linux-x86_64-3.7/content/CenterTrack/src/lib/model/networks/DCNv2/src/cuda/dcn_v2_cuda.o -L/usr/local/lib/python3.7/dist-packages/torch/lib -L/usr/local/cuda/lib64 -lc10 -ltorch -ltorch_cpu -ltorch_python -lcudart -lc10_cuda -ltorch_cuda -o build/lib.linux-x86_64-3.7/_ext.cpython-37m-x86_64-linux-gnu.so\n",
            "running develop\n",
            "running egg_info\n",
            "creating DCNv2.egg-info\n",
            "writing DCNv2.egg-info/PKG-INFO\n",
            "writing dependency_links to DCNv2.egg-info/dependency_links.txt\n",
            "writing top-level names to DCNv2.egg-info/top_level.txt\n",
            "writing manifest file 'DCNv2.egg-info/SOURCES.txt'\n",
            "writing manifest file 'DCNv2.egg-info/SOURCES.txt'\n",
            "running build_ext\n",
            "copying build/lib.linux-x86_64-3.7/_ext.cpython-37m-x86_64-linux-gnu.so -> \n",
            "Creating /usr/local/lib/python3.7/dist-packages/DCNv2.egg-link (link to .)\n",
            "Adding DCNv2 0.1 to easy-install.pth file\n",
            "\n",
            "Installed /content/CenterTrack/src/lib/model/networks/DCNv2\n",
            "Processing dependencies for DCNv2==0.1\n",
            "Finished processing dependencies for DCNv2==0.1\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "voQKsstoyW46"
      },
      "source": [
        "!pip install gdown\n",
        "#https://drive.google.com/file/d/1tJCEJmdtYIh8VuN8CClGNws3YO7QGd40/view?usp=sharing\n",
        "#https://drive.google.com/file/d/1sf1bWJ1LutwQ_wp176nd2Y3HII9WeFf0/view?usp=sharing\n",
        "\n",
        "!gdown --id 1H0YvFYCOIZ06EzAkC2NxECNQGXxK27hH"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "I512ufGmLQAm"
      },
      "source": [
        "!rm -rf CenterTrack"
      ],
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kGZhv_XAPPit",
        "outputId": "e1bcba70-0961-4c77-851c-580e1cc682dc"
      },
      "source": [
        "!python /content/CenterTrack/src/demo.py"
      ],
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/linear_assignment_.py:22: FutureWarning: The linear_assignment_ module is deprecated in 0.21 and will be removed from 0.23. Use scipy.optimize.linear_sum_assignment instead.\n",
            "  FutureWarning)\n",
            "usage: demo.py [-h] [--dataset DATASET] [--test_dataset TEST_DATASET]\n",
            "               [--exp_id EXP_ID] [--test] [--debug DEBUG] [--no_pause]\n",
            "               [--demo DEMO] [--load_model LOAD_MODEL] [--resume]\n",
            "               [--gpus GPUS] [--num_workers NUM_WORKERS]\n",
            "               [--not_cuda_benchmark] [--seed SEED] [--not_set_cuda_env]\n",
            "               [--print_iter PRINT_ITER] [--save_all]\n",
            "               [--vis_thresh VIS_THRESH] [--debugger_theme {white,black}]\n",
            "               [--eval_val] [--save_imgs SAVE_IMGS]\n",
            "               [--save_img_suffix SAVE_IMG_SUFFIX] [--skip_first SKIP_FIRST]\n",
            "               [--save_video] [--save_framerate SAVE_FRAMERATE]\n",
            "               [--resize_video] [--video_h VIDEO_H] [--video_w VIDEO_W]\n",
            "               [--transpose_video] [--show_track_color] [--not_show_bbox]\n",
            "               [--not_show_number] [--not_show_txt] [--qualitative]\n",
            "               [--tango_color] [--only_show_dots] [--show_trace] [--arch ARCH]\n",
            "               [--dla_node DLA_NODE] [--head_conv HEAD_CONV]\n",
            "               [--num_head_conv NUM_HEAD_CONV] [--head_kernel HEAD_KERNEL]\n",
            "               [--down_ratio DOWN_RATIO] [--not_idaup]\n",
            "               [--num_classes NUM_CLASSES] [--num_layers NUM_LAYERS]\n",
            "               [--backbone BACKBONE] [--neck NECK]\n",
            "               [--msra_outchannel MSRA_OUTCHANNEL]\n",
            "               [--efficient_level EFFICIENT_LEVEL] [--prior_bias PRIOR_BIAS]\n",
            "               [--input_res INPUT_RES] [--input_h INPUT_H] [--input_w INPUT_W]\n",
            "               [--dataset_version DATASET_VERSION] [--optim OPTIM] [--lr LR]\n",
            "               [--lr_step LR_STEP] [--save_point SAVE_POINT]\n",
            "               [--num_epochs NUM_EPOCHS] [--batch_size BATCH_SIZE]\n",
            "               [--master_batch_size MASTER_BATCH_SIZE] [--num_iters NUM_ITERS]\n",
            "               [--val_intervals VAL_INTERVALS] [--trainval] [--ltrb]\n",
            "               [--ltrb_weight LTRB_WEIGHT] [--reset_hm] [--reuse_hm]\n",
            "               [--use_kpt_center] [--add_05] [--dense_reg DENSE_REG]\n",
            "               [--flip_test] [--test_scales TEST_SCALES] [--nms] [--K K]\n",
            "               [--not_prefetch_test] [--fix_short FIX_SHORT] [--keep_res]\n",
            "               [--map_argoverse_id] [--out_thresh OUT_THRESH]\n",
            "               [--depth_scale DEPTH_SCALE] [--save_results]\n",
            "               [--load_results LOAD_RESULTS] [--use_loaded_results]\n",
            "               [--ignore_loaded_cats IGNORE_LOADED_CATS] [--model_output_list]\n",
            "               [--non_block_test] [--vis_gt_bev VIS_GT_BEV]\n",
            "               [--kitti_split KITTI_SPLIT]\n",
            "               [--test_focal_length TEST_FOCAL_LENGTH] [--not_rand_crop]\n",
            "               [--not_max_crop] [--shift SHIFT] [--scale SCALE]\n",
            "               [--aug_rot AUG_ROT] [--rotate ROTATE] [--flip FLIP]\n",
            "               [--no_color_aug] [--tracking] [--pre_hm] [--same_aug_pre]\n",
            "               [--zero_pre_hm] [--hm_disturb HM_DISTURB]\n",
            "               [--lost_disturb LOST_DISTURB] [--fp_disturb FP_DISTURB]\n",
            "               [--pre_thresh PRE_THRESH] [--track_thresh TRACK_THRESH]\n",
            "               [--new_thresh NEW_THRESH] [--max_frame_dist MAX_FRAME_DIST]\n",
            "               [--ltrb_amodal] [--ltrb_amodal_weight LTRB_AMODAL_WEIGHT]\n",
            "               [--public_det] [--no_pre_img] [--zero_tracking] [--hungarian]\n",
            "               [--max_age MAX_AGE] [--tracking_weight TRACKING_WEIGHT]\n",
            "               [--reg_loss REG_LOSS] [--hm_weight HM_WEIGHT]\n",
            "               [--off_weight OFF_WEIGHT] [--wh_weight WH_WEIGHT]\n",
            "               [--hp_weight HP_WEIGHT] [--hm_hp_weight HM_HP_WEIGHT]\n",
            "               [--amodel_offset_weight AMODEL_OFFSET_WEIGHT]\n",
            "               [--dep_weight DEP_WEIGHT] [--dim_weight DIM_WEIGHT]\n",
            "               [--rot_weight ROT_WEIGHT] [--nuscenes_att]\n",
            "               [--nuscenes_att_weight NUSCENES_ATT_WEIGHT] [--velocity]\n",
            "               [--velocity_weight VELOCITY_WEIGHT]\n",
            "               [--custom_dataset_img_path CUSTOM_DATASET_IMG_PATH]\n",
            "               [--custom_dataset_ann_path CUSTOM_DATASET_ANN_PATH]\n",
            "               task\n",
            "demo.py: error: the following arguments are required: task\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Jqpl-kEAPfVE"
      },
      "source": [
        "!! write"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q9E8hpjh-dK-",
        "outputId": "47ec55b3-f14d-407b-f5d7-c7e08a7c4d5e"
      },
      "source": [
        "!sudo apt-get install libx264-dev"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Reading package lists... Done\n",
            "Building dependency tree       \n",
            "Reading state information... Done\n",
            "The following NEW packages will be installed:\n",
            "  libx264-dev\n",
            "0 upgraded, 1 newly installed, 0 to remove and 29 not upgraded.\n",
            "Need to get 461 kB of archives.\n",
            "After this operation, 1,766 kB of additional disk space will be used.\n",
            "Get:1 http://archive.ubuntu.com/ubuntu bionic/universe amd64 libx264-dev amd64 2:0.152.2854+gite9a5903-2 [461 kB]\n",
            "Fetched 461 kB in 1s (465 kB/s)\n",
            "debconf: unable to initialize frontend: Dialog\n",
            "debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76, <> line 1.)\n",
            "debconf: falling back to frontend: Readline\n",
            "debconf: unable to initialize frontend: Readline\n",
            "debconf: (This frontend requires a controlling tty.)\n",
            "debconf: falling back to frontend: Teletype\n",
            "dpkg-preconfigure: unable to re-open stdin: \n",
            "Selecting previously unselected package libx264-dev:amd64.\n",
            "(Reading database ... 160975 files and directories currently installed.)\n",
            "Preparing to unpack .../libx264-dev_2%3a0.152.2854+gite9a5903-2_amd64.deb ...\n",
            "Unpacking libx264-dev:amd64 (2:0.152.2854+gite9a5903-2) ...\n",
            "Setting up libx264-dev:amd64 (2:0.152.2854+gite9a5903-2) ...\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DBKdv0iD-gM4",
        "outputId": "5945a4fd-6cb5-448b-89e3-737d7386ae2f"
      },
      "source": [
        "#!gdown --id 1d82DiCiyp435dyGawaMgr3sbiU8S8rEU\n",
        "!gdown --id 1noEHcNaliP2BtvDSuMkkeWNJ6VqRb-Nr\n",
        "#!gdown --id 1JXWpV4ivzEDyjwLBuJcFU6A3jwWHLodb"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Downloading...\n",
            "From: https://drive.google.com/uc?id=1noEHcNaliP2BtvDSuMkkeWNJ6VqRb-Nr\n",
            "To: /content/test4.mp4\n",
            "\r0.00B [00:00, ?B/s]\r10.5MB [00:00, 103MB/s]\r14.8MB [00:00, 90.2MB/s]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XL-NhEth_AeX",
        "outputId": "5452b0d7-0fdf-4640-8aec-61678172f2af"
      },
      "source": [
        "%matplotlib notebook\n",
        "%cd /content/CenterTrack/src/\n",
        "!mkdir ../results\n",
        "!python demo.py tracking --load_model /content/coco_pose_tracking.pth --demo /content/drive/MyDrive/ColabNotebooks/test4.mp4 --save_results\n",
        "\n",
        "\n",
        "#python demo.py tracking --load_model ../mot17_half.pth --num_class 1 --demo ../videos/nuscenes_mini.mp4"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/content/CenterTrack/src\n",
            "mkdir: cannot create directory ‘../results’: File exists\n",
            "/usr/local/lib/python3.7/dist-packages/sklearn/utils/linear_assignment_.py:22: FutureWarning: The linear_assignment_ module is deprecated in 0.21 and will be removed from 0.23. Use scipy.optimize.linear_sum_assignment instead.\n",
            "  FutureWarning)\n",
            "Running tracking\n",
            "Using tracking threshold for out threshold! 0.3\n",
            "Fix size testing.\n",
            "training chunk_sizes: [32]\n",
            "input h w: 512 512\n",
            "heads {'hm': 80, 'reg': 2, 'wh': 2, 'tracking': 2}\n",
            "weights {'hm': 1, 'reg': 1, 'wh': 0.1, 'tracking': 1}\n",
            "head conv {'hm': [256], 'reg': [256], 'wh': [256], 'tracking': [256]}\n",
            "Creating model...\n",
            "Using node type: (<class 'model.networks.dla.DeformConv'>, <class 'model.networks.dla.DeformConv'>)\n",
            "Warning: No ImageNet pretrain!!\n",
            "loaded /content/coco_pose_tracking.pth, epoch 70\n",
            "Skip loading parameter hm.2.weight, required shapetorch.Size([80, 256, 1, 1]), loaded shapetorch.Size([1, 256, 1, 1]).\n",
            "Skip loading parameter hm.2.bias, required shapetorch.Size([80]), loaded shapetorch.Size([1]).\n",
            "Drop parameter hps.0.weight.\n",
            "Drop parameter hps.0.bias.\n",
            "Drop parameter hps.2.weight.\n",
            "Drop parameter hps.2.bias.\n",
            "Drop parameter hm_hp.0.weight.\n",
            "Drop parameter hm_hp.0.bias.\n",
            "Drop parameter hm_hp.2.weight.\n",
            "Drop parameter hm_hp.2.bias.\n",
            "Drop parameter hp_offset.0.weight.\n",
            "Drop parameter hp_offset.0.bias.\n",
            "Drop parameter hp_offset.2.weight.\n",
            "Drop parameter hp_offset.2.bias.\n",
            "Drop parameter base.pre_hm_layer.0.weight.\n",
            "Drop parameter base.pre_hm_layer.1.weight.\n",
            "Drop parameter base.pre_hm_layer.1.bias.\n",
            "Drop parameter base.pre_hm_layer.1.running_mean.\n",
            "Drop parameter base.pre_hm_layer.1.running_var.\n",
            "Drop parameter base.pre_hm_layer.1.num_batches_tracked.\n",
            "out_name test4.mp4\n",
            ": cannot connect to X server \n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}