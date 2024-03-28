import difflib
import fitz  # PyMuPDF

def calculate_similarity(file1_path, file2_path):
    # Extract the contents of the files
    file1_contents = read_text_from_file(file1_path)
    file2_contents = read_text_from_file(file2_path)

    # Create a SequenceMatcher
    matcher = difflib.SequenceMatcher(None, file1_contents, file2_contents)

    # Calculate the similarity ratio
    similarity_ratio = matcher.ratio()

    # Convert the similarity ratio to a percentage
    similarity_percentage = similarity_ratio * 100

    # Print the similarity percentage
    print(f"Similarity: {similarity_percentage:.2f}%\n")   
    
def read_text_from_file(file_path):
    """Reads text from a PDF or text file."""
    if file_path.lower().endswith('.pdf'):
        text = ''
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
    else:
        with open(file_path, 'r') as file:
            text = file.read()
    return text

def calculate_directional_similarity(base_contents, comparison_contents):
    """Calculates how much of the base content is found in the comparison content."""
    matcher = difflib.SequenceMatcher(None, base_contents, comparison_contents)
    total_matched = sum(match.size for match in matcher.get_matching_blocks() if match.size > 0)
    return total_matched / len(base_contents) * 100 if len(base_contents) > 0 else 0

if __name__ == "__main__":
    file1_path = r"Understanding and Detecting Software Upgrade Failures in Distributed Systems.pdf"  # Update this path
    file2_path = r"DREAM A Dynamic Scheduler for Dynamic Real-time.pdf"  # Update this path

    file1_contents = read_text_from_file(file1_path)
    file2_contents = read_text_from_file(file2_path)

    calculate_similarity(file1_path, file2_path)
    similarity_percentage_1_to_2 = calculate_directional_similarity(file1_contents, file2_contents)
    similarity_percentage_2_to_1 = calculate_directional_similarity(file2_contents, file1_contents)

    print(f"Percentage of File 1's content found in File 2: {similarity_percentage_1_to_2:.2f}%")
    print(f"Percentage of File 2's content found in File 1: {similarity_percentage_2_to_1:.2f}%")
