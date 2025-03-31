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
        <img src="https://media.licdn.com/dms/image/v2/D4E03AQHpkcCWW015MA/profile-displayphoto-shrink_400_400/B4EZQYxBK1GYAk-/0/1735582290987?e=1749081600&v=beta&t=Lu2FL3fN6oK7gub-yRT8A5yphM2MkU5RBEjTlX1uJf8" alt="Profile Picture">
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
    I also built an asteroid dashboard website during the Ascend Hackathon, a 3-day event in LA that brought together talented girls from around the world! 
    Check it out here: 
    <a href="https://astroid-dashboard.streamlit.app" target="_blank" style="color: #4A90E2; text-decoration: underline;">
        AstroAscend
    </a>
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
        "image": "https://npr.brightspotcdn.com/legacy/news/files/2013/11/SarahSolo11-91.jpg"
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
        "image": "data:image/jpeg;base64,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"
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
        "image": "https://static.wixstatic.com/media/2d4825_7f4020de4ed84ab6b14b1514cdf6f645~mv2.jpg/v1/fill/w_591,h_563,al_c,q_80,enc_avif,quality_auto/2d4825_7f4020de4ed84ab6b14b1514cdf6f645~mv2.jpg"
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
        "image": "https://teenstutorteenslawrenceville.weebly.com/uploads/1/3/3/2/133261096/edited/967275336.png?1615341999"
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
        "image": "https://static.wixstatic.com/media/d21506_9d04459aad2b4c8fb2cb0b346a298fdc~mv2.png/v1/fill/w_560,h_266,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/sgclogotransparentcolor1.png"
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
        "image": "https://shopequo.com/cdn/shop/articles/1._anh_bia_2b83c021-34fe-465e-8a3c-520e5c73e9c5.jpg?v=1701595625&width=1600"
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
