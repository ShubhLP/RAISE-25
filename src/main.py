# custom libraries
from lib import loading, request
import os
import sys
import pandas as pd

def main():
        
        model = "gpt-4o"
        embedding = "text-embedding-ada-002"
        df = loading.get_embedding_matrix('../search/embedding_history.csv')
        token_budget = 3000        
 
        if len(sys.argv) != 2:
            return "Usage: python main.py 'your question'"

        query = sys.argv[1]
        response = request.recommendations(query, df, model, token_budget, embedding, False)
        
        return response

if __name__ == '__main__':
        print(main())


