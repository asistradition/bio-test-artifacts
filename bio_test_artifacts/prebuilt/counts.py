import pandas as pd
import os
from bio_test_artifacts._loader import Load

_data_path = os.path.join(os.path.dirname(__file__), "artifacts")

_YEAST_COUNTS_TPM_FILE_NAME = "GSE135430_counts_TPM.tsv"
_YEAST_COUNTS_TPM_CHR01_FILE_NAME = "GSE135430_counts_chr01_TPM.tsv"


def counts_yeast_tpm():
    file = os.path.join(_data_path, _YEAST_COUNTS_TPM_FILE_NAME)

    copied_file = Load.copy_test_file(file)
    return copied_file, pd.read_csv(file, sep="\t", index_col=None)


def counts_yeast_tpm_chr01():
    file = os.path.join(_data_path, _YEAST_COUNTS_TPM_CHR01_FILE_NAME)

    copied_file = Load.copy_test_file(file)
    return copied_file, pd.read_csv(file, sep="\t", index_col=None)