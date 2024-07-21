## Running unit tests

Native python:
```
python -m unittest tests/
```

Embedded python (Windows zip file installation method):
```
..\python_embeded\python.exe -m unittest
```


```
Install TORCH:
nvcc --version
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia

`https://pytorch.org/get-started/locally/`

>>> import torch
>>> torch.cuda.is_available()
>>> print(torch.__version__)

```

```
pip3 install --force-reinstall --pre torch torchtext torchvision torchaudio torchrec --extra-index-url https://download.pytorch.org/whl/nightly/cu121


pip install --force-reinstall charset-normalizer==3.1.0
```