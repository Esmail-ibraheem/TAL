from transformer_lib.transformer import TransformerBlock, Args, Transformer_model


args = Args(source_vocab_size=10000, target_vocab_size=10000, source_sequence_length=100, target_sequence_length=100)
model = Transformer_model(args)
