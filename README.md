# CSV to FASTA Converter

This script converts a CSV file containing protein sequences into a FASTA file format. The CSV file is expected to have specific column headers (`protein_id` and `seq.text`), and the output is a FASTA file suitable for sequence analysis.

## Features
- Reads a CSV file with columns:
  - `protein_id`: A unique identifier for each protein.
  - `seq.text`: The sequence of the protein.
- Outputs a FASTA file where each protein is represented in FASTA format.

## Requirements
This script requires Python 3 and the following standard library modules:
- `csv`
- `argparse`

No additional dependencies are required.

## Usage

### Command Line

Run the script directly from the command line by specifying the input CSV file and the desired output FASTA file:

```bash
python csv_to_fasta.py <csv_file> <fasta_file>
```

#### Positional Arguments
- `<csv_file>`: Path to the input CSV file.
- `<fasta_file>`: Path to the output FASTA file.

### Example
Given a CSV file `proteins.csv` with the following content:

```csv
protein_id,seq.text
P12345,MKAILVVLLYTQGMLAKAFS
P67890,MTMDKSELVQKAKLAEQAERY
```

Run the script:

```bash
python csv_to_fasta.py proteins.csv proteins.fasta
```

The output FASTA file `proteins.fasta` will contain:

```fasta
>P12345
MKAILVVLLYTQGMLAKAFS
>P67890
MTMDKSELVQKAKLAEQAERY
```

## Function Details

### `csv_to_fasta(csv_file, fasta_file)`
This function reads the CSV file, processes each row, and writes the FASTA format to the output file.

#### Parameters
- `csv_file`: Path to the input CSV file.
- `fasta_file`: Path to the output FASTA file.

## Error Handling
- Ensure the CSV file exists and is formatted correctly with the required headers (`protein_id` and `seq.text`).
- The script will overwrite the specified output FASTA file if it already exists.

## License
This script is released under the MIT License.

## Author
Maximilian Boehm

(The README.md was generated with the help of ChatGPT)
