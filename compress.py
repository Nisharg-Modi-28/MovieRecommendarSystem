import pickle
import gzip

def compress_pickle(input_pkl, output_pkl_gz):
    """
    Compress a pickle file using gzip.

    Parameters:
        input_pkl (str): Path to the input .pkl file
        output_pkl_gz (str): Path to save the compressed .pkl.gz file
    """
    # Read the pickle file
    with open(input_pkl, 'rb') as f_in:
        data = pickle.load(f_in)

    # Write compressed pickle
    with gzip.open(output_pkl_gz, 'wb') as f_out:
        pickle.dump(data, f_out, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"Compressed {input_pkl} -> {output_pkl_gz}")


# Example usage
compress_pickle("similarity.pkl", "similarity_com.pkl.gz")
