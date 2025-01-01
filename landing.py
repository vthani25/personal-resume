import streamlit as st
import os

# Set page configuration
st.set_page_config(page_title="Personal Portfolio", layout="wide")

def load_css(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS file
load_css("styles.css")

# Add the Spline Viewer
spline_html = """
<script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.54/build/spline-viewer.js"></script>
<spline-viewer url="https://prod.spline.design/WUCjPC1jNmp79Mf6/scene.splinecode"></spline-viewer>
"""

st.components.v1.html(spline_html, height=750)

# Add a fade-out effect
st.markdown('<div class="fade-out"></div>', unsafe_allow_html=True)

# Add the profile section
st.markdown(
    """
    <div class="profile-section">
        <img src="https://media.licdn.com/dms/image/v2/D4E03AQHpkcCWW015MA/profile-displayphoto-shrink_400_400/B4EZQYxBK1GYAk-/0/1735582290987?e=1741219200&v=beta&t=WXdydMH38nGWTj1VmoJep16dEDtSdysLmxTz2ZhDNoM" alt="Profile Picture">
        <div class="text">
            <h2>About Me</h2>
            <p>
                Hello! I’m Thanishkka Vijayabaskar, a tech enthusiast, leader, and problem-solver dedicated to making an impact. </p>
            <p> With a strong foundation in programming, web development, and data analysis, I’ve channeled my skills into projects
                that address real-world challenges. Beyond technology, I’ve embraced roles in business and volunteering, where I’ve cultivated a passion for leadership, teamwork, and giving back to the community.  </p>
            <p> When I’m not coding or mentoring, you’ll find me working on math, sketching, playing flute, or playing with my little sister.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Add a fade-out effect
st.markdown('<div class="fade-in"></div>', unsafe_allow_html=True)

# Skills Section
# Add a title
st.markdown(" ")
st.markdown("<h1 style='text-align: center; color: white; text-decoration: underline;'> TECHNICAL SKILLS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>(Hover over the cards & click the buttons to know more!)</p>", unsafe_allow_html=True)
st.markdown(" ")
st.markdown(" ")

# Embed the skills section directly using HTML and CSS
skills_html = """ 
<style>
.skills-section {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    padding: 20px 0;
    margin-top:5px;
}

.skill-card {
    flex: 1 1 200px;  /* Ensure the cards have a flexible width, but at least 200px */
    max-width: 250px;
    min-width: 200px;
    height: 360px;  /* Adjusted height */
    background: #ffffff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
    margin-bottom: 20px;
}

.skill-card:hover {
    transform: translateY(-15px);
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
}

.skill-card img {
    width: 140px;
    height: 140px;
    object-fit: contain;
    margin: 20px auto 10px;
}

.skill-card h3 {
    font-size: 25px;
    color: #333;
    margin: 10px 0;
    font-family: "Fantasy", "Impact";
}

.skill-card p {
    font-size: 16px;
    font-family: "Helvetica", serif;
    color: #555;
    opacity: 0;
    position: absolute;
    bottom: 10px;
    left: 0;
    right: 0;
    text-align: center;
    transition: opacity 0.3s ease;
}

.skill-card:hover p {
    opacity: 1;
}

</style>


<div class="skills-section">
    <div class="skill-card">
        <img src="https://i0.wp.com/junilearning.com/wp-content/uploads/2020/06/python-programming-language.webp?fit=800%2C800&ssl=1" alt="Python">
        <h3>Python</h3>
        <p>Experienced in competitive programming, machine learning, and data visualization</p>
        
    </div>
    <div class="skill-card">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRELunlkyFk5TtyF76yEpHkyvGPOfaDGIXK-A&s" alt="HTML, CSS, JS">
        <h3>Web Development</h3>
        <p>Proficient in building basic web pages with a focus on layout, styling, and interactive elements.</p>
    </div>
    <div class="skill-card">
        <img src="https://blog.mozilla.org/wp-content/blogs.dir/278/files/2016/09/Cybersecurity.png" alt="G Suite">
        <h3>Cybersecurity</h3>
        <p>Gained hands-on experience protecting digital assets and systems from cyber threats</p>
    </div>
    <div class="skill-card">
        <img src="https://miro.medium.com/v2/resize:fit:1200/1*7l5OQaemuQJLuQxYXze38g.jpeg" alt="Microsoft Suite">
        <h3>Google & MS Suite</h3>
        <p>Efficiently use Slides, Powerpoint, Excel, Calendar for document creation and organization.</p>
    </div>
    <div class="skill-card">
        <img src="https://firebearstudio.com/blog/wp-content/uploads/2022/11/1A6kkoOVJVpXPWewg8axc5w.png" alt="Canva">
        <h3>Canva</h3>
        <p>Skilled in designing visually appealing graphics for presentations, events, and promotional materials</p>
    </div>
</div>
"""

# Render the HTML
st.components.v1.html(skills_html, height=400)


# Initialize session state for toggling sections
if "active_section" not in st.session_state:
    st.session_state.active_section = None

# Function to update the active section
def show_section(section):
    st.session_state.active_section = section

col1, col2, col3, col4, col5, col6, col7 = st.columns([2,13,13,13,13,13,2])
with col2:
    if st.button("Click For Python"):
        show_section("Python")

with col3:
    if st.button("Click For Web Development"):
        show_section("Web Development")

with col4:
    if st.button("Click For Cybersecurity"):
        show_section("Cybersecurity")

with col5:
    if st.button("Click For G Suite/MS Suite"):
        show_section("Suites")
with col6:
    if st.button("Click For Canva"):
        show_section("Canva")


st.markdown("</div>", unsafe_allow_html=True)

# Sections to display based on active button
# Sections to display based on active button
if st.session_state.active_section == "Python":
    st.markdown(
        """
            <div class="content-section">
                <h2>Python Achievements</h2>
                <p>I am highly experienced with Python, from mastering data structures to advanced algorithms. 
                I've participated in competitive programming and proudly won <strong>1st place</strong> 
                in the <strong>GA State Programming Challenge</strong>!</p>
                <p>Over time, I became deeply interested in machine learning and began working with libraries 
                like <strong>Pandas</strong>, <strong>Scikit-learn</strong>, and <strong>Seaborn</strong>. 
                These tools have allowed me to clean and analyze data, build machine learning models, and create insightful visualizations.</p>
                <h4 style="color: #555; font-size:16px; text-decoration:underline;">Google Colab Projects</h4>
                <ul>
                    <li><a href="https://colab.research.google.com/drive/1dk0i3AB6RTd4zBZFo_fy5AFW3Qj9b7Ln?usp=sharing" target="_blank">
                    <strong>Smart Cities Visualization</strong></a>: Visualized data of smart cities worldwide and performed data analysis.</li>
                    <li><a href="https://colab.research.google.com/drive/1nJxoCxjiAjl3qAIOUhFxJisV5WPuYKP-?usp=sharing" target="_blank">
                    <strong>Machine Learning Models</strong></a>: Trained machine learning models, analyzed results using metrics, and applied techniques to address overfitting and underfitting.</li>
                </ul>
                <p>In addition, this website was built using <strong>Streamlit</strong>, a Python framework that makes it easy to turn scripts into interactive web apps. 
                Currently, I’m learning <strong>Plotly Dash</strong> to create more advanced and interactive data apps with front-end styling and enhanced graph capabilities.</p>
                <h4 style="color: #555; font-size:16px; text-decoration:underline;">Certificates</h4>
                <div style="display: flex; gap: 20px; flex-wrap: wrap;">
                    <div style="text-align: center;">
                        <img src="https://lh6.googleusercontent.com/RtwxGhgg35WWNLaUp9T0r-uY_PkPge8qBMLUlo-DsrvqXM1a6a134kzriJUHLW1ahnH5axYoDj6HyUqBhKzBcu55wSB9_C-nICfdxfqaG4C37_7mYC7uRkqKDd6vpII7Ig=w1280" 
                        alt="Python Certificate" style="width: 300px; border-radius: 10px;"/>
                        <p>Python Programming Certificate</p>
                    </div>
                    <div style="text-align: center;">
                        <img src="https://lh4.googleusercontent.com/7QFIHzJP-xRTltmPSPa3MNdb6eJMb3r92lLvE_N-5Hl8Ll5NDiHJEy-kbz24L7y18p821oLAgpuVlqjl-7dTgZdUG-inw570BK_4Zj6eaUcJx2Vjp66FxDFPuxDEycLuLQ=w1280" 
                        alt="Machine Learning Certificate" style="width: 300px; border-radius: 10px;"/>
                        <p>Machine Learning Certificate</p>
                    </div>
                </div>
        </div>
        """,
        unsafe_allow_html=True
    )

elif st.session_state.active_section == "Web Development":
    st.markdown(
        """<div class="content-section">
                <h2>Web Development Experience</h2>
                <div class="technologies-highlight" style="background-color: #4A90E2; color: #fff; padding: 15px; border-radius: 8px; margin-bottom: 20px; text-align: center;">
                <h3 style="margin: 0; font-size: 1.5em;">Technologies I Use</h3>
                <p style="margin: 10px 0 0; font-size: 1.2em;">HTML | CSS | JavaScript | Streamlit | MySQL | PHP</p>
            </div>
                <p style="margin-bottom: 15px;">
                    I have a strong foundation in web development, starting with <strong>HTML</strong>, <strong>CSS</strong>, and <strong>JavaScript</strong> 
                    to create responsive and engaging websites. This website, for example, utilizes <strong>Streamlit</strong>, along with HTML and CSS, 
                    to deliver an interactive and visually appealing user experience. Streamlit powers the dynamic functionality of the app, 
                    while HTML and CSS provide structure and style.
                </p>
                <p style="margin-bottom: 15px;">
                    Currently, I’m working on a website which streamlines the process of finding and applying for jobs and internships for teens. I’m learning backend development with <strong>MySQL</strong> 
                    and <strong>PHP</strong> to make the platform dynamic and user-friendly.
                </p>
                <p style="margin-bottom: 15px;">
                    Previously, I developed a demo website for a local business to showcase their services and enhance their brand presence. 
                    This experience taught me the importance of understanding client needs and tailoring solutions to their goals.
                </p>
                <p style="margin-bottom: 0;">
                    Looking ahead, I’m eager to bring more ideas to life, such as apps for personal finance management and professional networking!
                </p>
</div>
            """
        , unsafe_allow_html=True)

elif st.session_state.active_section == "Cybersecurity":
    st.markdown(
        """<div class="content-section">
                <h2>Cybersecurity</h2>
            <p style="margin-bottom: 15px;">
                At the <strong>Ada Lovelace Cybersecurity Hackathon</strong>, I built an interactive game to teach cybersecurity concepts. 
                The game featured stages on <strong>password authentication</strong>, <strong>malware protection</strong>, and <strong>network security</strong>. 
                The game won the <strong>grand prize of $1500</strong>!
            </p>
            <p style="margin-bottom: 15px;">
                I’ve participated in <strong>CyberPatriot</strong>, a national cybersecurity competition, where I have secured vulnerabilities in 
                <strong>Windows</strong> and <strong>Linux</strong> virtual machines.
            </p>
            <p style="margin-bottom: 0;">
                I am currently pursuing a <strong>Cisco Cybersecurity Certification</strong>, which is helping me expand my technical knowledge and 
                prepare for tackling modern cyber threats.
            </p>
        </div>""", unsafe_allow_html=True)

elif st.session_state.active_section == "Suites":
    st.markdown("""
                '<div class="content-section">
                    <h2>Google Suite and Microsoft Suite</h2>
                    <p style="margin-bottom: 15px;">
            I am highly proficient with both <strong>Google Suite</strong> (Docs, Sheets, Slides, Drive, etc.) and <strong>Microsoft Suite</strong> (Word, Excel, PowerPoint). 
            These tools enable me to collaborate effectively, organize information, and produce professional documents and presentations.
                    </p>
                    <p style="margin-bottom: 15px;">
            I frequently use <strong>Google Docs</strong> for collaborative writing, <strong>Sheets</strong> and <strong>Excel</strong> for data organization and analysis, 
            and <strong>PowerPoint</strong>/<strong>Slides</strong> for creating impactful presentations. I also schedule events and keep track of my schedule with 
            <strong>Google Calendar</strong>.
                    </p>
                    <p style="margin-bottom: 15px;">
            One of my most notable achievements was my <strong>Internet of Things (IoT) project</strong>, which earned <strong>First Place</strong> at the 
            <strong>State Tech Fair</strong>. By using <strong>PowerPoint</strong> to effectively visualize complex ideas, I was able to communicate my project's 
            goals, functionality, and outcomes clearly. </p>
            <p>View the demo of the project here: 
            <a href="https://youtu.be/Y7sxgo_uKGA" target="_blank" style="color: #4A90E2;">IoT Project - State Tech Fair Winner</a>
                    </p>
</div>""", unsafe_allow_html=True)

elif st.session_state.active_section == "Canva":
    st.markdown("""'<div class="content-section">
                        <h2>Canva</h2>
                        <p style="margin-bottom: 15px;">
                        I use <strong>Canva</strong> to design visually appealing graphics for presentations, events, and promotional materials, creating marketing visuals and social media content that effectively communicate messages and engage audiences.</p>
                        <p style="margin-bottom: 15px;">
                        Some key projects include:
                        </p>
                        <ul style="margin-bottom: 15px;">
                            <li><strong>FBLA</strong>: Designed flyers and presentations for events like school recruitment (over 400 members!) and a state rack card competition. I also used Canva to create professional presentations for competitive events.</li>
                            <li><strong>Eco Eagles</strong>: As the founder of the Eco Eagles club, I recruited over 80 members and designed flyers and materials to raise awareness about environmental issues, focusing on aesthetics to attract members and convey sustainability messages.</li>
                            <li><strong>Local Library</strong>: Created eye-catching flyers and posters to promote library events and programs, boosting community engagement.</li>
                        </ul>
                        <p style="margin-bottom: 0;">
                            In all my design work, I prioritize elements like <strong>color schemes</strong>, <strong>typography</strong>, and <strong>layout</strong> to ensure visuals are both attractive and functional.
                        </p> </div>'""", unsafe_allow_html=True)


st.markdown(" ")
st.divider()

col1, col2= st.columns([1.5,3])
with col1:
    st.markdown(
    """
    <div class="kaleidoscope-card">
        <h2>✨ A Kaleidoscope of Pursuits ✨</h2>
        <p>Through serving in leadership roles and actively engaging with my community, I’ve gained invaluable insights and skills. 
        Whether it’s exploring business, delving into math, expressing myself through music, volunteering, or celebrating cultural activities, 
        I’m passionate about expanding my horizons and creating new experiences!</p>
        <br>
        <img src="https://cdn-icons-png.flaticon.com/128/14931/14931655.png" alt="Leadership Illustration">
        <br>
        <br>
        <br>
    </div>
    """,
    unsafe_allow_html=True,
)


# Define the data for each organization
organizations = [
    {
        "title": "FBLA",
        "description": """
        As Chapter President of FBLA at South Forsyth Middle School, I spearheaded a strategic recruitment campaign that increased our membership to over 400 members, making it the largest middle school chapter in the state, led chapter meetings, organized sessions for competitive event practice, and sent out daily communication.

        **National Awards**
          - 1st Place in Financial Literacy (2022)
          - 1st Place in Exploring Economics, Business Math (2023)
          - 1st Place in Exploring Business Communications, 6th Place in Digital Citizenship (2024)
          - LEAD Explore and Aspire Certifications

        **State Awards**
          - 1st Place in Business Ethics (2024)
          - 1st Place in Exploring Computer Science (2023)
          - 5th Place in Exploring Technology (2022)

        **Conferences Attended**
        - Summer Leadership Officer Training Session
        - Fall Leadership Conference
        - State Leadership Conference
        - National Leadership Conference
        
        """,
        "image": "https://core-docs.s3.amazonaws.com/calhoun_city_schools_ar/article/image/large_253062c8-a766-4371-854c-5efff0aa894f.jpg"
    },
    {
        "title": "Band",
        "description": """
            <ul>
                <li>Principal Flute Player in Wind Ensemble – Lead weekly sectionals and provide progress reports to the band director</li>
                <li>Concertmaster in middle school – Earned highest score during auditions</li>
                <li>Performed at Music for All National Festival in Indianapolis – A prestigious national event</li>
                <li>Member of the Atlanta Metro Youth Flute Choir (2024)</li>
            </ul>
            <strong>Awards</strong>
            <ul>
                <li>All State Band Alternate (2024) and District 9 Honor Band (2022–2025)</li>
                <li>Director’s Award for Best Musician in the Band (2023, 2024)</li>
                <li>Superior Rating from National Federation of Music Clubs in piano (5 years)</li>
            </ul>
            <p>Music has instilled in me discipline, teamwork, and the power of artistic expression.</p>
        """,
        "image": "https://lh3.googleusercontent.com/iRPS62ReDESSybP_wCeOUaH2OpFTcf42PZfQIFjHlvIjfKyEBtxT1EEOT1IOcKd7mWE4ok-b4O9jH3P2iBOlus_VCu8-v_FgnPOqUnok-XbnkG56o9BtUlZplLGUSXYS6Q=w1280"
    },
    {
        "title": "Math Team",
        "description": """
            <ul>
                <li>1st Place in MATHCOUNTS Regionals (2022–2024) 
                <li>2nd Place statewide in Math Kangaroo (2023)</li>
                <li>Champion of the Local Pi Fight (2022)</li>
                <li>Won 1st Place in multiple MathLeague events held in the county/state level(2019-2023)</li>
                <li>National distinctions:
                    <ul>
                        <li>Noetic National Honor Roll with perfect scores</li>
                        <li>Top 5% in AMC 8</li>
                        <li>AMC 10 Certificate of Achievement</li>
                        <li>MOEMS Team – National Top 2% placement</li>
                    </ul>
                </li>
            </ul>
    Math has taught me the value of persistence, problem-solving, and quick thinking, and it continues to inspire me to strive for excellence.""",
        "image": "https://lh4.googleusercontent.com/HqS0p4l_poGfWE8_kX8v2NfEZz2_VJKNn9SkH0ftH0UWpVWcOR4DAr3_lWbzThZQbwBAP7bJYpDYAULu5nrlBdQ=w1280"
    },
    {
        "title": "Math & AI for Girls",
        "description": """<strong>Participant & Leadership Team Member</strong> in the Math and AI for Girls initiative. 
        <ul>
            <li>Placed in the <strong>top ranks nationally</strong> in the Math and AI for Girls Competition, demonstrating excellence in mathematical problem-solving and AI applications.</li>
            <li>Serve on the competition team, contributing by <strong>creating challenging problem sets</strong> that test critical thinking and foster problem-solving skills.</li>
            <li>Lead <strong>outreach efforts</strong> to promote the competition and encourage participation among young girls in STEM fields.</li>
            <li>Driven by a passion to <strong>bridge the gender gap in STEM</strong>, I aim to create opportunities for girls to excel in fields like mathematics and artificial intelligence.</li>

        </ul>""",
        "image": "https://lh5.googleusercontent.com/cnxM26qLtQrmEfMTX1Ho8ouvsP41CEUxeMLF0PQflsRMuYKtGJwI4AOWQjvMWr3PtGKQPF86sjEKXRJMR9UgZzc90rhQsoU9n6QbMZedkEQSxdOr8Hi208sbAsyc6Zgj1g=w1280"
    },
    {
        "title": "Teens Tutor Teens",
        "description": """<strong>Tutor and Advisor</strong> for Teens Tutor Teens, GA Chapter. 
        <ul>
            <li>Formed a partnership with an organization in Tennessee to serve underpriviledged children</strong>.</li>
            <li>Serve as an <strong>Advisor</strong>, working to <strong>rebuild and improve chapters</strong> across the nation by mentoring leaders and sharing best practices.</li>
            <li>Developed multiple worksheets in <strong>Algebra, Pre-Calculus, and Physics</strong>.</li>
            <li>Tutored global students in math through <strong>one-on-one meetings</strong>.</li>
            <li>Composed monthly outreach emails to <strong>promote the organization</strong>.</li>
            <li>Actively participated in <strong>state and national meetings</strong>.</li>
            
        </ul>""",
        "image": "https://lh6.googleusercontent.com/cL7DO2BstNkN1xwhD_nAmMEUW3biWlmWqh7mh4jjtLKd9--aJccMIY8u8szI7C2ATsxHBDo9XPRZf8WWKQCCo9w=w1280"
    },
    {
        "title": "National Beta",
        "description": """I've been involved with Beta Club since Junior Beta, which is for elementary school students, and I’ve developed a deep passion for volunteering and giving back to my community. As a member of the National Beta Club, I’ve continued to embrace the values of service, leadership, and academic excellence.
        <ul>
                <li>Fundraised thousands of dollars for various charities, including breast cancer awareness, local hospitals, and military support.</li>
                <li>Tutored students in math and science through weekly morning sessions, helping them improve their academic skills.</li>
                <li>Volunteered at local food pantries, enhancing my interpersonal and teamwork skills while giving back to the community.</li>
            </ul>""",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdVMWCMHSMsg7iXypLCYJT9QK3DpIOCNkM7w&s"
    },
    
    {
        "title": "Foreign Languages",
        "description": """
        <strong> German </strong>
        <ul>
            <li>Actively involved in my school's German Club, helping set up events like Oktoberfest and the Christmas Market. </li>
            <li>National German Exam Gold Medalist (April 2024) </li>
            <li>State German Convention: 1st place in Partner Work, Poetry Declamation, Spelling Bee, Vocab Bee, and Banner (December 2023) </li>
        </ul>
        <strong> Tamil </strong>
        <ul>
            <li>Alpharetta Tamil School: Valedictorian and Graduate Diploma (May 2024) </li>
            <li>Seal of Biliteracy (earned in December 2024) </li>
            <li>Volunteer at Alpharetta Tamil School, teaching younger kids and giving back to the community </li> 
            </ul>""",
        "image": "https://lh6.googleusercontent.com/8rlSZOMnEw7GSNCLP-YiD5O6LGIylb-vA0GTINnI5Yzu_D-1kEflXSw3GaB03-6fQmjW7cSiBmbFr-PodpqwLuDNDXx002vSkyP32kt80XKic6XofaKRDRq6qyu2EI3omg=w1280"
    },
    {
        "title": "Eco Eagles",
        "description": """<strong>Co-Founder and President</strong> of Eco Eagles at South Forsyth Middle School 
        <ul>
            <li>Recruited around <strong>100 members</strong> from all grade levels.</li>
            <li>Trained an officer team in managing <strong>social media, school publications, meetings, and events</strong>.</li>
            <li>Secured multiple prestigious <strong>guest speakers</strong> for meetings.</li>
            <li>Collaborated with school administration to <strong>host awareness events</strong>.</li>
            <li>Orchestrated environment-centered debate and <strong>product pitch competitions</strong> with judges and prizes.</li>
            <li>Organized weekly <strong>community service events</strong> at school and promoted local nonprofits.</li>
        </ul>""",
        "image": "https://lh3.googleusercontent.com/jV4471Zz3jshzLh_vCQ09g2JU3p4CFQ0aaMJvWYCCXftMl5JIVSzna18vLbpVeGDhERXQwVngyzwr4wkeRSB33_tZcI9AjX7NQ1IMihoRYpCme4XP0SJ-ZbeYiy5uvoOUA=w1280"
    }
    
]


with col2:
    # Create a list of organization titles for the segmented control
    organization_titles = [org["title"] for org in organizations]

    # Use Streamlit's segmented control to select an organization
    selected_org_title = st.segmented_control(
        label="Select an Organization to Know More About My Involvement!", 
        options=organization_titles,
    )

    # Use 'next' with default value to avoid StopIteration
    selected_org = next(
        (org for org in organizations if org["title"] == selected_org_title), 
        None
    )

    if selected_org:
        col1, col2 = st.columns([1,2])
        with col1:
        # Display organization details in a styled format
            st.markdown(
                f"""
                <div >
                    <img src="{selected_org['image']}" alt="{selected_org['title']} Logo" style="width: 500px; border-radius: 15%; border: 5px solid #1b284f; margin-top: 50px; margin-bottom: 5px;">
                </div>
                """, unsafe_allow_html=True)
        with col2:
            st.markdown(
                f"""
                <div style="
                    background-color: #1b284f;
                    color: white;
                    border-radius: 15px;
                    padding: 20px;
                    margin: 20px 0;
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
                    text-align: left;
                ">
                <h3 style="font-family: 'Cinzel', serif; font-size: 1.8em; margin-bottom: 10px; text-align:center;">{selected_org['title']}</h3>
                <p style="font-size: 1.1em; line-height: 1.6; font-family: 'Open Sans', sans-serif;">{selected_org['description']}</p> </div> """,
                unsafe_allow_html=True
            )


st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.divider()

#contact form
buff1, buff2, col, buff3 = st.columns([1, 1, 3,1])
# Title
with buff2:
    st.markdown('<h2 class="contact-title">CONTACT</h2>', unsafe_allow_html=True)
    st.markdown('<p class="contact-description">My inbox is always open for new opportunities!</p>', unsafe_allow_html=True)
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')

    # GitHub
    st.markdown(
        """
        <div class="icon-text">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
            <a href="https://github.com/yourusername" target="_blank">@vthani25</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Email
    st.markdown(
        """
        <div class="icon-text">
            <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="Email">
            <a href="mailto:your.email@example.com">vthanishkka@gmail.com</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # LinkedIn
    st.markdown(
        """
        <div class="icon-text">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
            <a href="https://www.linkedin.com/in/yourusername" target="_blank">Thanishkka Vijaya Baskar</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col:
    # Form
    with st.form("contact_form", clear_on_submit=True):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        email = st.text_input("Email", placeholder="Your email")
        subject = st.text_input("Subject", placeholder="Your subject")
        message = st.text_area("Message", placeholder="Your message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            if email and subject and message:
                st.success("Your message has been sent!")
            else:
                st.error("Please fill out all the fields!")
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f9f9f9;
            padding: 10px 0;
            text-align: center;
            font-size: 14px;
            color: #6c757d;
        }
        .footer a {
            color: #007bff;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        </style>
        <div class="footer">
            © 2024 Thanishkka Vijayabaskar. All Rights Reserved. | 
            <a href="https://github.com/vthani25" target="_blank">GitHub</a> | 
            <a href="https://www.linkedin.com/in/thanishkka-vijaya-baskar-a95b43297" target="_blank">LinkedIn</a> 
        </div>
        """,
        unsafe_allow_html=True
    )
st.markdown('footer')
