import zipfile
import xml.etree.ElementTree as ET
import os
import pandas as pd

job_roles_to_skills_map = []
main_df = pd.DataFrame({
    0: [],
    1: [],
    2: []
})


def main():
    dirs = [
        './SFw_ICT_Skills Map_Top_5_CCS/1. Strategy and Governance/',
        './SFw_ICT_Skills Map_Top_5_CCS/2. Infrastructure/',
        './SFw_ICT_Skills Map_Top_5_CCS/3. Software and Applications/',
        './SFw_ICT_Skills Map_Top_5_CCS/4. Data and AI/',
        './SFw_ICT_Skills Map_Top_5_CCS/5. Operations and Support/',
        './SFw_ICT_Skills Map_Top_5_CCS/6. Cyber Security/',
        './SFw_ICT_Skills Map_Top_5_CCS/7. Sales and Marketing/',
        './SFw_ICT_Skills Map_Top_5_CCS/8. Product Development/'
    ]

    for dir in dirs:
        traverse_dir(dir)

    # convert to pandas dataframe
    main_df = pd.DataFrame.from_dict(job_roles_to_skills_map)
    print(main_df.shape)
    main_df.columns = ["Track", "Job Role", "TSC", "Minimum Level"]
    print(main_df.head())
    main_df.to_csv("out.csv")


def traverse_dir(dir):
    global main_df
    track = dir.split(" ", 1)[1]
    for filename in os.listdir(dir):
        if "~" in filename:
            continue
        if ".docx" in filename:
            doc = zipfile.ZipFile(dir + filename).read('word/document.xml')
            keyname = filename.replace('Skills Map_', '').replace(
                ' (GSC Top 5).docx', '').replace(" (CCS Top 5)_v3.0", "")
            traverse_file(doc, keyname, track)


def traverse_file(doc, keyname, track):
    root = ET.fromstring(doc)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    t_nodes = root.findall(
        './/w:t', ns)

    text_arr = []
    start_including = False
    for node in t_nodes:
        if node.text == "Technical Skills and Competencies":
            start_including = True
        if start_including:
            text_arr.append(node.text)

    text_arr = text_arr[2:]
    d_to_2d(text_arr, keyname, track)
    return len(text_arr)


def d_to_2d(arr, keyname, track):
    ignore_arr = ["The information contained in this document serves as a guide.",
                  "For a list of Training Programmes available for the ICT sector, please visit: www.skillsfuture.sg/skills-framework/ict",
                  "For a list of Training Programmes available for the ICT sector, please visit: ",
                  "For a list of Training Programmes available for the "
                  "www.skillsfuture.sg/skills-framework/ict",
                  " Skills and Competencies",
                  "Skills and Competencies"
                  "Programme Listing",
                  " available for the ICT sector, please visit: www.skillsfuture.sg/skills-framework/ict",
                  "Programme",
                  " Listing",
                  "For a list of Training ",
                  "Programmes",
                  " (Top 5)",
                  " Skills and Competencies (Top 5)",
                  " available for the ICT sector, please visit: ",
                  "evel 2",
                  "ICT",
                  " sector, please visit: www.skills",
                  "future.sg/skills-framework/ict",
                  "Programme Listing",
                  "www.skillsfuture.sg/skills-framework/ict"
                  ]

    i = 0
    while i < (len(arr) - 1):
        if arr[i] in ignore_arr:
            i += 1
        # dirty data cases
        # case 1: Project Management
        elif arr[i] == "Project" and "Management" in arr[i+1] and "Level" in arr[i+2]:
            job_roles_to_skills_map.append(
                [track, keyname, "Project Management", arr[i+2]])
            i += 3
        # case: Data Visualization
        elif arr[i] == "Data " and "Visualisation" in arr[i+1] and "Level" in arr[i+2]:
            job_roles_to_skills_map.append(
                [track, keyname, "Data Visualisation", arr[i+2]])
            i += 3
        # case 2: Data Analy - tics
        elif arr[i] == "Data Analy" and arr[i+1] == "tics" and "Level" in arr[i+2]:
            job_roles_to_skills_map.append(
                [track, keyname, "Data Analytics", arr[i+2]])
            i += 3
        # case 3: data - sharing
        elif arr[i] == "Data " and arr[i+1] == "Sharing" and "Level" in arr[i+2]:
            job_roles_to_skills_map.append(
                [track, keyname, "Data Sharing", arr[i+2]])
            i += 3
        # case 3: data - ethics
        elif arr[i] == "Data " and arr[i+1] == "Ethics" and "Level" in arr[i+2]:
            job_roles_to_skills_map.append(
                [track, keyname, "Data Ethics", arr[i+2]])
            i += 3
        # case 4: data - governance
        elif arr[i] == "Data " and arr[i+1] == "Governance" and "Level" in arr[i+2]:
            job_roles_to_skills_map.append(
                [track, keyname, "Data Governance", arr[i+2]])
            i += 3
        # case 5: Process Improvement and  - Optimisation
        elif arr[i] == "Process Improvement and " and arr[i+1] == "Optimisation" and "Level" in arr[i+2]:
            job_roles_to_skills_map.append(
                [track, keyname, "Process Improvement and Optimisation", arr[i+2]])
            i += 3
        # case 6: problem solving - a - dvanced
        elif arr[i] == "Problem Solving" and arr[i+1] == "A" and arr[i+2] == "dvanced":
            i += 3
        # case: problem solving - I - ntermediate
        elif arr[i] == "Problem Solving" and arr[i+1] == "I" and arr[i+2] == "ntermediate":
            i += 3
        # case 7: Service Orientation - I - ntermediate
        elif arr[i] == "Service Orientation" and arr[i+1] == "I" and arr[i+2] == "ntermediate":
            i += 3
        # case: Service Orientation - B - asic
        elif arr[i] == "Service Orientation" and arr[i+1] == "B" and arr[i+2] == "asic":
            i += 3
        # case 8: Sense Making - I - ntermediate
        elif arr[i] == "Sense Making" and arr[i+1] == "I" and arr[i+2] == "ntermediate":
            i += 3
        # case 9: Organisational - Analysis
        elif arr[i] == "Organisational" and arr[i+1] == " Analysis" and "Level" in arr[i+2]:
            job_roles_to_skills_map.append(
                [track, keyname, "Organisational Analysis", arr[i+2]])
            i += 3
        # case 10: Security - Administration
        elif arr[i] == "Security " and arr[i+1] == " Administration" and "Level" in arr[i+2]:
            job_roles_to_skills_map.append(
                [track, keyname, "Security Administration", arr[i+2]])
            i += 3
        # case 11: Resource Management - I - ntermediate
        elif arr[i] == "Resource Management" and arr[i+1] == "I" and arr[i+2] == "ntermediate":
            i += 3
        # case: Resource Management - B - asic
        elif arr[i] == "Resource Management" and arr[i+1] == "B" and arr[i+2] == "asic":
            i += 3
        # case 12: Teamwork - B - asic
        elif arr[i] == "Teamwork" and arr[i+1] == "B" and arr[i+2] == "asic":
            i += 3
        # case 8: Sense Making - B - asic
        elif arr[i] == "Sense Making" and arr[i+1] == "B" and arr[i+2] == "asic":
            i += 3
        # case : Data - Analy - tics - - Level X
        elif arr[i] == "Data " and arr[i+1] == "Analy" and arr[i+2] == "tics" and arr[i+3] == " " and "Level" in arr[i+4]:
            job_roles_to_skills_map.append(
                [track, keyname, "Data Analytics", arr[i+4]])
            i += 5
        # case : Data - Analy - tics - - Level X
        elif arr[i] == "Data " and arr[i+1] == "Governance" and arr[i+2] == " " and "Level" in arr[i+3]:
            job_roles_to_skills_map.append(
                [track, keyname, "Data Governance", arr[i+3]])
            i += 4
        # case : Quality - Standards
        elif arr[i] == "Quality " and arr[i+1] == "Standards" and "Level" in arr[i+2]:
            job_roles_to_skills_map.append(
                [track, keyname, "Quality Standards", arr[i+2]])
            i += 3
        # case: System - s - Design
        elif arr[i] == "System" and arr[i+1] == "s" and " Design" in arr[i+2] and "Level" in arr[i+3]:
            job_roles_to_skills_map.append(
                [track, keyname, "Systems Design", arr[i+3]])
            i += 4
        # case: something - Level - digit:
        elif "Level" not in arr[i] and arr[i+1] == "Level " and arr[i+2].isdigit():
            job_roles_to_skills_map.append(
                [track, keyname, arr[i], arr[i+1] + arr[i+2]])
            i += 3
        # fall through cases
        elif "Level" not in arr[i] and "Level" in arr[i+1]:
            job_roles_to_skills_map.append(
                [track, keyname, arr[i], arr[i+1]])
            i += 2
        elif "Level" not in arr[i] and arr[i+1] in ["Basic", "Intermediate", "Advanced"]:
            i += 2
        else:
            job_roles_to_skills_map.append([track, keyname, arr[i], "NA"])
            i += 1

    for item in job_roles_to_skills_map:
        item[3] = item[3].split(",", 1)[0]
        if item[2] == "Global " and item[3] == "NA":
            job_roles_to_skills_map.remove(item)
        if "Level" in item[2] and item[3] == "NA":
            job_roles_to_skills_map.remove(item)

    # Service Level Management
    # Solution Architect
    # evel 2, NA
    # Strategy Implementation
    # IT Governance


if __name__ == '__main__':
    main()
