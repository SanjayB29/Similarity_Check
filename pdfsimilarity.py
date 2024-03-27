import difflib
import sys
import fitz  # PyMuPDF

def read_text_from_file(file_path):
    if file_path.lower().endswith('.pdf'):
        text = ''
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
    else:
        with open(file_path, 'r') as file:
            text = file.read()
    return text

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

    # Highlight the similar text
    # print("Similar Text Segments:")
    # for match in matcher.get_matching_blocks():
    #     # match is a namedtuple with attributes a, b, and size
    #     if match.size > 0:
    #         start_a, start_b, size = match
    #         similar_segment = file1_contents[start_a:start_a + size]
    #         print(f"File1 ({start_a}-{start_a + size}): {similar_segment}\nFile2 ({start_b}-{start_b + size}): {similar_segment}\n")

if __name__ == "__main__":
    file1_path = r"Research_on_Algorithms_for_Differential_Graphical_Game_and_Distributed_Nash_Equilibrium_in_Continuous_Systems.pdf"  # Update these paths as necessary, e.g., to PDF files
    file2_path = r"Research_on_Algorithms_for_Differential_Graphical_Game_and_Distributed_Nash_Equilibrium_in_Continuous_Systems.pdf"
    
    calculate_similarity(file1_path, file2_path)
