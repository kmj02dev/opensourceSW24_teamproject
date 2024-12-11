# SPAM Classifier
This project provides the ability to **determine spam emails**.  You can use it by inputting a **title of the email**. 

If it is determined that it is a spam email, it will appear as **spam** or not appears **ham**.

## Project Process
1. Get data containing spam e-mail information
2. Sample data
3. Load BERT models and tokenize data
4. Learn the model based on the data
5. Enter the title of the e-mail with input
6. It will appears the result whether it is spam or not spam

## Required Packages

#### Torch
v 2.5.1
```python
pip install torch
```

#### Scikit-learn
v 1.6.0
```python
pip install scikit-learn
```


#### Transformers (from HuggingFace)
v 4.47.0
```python
pip install transformers
```

#### Pandas
v 2.2.3
```python
pip install pandas
```

## Sample Image
![Sample Image](https://github.com/hyunsy1214/opensourceSW24_teamproject/blob/main/HyunSuYeong/demo.JPG)

## Reference
DATASET: [SPAM dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

DOCUMENT: [HuggingFace Official Document](https://huggingface.co/docs/transformers/index), [Examples Using Transformers](https://github.com/huggingface/transformers)
