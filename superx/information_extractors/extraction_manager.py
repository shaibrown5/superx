import os
import sys

# adds the path to system so that the script can run
add_to_python_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
sys.path.append(add_to_python_path)

from information_extractors.item_info_extractor import InfoExtractor
from information_extractors.branch_info_extractor import BranchExtractor
from app import session
from models import BranchPrice, Branch, Product


def main():
    b_extractor = BranchExtractor()
    i_extractor = InfoExtractor()

    b_extractor.run_branch_extractor()
    i_extractor.run_info_extractor()

    BranchPrice.query.delete()
    Product.query.delete()
    Branch.query.delete()

    session.commit()


if __name__ == "__main__":
    main()

