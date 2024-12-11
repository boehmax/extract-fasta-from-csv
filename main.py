import csv
import argparse

def csv_to_fasta(csv_file, fasta_file):
    with open(csv_file, 'r') as csvfile, open(fasta_file, 'w') as fastafile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            fastafile.write(f">{row['protein_id']}\n")
            fastafile.write(f"{row['seq.text']}\n")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert a CSV file to a FASTA file.')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file')
    parser.add_argument('fasta_file', type=str, help='Path to the output FASTA file')

    # Parse arguments
    args = parser.parse_args()

    # Call the function with the provided arguments
    csv_to_fasta(args.csv_file, args.fasta_file)