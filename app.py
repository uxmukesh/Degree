
from flask import Flask, render_template, redirect
import xml.etree.ElementTree as ET

app = Flask(__name__)
#========start of Core courses logic handler========#
def get_courses(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    #Get the root node of xml
    root = tree.getroot()
    
    courses = []
    
    # Iterate over each course element
    # Loop through each 'CoreCourses' element in the root XML tree
    for course in root.findall('CoreCourses'):
        # Loop through each 'course' element within the 'CoreCourses' element
        for course in course.findall('course'):
            # Extracting various attributes of the course
            subject = course.find('subject').text
            course_number = course.find('course_number').text
            course_name = course.find('course_name').text
            credit = course.find('credit').text
            course_description = course.find('course_description').text
            
            # Extract rotation details for the course
            for rotation in course.findall('rotation_term'):
                term = rotation.find('term').text
                time_code = rotation.find('time_code').text
            
            # Initialize an empty list to store prerequisites for the course
            prerequisites = []
            
            # Extract prerequisites information if available
            prerequisites_element = course.find('prerequisite')
            if prerequisites_element is not None:
                or_choices = prerequisites_element.findall('or_choice')
                if or_choices:
                    for or_choice in or_choices:
                        and_required = or_choice.findall('and_required')
                        if and_required:
                            for req in and_required:
                                prerequisites.append(req.text)
            rotation_terms = []
            for rotation in course.findall('rotation_term'):
                term = rotation.find('term').text
                time_code = rotation.find('time_code').text
                rotation_terms.append({'term': term, 'time_code': time_code})
            
            # Append extracted course information into the 'courses' list
            courses.append({
                'subject': subject,
                'course_number': course_number,
                'course_name': course_name,
                'credit': credit,
                'term': term,
                'rotation_terms': rotation_terms,
                'time_code': time_code,
                'course_description': course_description,
                'prerequisites': prerequisites
            })

    # Return the list of extracted courses
    return courses
#========End of Core courses logic handler========#
#========start of Electives courses logic handler========#
#Function to handle the ELECTIVES
def get_Electives(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    elective = []
    #========start of Electives logic handler========#
            # Iterate over each course element
    for electives in root.findall('Electives'):
        for course in electives.findall('course'):
            subject = course.find('subject').text
            course_number = course.find('course_number').text
            course_name = course.find('course_name').text
            credit = course.find('credit').text
            course_description = course.find('course_description').text
            # for rotation in course.findall('rotation_term'):
            #     term = rotation.find('term').text
            #     time_code = rotation.find('time_code').text
            prerequisites = []
            # Extract prerequisites
            prerequisites_element = course.find('prerequisite')
            if prerequisites_element is not None:
                or_choices = prerequisites_element.findall('or_choice')
                if or_choices:
                    for or_choice in or_choices:
                        and_required = or_choice.findall('and_required')
                        if and_required:
                            for req in and_required:
                                prerequisites.append(req.text)
            rotation_terms = []
            for rotation in course.findall('rotation_term'):
                term = rotation.find('term').text
                time_code = rotation.find('time_code').text
                rotation_terms.append({'term': term, 'time_code': time_code})

            elective.append({
                'subject': subject,
                'course_number': course_number,
                'course_name': course_name,
                'credit': credit,
                'rotation_terms': rotation_terms,
                'course_description': course_description,
                'prerequisites': prerequisites
            })
    return elective
#========End of Electives logic handler========#
#========start of Math and statistics logic handler========#
#Function to return math and statistics courses
def get_mathAndStatistics(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    math_and_statistics = []
    #========start of Electives logic handler========#
            # Iterate over each course element
    for mathandstat in root.findall('MathandStatistics'):
        #Iterate through different math and statistics courses
        for course in mathandstat.findall('course'):
            #Extracting the content from course array
            subject = course.find('subject').text
            course_number = course.find('course_number').text
            course_name = course.find('course_name').text
            credit = course.find('credit').text
            course_description = course.find('course_description').text
            # for rotation in course.findall('rotation_term'):
            #     term = rotation.find('term').text
            #     time_code = rotation.find('time_code').text
            prerequisites = []
            # Extract prerequisites
            prerequisites_element = course.find('prerequisite')
            #check if the course have prerequisite course
            if prerequisites_element is not None:
                #Iterate through prerequisites 
                or_choices = prerequisites_element.findall('or_choice')
                if or_choices:
                   #loop through choices
                    for or_choice in or_choices:
                        
                        and_required = or_choice.findall('and_required')
                        if and_required:
                            for req in and_required:
                                prerequisites.append(req.text)
            rotation_terms = []
            for rotation in course.findall('rotation_term'):
                term = rotation.find('term').text
                time_code = rotation.find('time_code').text
                rotation_terms.append({'term': term, 'time_code': time_code})

            math_and_statistics.append({
                'subject': subject,
                'course_number': course_number,
                'course_name': course_name,
                'credit': credit,
                'rotation_terms': rotation_terms,
                'course_description': course_description,
                'prerequisites': prerequisites
            })
    return math_and_statistics
#========End of Math and statistics logic handler========#
#========start of Other courses logic handler========#
def get_Othercourses(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    othercourses = []
    
    # Iterate over each course element
    for other in root.findall('OtherCourses'):
        for course in other.findall('course'):
            subject = course.find('subject').text
            course_number = course.find('course_number').text
            course_name = course.find('course_name').text
            credit = course.find('credit').text
            course_description = course.find('course_description').text
            
            prerequisites = []
            # Extract prerequisites
            prerequisites_element = course.find('prerequisite')
            if prerequisites_element is not None:
                or_choices = prerequisites_element.findall('or_choice')
                if or_choices:
                    for or_choice in or_choices:
                        and_required = or_choice.findall('and_required')
                        if and_required:
                            for req in and_required:
                                prerequisites.append(req.text)
            
            rotation_terms = []
            for rotation in course.findall('rotation_term'):
                term = rotation.find('term').text
                time_code = rotation.find('time_code').text
                rotation_terms.append({'term': term, 'time_code': time_code})
                
            othercourses.append({
                'subject': subject,
                'course_number': course_number,
                'course_name': course_name,
                'credit': credit,
                'rotation_terms': rotation_terms,
                'course_description': course_description,
                'prerequisites': prerequisites
            })
                
    return othercourses
#========End of Other courses logic handler========#
#route to restructure the default redirection
@app.route('/')
def redirectDefault():
    return redirect('/umsl/dataparser')
#The first route to handle the parsing of XML 
@app.route('/umsl/dataparser',methods = ['POST','GET'])
def index():
    # Get courses from XML file
    courses = get_courses("course_data.xml")
    elective = get_Electives("course_data.xml")
    math_and_statistics = get_mathAndStatistics("course_data.xml")
    othercourses = get_Othercourses("course_data.xml")
    return render_template('BsCs.html', courses=courses, electives=elective, stat = math_and_statistics, othercourses = othercourses)

@app.route('/umsl/degreeplanner/dashboard', methods = ['POST','GET'])
def displayResults():
    # Get courses from XML file
    courses = get_courses("course_data.xml")
    elective = get_Electives("course_data.xml")
    math_and_statistics = get_mathAndStatistics("course_data.xml")
    othercourses = get_Othercourses("course_data.xml")
    return render_template('dashboard.html', courses=courses, electives=elective, stat = math_and_statistics, othercourses = othercourses)
if __name__ == '__main__':
    app.run(debug=True)
