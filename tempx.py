import pytest
import glob

# "TRANSFORMERS_VERBOSITY=error python3 -m pytest -n 2 --max-worker-restart=0 --dist=loadfile -s --make-reports=tests tests/models/xlm_roberta/test_tokenization_xlm_roberta.py"
# python3 -m pytest -n 4 --max-worker-restart=1 --dist="loadfile" tests/models/bert/test_modeling_bert.py tests/models/gpt2/test_modeling_gpt2.py tests/models/bart/test_modeling_bart.py tests/models/plbart/test_modeling_plbart.py tests/models/mbart/test_modeling_mbart.py tests/models/t5/test_modeling_t5.py tests/models/big_bird/test_modeling_big_bird.py tests/models/gpt_neox/test_modeling_gpt_neox.py


if __name__ == "__main__":

    import numpy as np
    import torch
    from PIL import Image
    import transformers

    # pytest.main(["-n", "8", "--max-worker-restart", "1", "--dist", "loadfile",  "tests/models/bert/test_modeling_bert.py", "tests/models/gpt2/test_modeling_gpt2.py", "tests/models/bart/test_modeling_bart.py", "tests/models/plbart/test_modeling_plbart.py", "tests/models/mbart/test_modeling_mbart.py", "tests/models/t5/test_modeling_t5.py", "tests/models/big_bird/test_modeling_big_bird.py", "tests/models/gpt_neox/test_modeling_gpt_neox.py"])

    test_list_items = sorted([x for x in glob.glob("tests/models/*/**.py") if "test_" in x])
    tests_to_run = [x for x in test_list_items if "/test_modeling_" in x or "/test_tokenization_" in x]
    # L = sorted([x for x in test_list_items if "/test_modeling_" not in x and "/test_tokenization_" in x])

    # tests_to_run = " ".join(tests_to_run)

    pytest.main(["-n", "8", "--max-worker-restart", "0", "--dist", "loadfile", "-s", "--make-reports", "tests_torch"] + tests_to_run)
