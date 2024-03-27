import difflib
import sys

def calculate_similarity(file1_path, file2_path):
    # Read the contents of the first file
    with open(file1_path, 'r') as file1:
        file1_contents = file1.read()

    # Read the contents of the second file
    with open(file2_path, 'r') as file2:
        file2_contents = file2.read()

    # Create a SequenceMatcher
    matcher = difflib.SequenceMatcher(None, file1_contents, file2_contents)

    # Calculate the similarity ratio
    similarity_ratio = matcher.ratio()
    
    # Convert the similarity ratio to a percentage
    similarity_percentage = similarity_ratio * 100
    
    # Print the similarity percentage
    print(f"Similarity: {similarity_percentage:.2f}%\n")

    # Highlight the similar text
    print("Similar Text Segments:")
    for match in matcher.get_matching_blocks():
        # match is a namedtuple with attributes a, b, and size
        if match.size > 0:
            start_a, start_b, size = match
            similar_segment = file1_contents[start_a:start_a + size]
            print(f"File1 ({start_a}-{start_a + size}): {similar_segment}\nFile2 ({start_b}-{start_b + size}): {similar_segment}\n")

if __name__ == "__main__":
    
    
    file1_path = r"a.txt"
    file2_path = r"b.txt"
    
    calculate_similarity(file1_path, file2_path)
