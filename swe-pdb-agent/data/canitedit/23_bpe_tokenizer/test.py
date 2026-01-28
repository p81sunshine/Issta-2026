from solution import *
import math

def test_all():
    training_set = "Think slow when you write in ink"
    trainer0 = BPETokenizerTrainer(training_set=training_set, max_num_merges=250, max_num_tokens=100)
    assert len(trainer0.get_lookup_table()) == 15

    assert "in" not in trainer0.get_lookup_table()
    trainer0.add_next_pair()
    assert len(trainer0.get_lookup_table()) == 16
    assert "in" in trainer0.get_lookup_table()
    trainer0.merge("in")
    assert len(trainer0.get_lookup_table()) == 16

    assert "ink" not in trainer0.get_lookup_table()
    trainer0.add_next_pair()
    assert len(trainer0.get_lookup_table()) == 17
    assert "ink" in trainer0.get_lookup_table()
    trainer0.merge("ink")
    assert len(trainer0.get_lookup_table()) == 17

    assert " w" not in trainer0.get_lookup_table()
    trainer0.add_next_pair()
    assert len(trainer0.get_lookup_table()) == 18
    assert " w" in trainer0.get_lookup_table()
    trainer0.merge(" w")

    trainer1 = BPETokenizerTrainer(training_set=training_set, max_num_merges=5, max_num_tokens=100)
    assert set(trainer1.get_lookup_table().keys()) == set([c for c in training_set])
    trainer1.train()
    assert set(trainer1.get_lookup_table().keys()) == set([c for c in training_set] + ["in", "ink", " w", "Th", "Think"])

    trainer2 = BPETokenizerTrainer(training_set=training_set, max_num_merges=5, max_num_tokens=10)
    assert set(trainer2.get_lookup_table().keys()) == set([c for c in training_set[:10]])
    trainer2.train()
    assert set(trainer2.get_lookup_table().keys()) == set([c for c in training_set[:10]])

    trainer3 = BPETokenizerTrainer(training_set=training_set, max_num_merges=100, max_num_tokens=18)
    assert set(trainer3.get_lookup_table().keys()) == set([c for c in training_set])
    trainer3.train()
    assert set(trainer3.get_lookup_table().keys()) == set([c for c in training_set] + ["in", "ink", " w"])