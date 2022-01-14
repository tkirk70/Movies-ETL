def extract_transform_load():
    # 2. Read in the kaggle metadata and MovieLens ratings CSV files as Pandas DataFrames.
    kaggle_metadata = pd.read_csv(kaggle_file, low_memory=False)
    ratings = pd.read_csv(ratings_file)

    # 3. Open the read the Wikipedia data JSON file.
    with open(wiki_file, mode='r') as file:
        wiki_movies_df = json.load(file)
    
    # 4. Read in the raw wiki movie data as a Pandas DataFrame.
    wiki_movies_df = pd.DataFrame(wiki_movies_df)   
    # 5. Return the three DataFrames
    return wiki_movies_df, kaggle_metadata, ratings

"""# 6 Create the path to your file directory and variables for the three files. 
file_dir = 'C:/Users/timot/OneDrive/Documents/Ohio State Program/Module 8 - ETL/Challenge'
# Wikipedia data
wiki_file = f'{file_dir}/wikipedia-movies.json'
# Kaggle metadata
kaggle_file = f'{file_dir}/movies_metadata.csv'
# MovieLens rating data.
ratings_file = f'{file_dir}/ratings.csv'"""