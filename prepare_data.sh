wget https://huggingface.co/datasets/simplescaling/s1K-1.1/resolve/main/data/train-00000-of-00001.parquet
python ./data_convert.py
git clone https://github.com/Abel2076/json2binidx_tool.git
cd json2binidx_tool
pip install -r requirements.txt
python3 tools/preprocess_data.py --input ../jsonl_dataset.jsonl --output-prefix ../ \
        --vocab ./rwkv_vocab_v20230424.txt --dataset-impl mmap --tokenizer-type RWKVTokenizer --append-eod