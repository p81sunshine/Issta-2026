from solution import *
import math

def test_all():
    class MockTokenizer:
        def __init__(self):
            pass

        def bos_id(self):
            return 1

        def eos_id(self):
            return 2

        def pad_id(self):
            return 0

        def encode_as_ids(self, s):
            return [ord(x) for x in s]

        def decode_ids(self, ids):
            return "".join([chr(x) for x in ids])

    mock_tokenizer = MockTokenizer()
    token_ids = [10, 20, 30]
    expected_tensor = torch.tensor(
        [mock_tokenizer.bos_id(), 10, 20, 30, mock_tokenizer.eos_id()])
    result_tensor = tokens_to_tensor(token_ids, mock_tokenizer)

    assert torch.equal(
        result_tensor, expected_tensor), "BOS and/or EOS tokens were not added correctly."

    assert len(result_tensor) == len(token_ids) + \
        2, "The resulting tensor length is incorrect."

    assert all(result_tensor[1:-1] == torch.tensor(token_ids)
               ), "Input tokens are not correctly positioned."

    data = ["test"]
    test_decoder_dataset = DecoderDatasetImpl(data, mock_tokenizer)
    test_idx = 0
    expected_output = tokens_to_tensor(
        mock_tokenizer.encode_as_ids(data[test_idx]), mock_tokenizer)
    result_output = test_decoder_dataset.__getitem__(test_idx)
    assert torch.equal(
        result_output, expected_output), "__getitem__ did not process the example correctly."

    data = ["input=output"]
    test_encoder_decoder_dataset = EncoderDecoderDatasetImpl(
        data, mock_tokenizer, mock_tokenizer, split="=")
    test_idx = 0
    lhs, rhs = data[test_idx].split("=")
    lhs += "="
    expected_output_lhs, expected_output_rhs = tokens_to_tensor(mock_tokenizer.encode_as_ids(
        lhs), mock_tokenizer), tokens_to_tensor(mock_tokenizer.encode_as_ids(rhs), mock_tokenizer)
    result_lhs, result_rhs = test_encoder_decoder_dataset.__getitem__(test_idx)
    assert torch.equal(result_lhs, expected_output_lhs) and torch.equal(
        result_rhs, expected_output_rhs), "__getitem__ did not split and process input/output correctly."
    data = ["test1", "test2", "test3"]
    decoder_dataset = DecoderDatasetImpl(data, mock_tokenizer)
    assert len(
        decoder_dataset) == 3, "DecoderDatasetImpl length does not match the expected value."

    data_varying_length = ["a", "bb", "ccc"]
    decoder_dataset_varying = DecoderDatasetImpl(
        data_varying_length, mock_tokenizer)
    batch_varying_length = [decoder_dataset_varying[i]
                            for i in range(len(data_varying_length))]
    padded_result_varying = decoder_dataset_varying.collate_fn(
        batch_varying_length)
    assert len(padded_result_varying.shape) == 2, "collate_fn result should have 2 dimensions for batch and sequence length."
    assert padded_result_varying[0].shape[0] == 3

    get1 = decoder_dataset_varying.__getitem__(0)
    get2 = decoder_dataset_varying.__getitem__(1)
    get3 = decoder_dataset_varying.__getitem__(2)

    assert torch.equal(get1, tokens_to_tensor(
        mock_tokenizer.encode_as_ids(data_varying_length[0]), mock_tokenizer))
    assert torch.equal(get2, tokens_to_tensor(
        mock_tokenizer.encode_as_ids(data_varying_length[1]), mock_tokenizer))
    assert torch.equal(get3, tokens_to_tensor(
        mock_tokenizer.encode_as_ids(data_varying_length[2]), mock_tokenizer))

    # encoder-decoder dataset tests
    data = ["ina=outa", "inbb=outbb", "inccc=outccc"]
    encoder_decoder_dataset = EncoderDecoderDatasetImpl(
        data, mock_tokenizer, mock_tokenizer, split="=")
    encoder_decoder_dataset = EncoderDecoderDatasetImpl(
        data, mock_tokenizer, mock_tokenizer, split="=")
    assert len(
        encoder_decoder_dataset) == 3, "EncoderDecoderDatasetImpl length does not match the expected value."

    padded_result = encoder_decoder_dataset.collate_fn(
        [encoder_decoder_dataset[i] for i in range(len(data))])
    assert len(
        padded_result) == 2, "collate_fn result should have 2 tensors for input and output."
    assert len(
        padded_result[0].shape) == 2, "collate_fn result should have 2 dimensions for batch and sequence length."
    assert len(
        padded_result[1].shape) == 2, "collate_fn result should have 2 dimensions for batch and sequence length."
    assert padded_result[0].shape[0] == 8
    assert padded_result[1].shape[0] == 8

    get1 = encoder_decoder_dataset.__getitem__(0)
    get2 = encoder_decoder_dataset.__getitem__(1)
    get3 = encoder_decoder_dataset.__getitem__(2)

    lhs1, rhs1 = data[0].split("=")
    lhs1 += "="
    lhs2, rhs2 = data[1].split("=")
    lhs2 += "="
    lhs3, rhs3 = data[2].split("=")
    lhs3 += "="

    expected_output_lhs1, expected_output_rhs1 = tokens_to_tensor(mock_tokenizer.encode_as_ids(
        lhs1), mock_tokenizer), tokens_to_tensor(mock_tokenizer.encode_as_ids(rhs1), mock_tokenizer)
    expected_output_lhs2, expected_output_rhs2 = tokens_to_tensor(mock_tokenizer.encode_as_ids(
        lhs2), mock_tokenizer), tokens_to_tensor(mock_tokenizer.encode_as_ids(rhs2), mock_tokenizer)
    expected_output_lhs3, expected_output_rhs3 = tokens_to_tensor(mock_tokenizer.encode_as_ids(
        lhs3), mock_tokenizer), tokens_to_tensor(mock_tokenizer.encode_as_ids(rhs3), mock_tokenizer)

    assert torch.equal(get1[0], expected_output_lhs1) and torch.equal(
        get1[1], expected_output_rhs1), "__getitem__ did not split and process input/output correctly."
    assert torch.equal(get2[0], expected_output_lhs2) and torch.equal(
        get2[1], expected_output_rhs2), "__getitem__ did not split and process input/output correctly."
    assert torch.equal(get3[0], expected_output_lhs3) and torch.equal(
        get3[1], expected_output_rhs3), "__getitem__ did not split and process input/output correctly."