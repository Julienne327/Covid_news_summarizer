# from transformers import BartTokenizer, BartForConditionalGeneration
# import torch
# from transformers import PegasusTokenizer, PegasusForConditionalGeneration

from imports import* 
def generate_summary(long_text):
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

    # model = PegasusForConditionalGeneration.from_pretrained('google/pegasus-xsum')
    # tokenizer = PegasusTokenizer.from_pretrained('google/pegasus-xsum')

    inputs_no_trunc = tokenizer(long_text, max_length=None, return_tensors='pt', truncation=False)


    chunk_start = 0
    chunk_end = tokenizer.model_max_length  # == 1024 for Bart
    inputs_batch_lst = []
    while chunk_start <= len(inputs_no_trunc['input_ids'][0]):
        inputs_batch = inputs_no_trunc['input_ids'][0][chunk_start:chunk_end]  # get batch of n tokens
        inputs_batch = torch.unsqueeze(inputs_batch, 0)
        inputs_batch_lst.append(inputs_batch)
        chunk_start += tokenizer.model_max_length  # == 1024 for Bart
        chunk_end += tokenizer.model_max_length  # == 1024 for Bart

    # generate a summary on each batch
    summary_ids_lst = [model.generate(inputs, num_beams=6, max_length=100, early_stopping=True) for inputs in inputs_batch_lst]

    # decode the output and join into one string with one paragraph per summary batch
    summary_batch_lst = []
    for summary_id in summary_ids_lst:
        summary_batch = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_id]
        summary_batch_lst.append(summary_batch[0])
    summary_all = '\n'.join(summary_batch_lst)
    print(summary_all)
    return summary_all