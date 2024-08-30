import csv

COLUMN_NAMES = ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"]
OFFSETS = [5, 12, 3, 2, 13, 7, 10, 13, 20, 13]
FIXED_WIDTH_ENCODING = "windows-1252"
DELIMITED_ENCODING = "utf-8"
INCLUDE_HEADER = True

def adjust_field_length(field, length):
    if len(field) > length:
        return field[:length]  # Truncate if the string is too long
    return field.ljust(length)  # Pad with spaces if too short

def generate_fixed_width_file(filename):
    with open(filename, 'w', encoding=FIXED_WIDTH_ENCODING) as f:
        rows = [
            "helloknowledgeispoweroflearningneverststopgrowingenrichyourmindbethechangeyouwanttoseeintheworld",
            "helloiamveryhappyasiamonboardingthedemystpythonjavamachinelearndatabrickssnowflakecloudcomputingremoveiflong"
        ]

        for row in rows:
            position = 0
            adjusted_row = ""
            for offset in OFFSETS:
                field = row[position:position + offset]
                adjusted_row += adjust_field_length(field, offset)
                position += offset
            f.write(adjusted_row + "\n")


def parse_fixed_width_to_csv(input_filename, output_filename):
    with open(input_filename, 'r', encoding=FIXED_WIDTH_ENCODING) as infile, \
         open(output_filename, 'w', newline='', encoding=DELIMITED_ENCODING) as outfile:
        
        writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)
        
        if INCLUDE_HEADER:
            writer.writerow(COLUMN_NAMES)
        
        for line in infile:
            position = 0
            row = []
            for offset in OFFSETS:
                field = line[position:position+offset].strip()
                row.append(field)
                position += offset
            writer.writerow(row)

if __name__ == "__main__":
    generate_fixed_width_file('fixed_width_file.txt')
    parse_fixed_width_to_csv('fixed_width_file.txt', 'output_file1.csv')
