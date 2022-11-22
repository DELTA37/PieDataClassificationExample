import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path")
    parser.add_argument("--batch_size", type=int, default=16)
    args = parser.parse_args()
    return args


def train(data_path, batch_size: int):
    pass


if __name__ == "__main__":
    train(**vars(parse_args()))
