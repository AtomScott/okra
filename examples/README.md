# [DEMO] Training ImageNet in Pytorch

This is a basic demo of how to use `okra` to train a model on MNIST. 
It is based on the official [Pytorch tutorial](https://github.com/pytorch/examples/tree/main/mnist).

## Requirements

- Make sure `okra` is installed.
- Install PyTorch ([pytorch.org](http://pytorch.org))
- `pip install -r requirements.txt`

The scripts for this demo are run from this folder so cd into it first.
```bash
cd examples/
pwd
# /path/to/okra/examples
```

## Run the official-pytorch example

```bash
python scriptstrain-mnist-official.py
```

The arguments are defined using pythons `argparse` module.

```python
def main():
    # Training settings
    parser = argparse.ArgumentParser(description="PyTorch MNIST Example")
    parser.add_argument(
        "--batch-size",
        type=int,
        default=64,
        metavar="N",
        help="input batch size for training (default: 64)",
    )
    parser.add_argument(
        "--test-batch-size",
        type=int,
        default=1000,
        metavar="N",
        help="input batch size for testing (default: 1000)",
    )
... # find the rest in examples/train-mnist-official.py
```

This results in the following output when `--help` is passed:


```bash
python scriptstrain-mnist-official.py --help

# output
usage: train-mnist-official.py [-h] [--batch-size N] [--test-batch-size N] [--epochs N] [--lr LR] [--gamma M] [--no-cuda] [--dry-run] [--seed S] [--log-interval N] [--save-model]

PyTorch MNIST Example

optional arguments:
  -h, --help           show this help message and exit
  --batch-size N       input batch size for training (default: 64)
  --test-batch-size N  input batch size for testing (default: 1000)
  --epochs N           number of epochs to train (default: 14)
  --lr LR              learning rate (default: 1.0)
  --gamma M            Learning rate step gamma (default: 0.7)
  --no-cuda            disables CUDA training
  --dry-run            quickly check a single pass
  --seed S             random seed (default: 1)
  --log-interval N     how many batches to wait before logging training status
  --save-model         For Saving the current Model
```

As you probably know, arguments can be passed from the command line.

```bash
python scriptstrain-mnist-official.py --batch-size 64 --test-batch-size 1000 --epochs 14 --lr 1.0 --gamma 0.7 --no-cuda --dry-run --seed 1 --log-interval 10 --save-model
```

## Run the okra example

Reproducibility is important for any machine learning project, it is common practice to store configuration arguments in a separate yaml file. 
The yaml file will be loaded and then passed to the necessary functions. 

Unfortunately, yaml files are extremely minimal and do not provide any validation. Also, using yaml files in addition to argparase can be cumbersome because you may need to write a lot of boilerplate code to parse the yaml file.

`okra` handles argparse and yaml configuration seemlessly. All the user needs to is provide a **schema**. 
A schema is just a yaml file where the arguments are defined. It's like arparse's `ArgumentParser` and `add_argument()` but with a yaml file.


For example, to produce the same output as example using argparse, we would create the following schema.

Change this,

```python 
# Argparse example
parser = argparse.ArgumentParser(description="PyTorch MNIST Example")
... 
parser.add_argument(
    "--log-interval",
    type=int,
    default=10,
    metavar="N",
    help="how many batches to wait before logging training status",
)
parser.add_argument(
    "--save-model",
    action="store_true",
    default=False,
    help="For Saving the current Model",
)
```

to this,

```yaml
# okra example
log-interval: 10
    type: int
    default: 10
    metavar: N
    help: how many batches to wait before logging training status
save-model:
    action: store_true
    default: False
    help: For Saving the current Model
```

(See `schemas/mnist.yaml` for the full schema yaml).

Then in the main function, we would call `okra.load_args()` to load the schema and then pass the arguments to the `okra.train()` function.

```python

```bash
python train-mnist-okra.py --help
``` 