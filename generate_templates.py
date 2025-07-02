from generate_outline_template import LLOutlineTemplate,MLOutlineTemplate,HLOutlineTemplate,VHLOutlineTemplate
from generate_research_template import LLResearchTemplate,MLResearchTemplate,HLResearchTemplate,VHLResearchTemplate
import os
import shutil
import filecmp

list_number=0

#Forces every research and outline template to change.
force_regenerate=False

'''EDIT SECTION'''

def generate_templates(question_file,question_folder):
    total_pictures=10
    total_videos=5

    topic=question_file
    topic=topic.replace(".txt","")
    topic=topic.replace("_"," ")
    topic=topic.title()

    presentation_file_name="LL Presentation Template.pptx"

    test_version=question_file
    test_version=test_version.replace("_"," ")
    if not topic.upper() in test_version.upper():
        print(topic,test_version)
        print("WARNING: NAME AND TOPIC DO NOT MATCH")
        confirmation=input("Are you sure you want to proceed? Enter y for yes. ")
        if "y" in confirmation:
            print("Proceeding")
        else:
            return

    '''END OF EDIT SECTION'''
    questions=[]
    with open(f"{question_folder}/{question_file}","r") as f:
        lines=f.readlines()
        for i in range(len(lines)):
            line=lines[i]
            line=line.strip()
            line=line.replace("\n","")
            questions.append(line)
    
    start_folder="Python_Generated"
    topic=topic.replace("-"," ")
    topic=topic.replace("_"," ")
    topic_plusgenerated=f"({start_folder}) {topic} Organized"
    print(f"Overwriting {start_folder}/{topic_plusgenerated}")

    if os.path.exists(f"{start_folder}/{topic_plusgenerated}"):
        shutil.rmtree(f"{start_folder}/{topic_plusgenerated}")
    else:
        os.mkdir(f"{start_folder}/{topic_plusgenerated}")

    levels=["LL","ML","HL","VHL"]
    for level in levels:
        folder_name=f"{start_folder}/{topic_plusgenerated}/{topic} {level}"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

            #Copy presentation file to each folder
            shutil.copy(presentation_file_name,f"{folder_name}/Part 3 - {presentation_file_name}")

    folder_name=f"{start_folder}/{topic_plusgenerated}/{topic} LL"
    print("Generating",folder_name)
    research_ll=LLResearchTemplate("LL",topic,total_pictures,total_videos,questions,folder_name)
    research_ll.generate_research_documents()

    folder_name=f"{start_folder}/{topic_plusgenerated}/{topic} ML"
    print("Generating",folder_name)
    research_ml=MLResearchTemplate("ML",topic,total_pictures,total_videos,questions,folder_name)
    research_ml.generate_research_documents()

    folder_name=f"{start_folder}/{topic_plusgenerated}/{topic} HL"
    print("Generating",folder_name)
    research_hl=HLResearchTemplate("HL",topic,total_pictures,total_videos,questions,folder_name)
    research_hl.generate_research_documents()

    folder_name=f"{start_folder}/{topic_plusgenerated}/{topic} VHL"
    print("Generating",folder_name)
    research_vhl=VHLResearchTemplate("VHL",topic,total_pictures,total_videos,questions,folder_name)
    research_vhl.generate_research_documents()


    folder_name=f"{start_folder}/{topic_plusgenerated}/{topic} LL"
    print("Generating",folder_name)
    outline_ll=LLOutlineTemplate("LL",topic,total_pictures,total_videos,questions,folder_name)
    outline_ll.generate_outline_documents()

    folder_name=f"{start_folder}/{topic_plusgenerated}/{topic} ML"
    print("Generating",folder_name)
    outline_ml=MLOutlineTemplate("ML",topic,total_pictures,total_videos,questions,folder_name)
    outline_ml.generate_outline_documents()

    folder_name=f"{start_folder}/{topic_plusgenerated}/{topic} HL"
    print("Generating",folder_name)
    outline_hl=HLOutlineTemplate("HL",topic,total_pictures,total_videos,questions,folder_name)
    outline_hl.generate_outline_documents()

    folder_name=f"{start_folder}/{topic_plusgenerated}/{topic} VHL"
    print("Generating",folder_name)
    outline_vhl=VHLOutlineTemplate("VHL",topic,total_pictures,total_videos,questions,folder_name)
    outline_vhl.generate_outline_documents()

def main():
    #If the file_names are too long, there are issues with finding the files
    dirs=["questions/original_topics","questions/new_topics"]
    for dir in dirs:
        for question_file in os.listdir(dir):
            start_location=f"{dir}/{question_file}"
            end_location=f"stored_questions/{question_file}"
            generating=False

            #If there is not an end file, update the soft skills research
            if not os.path.exists(end_location):
                generating=True

            #If the questions have been modified, update the soft skills research
            elif not filecmp.cmp(start_location,end_location,shallow=False):
                generating=True

            #Regenerate EVERYTHING if force_regenerate is true
            if force_regenerate:
                generating=True

            if generating:
                print(question_file)
                generate_templates(question_file,dir)
                #Copy the file in the questions folder to the stored questions folder.
                shutil.copy(f"{start_location}",end_location)
    print("Soft Skills Assignment Generation Complete")

if __name__=="__main__":
    main()