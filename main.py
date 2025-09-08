import re
from docx import Document

general_details = {}
experience_details = {}

def parse_resume(filename):
    document = Document(filename)

    parsed_tokens = []
    for i in document.paragraphs:
        parsed_tokens.append(i.text)

    parsed_tokens.remove("")

    parse_general_details(parsed_tokens)


def parse_general_details(tokens):

    ### Strict Locations for general details ###
    general_details['fullname'] = tokens[0]
    general_details['title'] = tokens[1]
    general_details['phone'] = tokens[2]
    general_details['email'] = tokens[3]

    general_details['professional_summary'] = tokens[5]

    parse_experience(tokens)

def parse_experience(tokens):

    total_tokens = len(tokens)
    experience_tokens = []
    for i in range(total_tokens):
        if tokens[i] == "EXPERIENCE":
            experience_tokens = tokens[i+1:]
            break



    temp_experience_holder = ""
    experience_points = ""
    # parse points inside each experience section
    for i in experience_tokens:

        if len(i)<80:
            temp_experience_holder += " " +  i
        else:
            experience_points += i
            temp_experience_holder = ""
            experience_details[temp_experience_holder] = experience_points


    print(experience_details)



    pass

# Example usage
if __name__ == "__main__":
    resume_file = "./Nishedh-Resume.docx"  # replace with your file
    parse_resume(resume_file)

