import pytest

# "TRANSFORMERS_VERBOSITY=error python3 -m pytest -n 2 --max-worker-restart=0 --dist=loadfile -s --make-reports=tests tests/models/xlm_roberta/test_tokenization_xlm_roberta.py"
# python3 -m pytest -n 4 --max-worker-restart=1 --dist="loadfile" tests/models/bert/test_modeling_bert.py tests/models/gpt2/test_modeling_gpt2.py tests/models/bart/test_modeling_bart.py tests/models/plbart/test_modeling_plbart.py tests/models/mbart/test_modeling_mbart.py tests/models/t5/test_modeling_t5.py tests/models/big_bird/test_modeling_big_bird.py tests/models/gpt_neox/test_modeling_gpt_neox.py


if __name__ == "__main__":
    pytest.main(["-n", "8", "--max-worker-restart", "1", "--dist", "loadfile",  "tests/models/bert/test_modeling_bert.py", "tests/models/gpt2/test_modeling_gpt2.py", "tests/models/bart/test_modeling_bart.py", "tests/models/plbart/test_modeling_plbart.py", "tests/models/mbart/test_modeling_mbart.py", "tests/models/t5/test_modeling_t5.py", "tests/models/big_bird/test_modeling_big_bird.py", "tests/models/gpt_neox/test_modeling_gpt_neox.py"])
