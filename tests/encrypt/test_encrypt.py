import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, 3)
    with pytest.raises(TypeError):
        encrypt_message("valorant", "3")

    assert encrypt_message("valorant", 3) == "lav_tnaro"
    assert encrypt_message("valorant", 0) == "tnarolav"
    assert encrypt_message("valorant", 30) == "tnarolav"
