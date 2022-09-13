import argparse

from pepe_semantics.inference import get_giphy_links


def main(input_text):
    giphy_links = get_giphy_links(input_text)
    print(giphy_links)

def _parse_args():
    parser = argparse.ArgumentParser(description="Returns relevant gif links in addition to texts")
    parser.add_argument("-i", "--input-text", required=True, help="Input text")
    parser.add_argument("-k", "--top-k", required=False, default=5, help="Top-k links to return")
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    main(input_text=args.input_text)
