import os
from bio_test_artifacts._loader import Load
_data_path = os.path.join(os.path.dirname(__file__), "artifacts")

_YEAST_CHR01_FASTA_FILE_NAME = "yeast_chr01.fasta"
_YEAST_CHR01_PROTEIN_FASTA_FILE_NAME = "yeast_chr01_protein.fasta"


def fasta_yeast_chr01():
    from bio_test_artifacts.prebuilt._yeast_fasta import _YEAST_CHR01_SEQ, _YEAST_CHR01_HEADER

    copied_file = Load.copy_test_file(os.path.join(_data_path, _YEAST_CHR01_FASTA_FILE_NAME))
    return copied_file, [(_YEAST_CHR01_HEADER, _YEAST_CHR01_SEQ)]


def fasta_protein_yeast_chr01():
    from bio_test_artifacts.prebuilt._yeast_fasta import (_YEAST_CHR01_PROTEIN_1_HEADER, _YEAST_CHR01_PROTEIN_1_SEQ,
                                                          _YEAST_CHR01_PROTEIN_2_HEADER, _YEAST_CHR01_PROTEIN_2_SEQ)

    copied_file = Load.copy_test_file(os.path.join(_data_path, _YEAST_CHR01_PROTEIN_FASTA_FILE_NAME))
    return copied_file, [(_YEAST_CHR01_PROTEIN_1_HEADER, _YEAST_CHR01_PROTEIN_1_SEQ),
                         (_YEAST_CHR01_PROTEIN_2_HEADER, _YEAST_CHR01_PROTEIN_2_SEQ)]
