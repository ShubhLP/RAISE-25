import os
import csv
import ast
import re
import string
import sys
import openai
import pandas as pd
import numpy as np
import tiktoken

def classify_text_with_llm(text, model):
    
    prompt = f"""
    Please classify the following text into either 'utopia' or 'dystopia'.

    Text: {text}

    Return only one word: either 'utopia' or 'dystopia'.
    """

    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that classifies text."},
            {"role": "user", "content": prompt.strip()}
        ],
        temperature=0  # lower temperature for more deterministic answers
    )
    classification = response.choices[0].message.content.strip().lower()
    
    # handles removing extra reponse test, bias towards uptopia
    if "utopia" in classification:
        return "utopia"
    elif "dystopia" in classification:
        return "dystopia"
    else:
        return "utopia"

def ai_detection_llm(text, model):
    
    prompt = f"""
    You are an AI detection tool that reviews text and determines if a human wrote it or an AI.

    Please classify the following text into either 'AI' or 'human'.

    Text: {text}

    Return only one word: either 'AI' or 'human'.
    """

    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that classifies text."},
            {"role": "user", "content": prompt.strip()}
        ],
        temperature=0  # lower temperature for more deterministic answers
    )
    classification = response.choices[0].message.content.strip().lower()
    
    # handles removing extra reponse test, bias towards uptopia
    if "AI" in classification:
        return "AI"
    elif "human" in classification:
        return "human"
    else:
        return "human"

def get_embedding_matrix(path):
    
    df = pd.read_csv(path)
    df['embedding'] = df['embedding'].apply(ast.literal_eval)
    
    return df

def make_embeddings(df, encoding_name, model):
    
    encoding = tiktoken.get_encoding(encoding_name)
    new_rows = []

    for idx, row in df.iterrows():
        text = row["text"]  # entire row text
        new_row = row.copy()
        
        # track the token count
        new_row["n_tokens"] = len(encoding.encode(text))

        response = openai.embeddings.create(
            input=[text],
            model=model)
        
        embedding = response.data[0].embedding
        new_row["embedding"] = embedding
        new_rows.append(new_row)

    df_expanded = pd.DataFrame(new_rows)
    df_expanded = df_expanded.dropna(how="all")
    
    return df_expanded

def run(
    csv_path,
    classification_model="gpt-4o",
    embedding_model="text-embedding-ada-002",
    encoding="cl100k_base",
    output_history_path="../../search/history.csv",
    output_embedding_path="../../search/embedding_history.csv"):
    
    df = pd.read_csv(csv_path, encoding="unicode_escape")
    df["classification"] = df["title"].apply(lambda x: classify_text_with_llm(str(x), model=classification_model))
    df["ai_detection"] = df["title"].apply(lambda x: ai_detection_llm(str(x), model=classification_model))
    df.to_csv(output_history_path, index=False)

    # create single text field for embedding
    df["text"] = df.apply(
        lambda row: (
            f"Date: {row['date']} | Title: {row['title']} "
            f"| Source: {row['source']} | Classification: {row['classification']}"
        ),
        axis=1
    )

    df_embedded = make_embeddings(df, encoding, embedding_model)
    df_embedded.to_csv(output_embedding_path, index=False)

    return df_embedded

if __name__ == "__main__":

    # dataset
    csv_path = r"../../files/Dataset_10k.csv"
    df_embedded = run(csv_path)
    print("Done. Classified data saved and embedded data saved.")

