
#!/bin/bash
# Bash script to run the resolution algorithm for all test cases

# Define the input and output directories
INPUT_DIR="INPUT"
OUTPUT_DIR="OUTPUT"

# Check if the input directory exists
if [ ! -d "$INPUT_DIR" ]; then
  echo "Input directory $INPUT_DIR does not exist."
  exit 1
fi

# Create the output directory if it does not exist
if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir $OUTPUT_DIR
fi

# Run the main.py script for each input file
for input_file in $INPUT_DIR/*.txt; do
  # Run the main.py Python script
  python main.py "$input_file" "$OUTPUT_DIR"
done

echo "Resolution hoàn thành. Hãy kiểm tra các $OUTPUT_DIR files."
