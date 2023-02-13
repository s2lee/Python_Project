import path

from generators_iteration import NumberSequence, SequenceOfNumbers


def test_number_sequence():
    seq = NumberSequence()
    assert seq.next() == 0
    assert seq.next() == 1


def test_sequence_of_numbers():
    seq = list(zip(SequenceOfNumbers(), "abcdef"))
    for i, char in enumerate("abcdef"):
        assert seq[i] == (i, char)
    seq2 = SequenceOfNumbers(100)
    assert next(seq2) == 100
    assert next(seq2) == 101

