import streamlit as st
st.markdown("""
    <style>
    .underline {
        text-decoration: underline;
    }
    .outline {
        border: 2px solid #2C3539;  
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Set the title of the app with underline

# Add a sidebar for navigation
st.sidebar.title('Navigation')


# Define the sections
sections = ['About Me', 'Projects', 'Contact','Study Materials',]
choice = st.sidebar.selectbox('Select Section', sections)


if choice == 'About Me':
    st.image('Banner.png', use_column_width=True)
    st.markdown('<h3 class="outline">About Me</h3>', unsafe_allow_html=True)

elif choice == 'Projects':
    st.image('pro.png', use_column_width=True)

    st.markdown('<h2 class="outline">Projects</h2>', unsafe_allow_html=True)
    st.write('Showcase your projects here.')
    if choice == 'Projects':
        col1, col2 ,col3 = st.columns(3)

        with col1:
            st.subheader('Power BI Dashboard')
            st.image('EV.png', use_column_width=True)

            st.write("Description of Project:-Developed an interactive dashboard analyzing EV sales trends, market penetration, and top manufacturers. Utilized Power BI for visual insights and strategic decision making.")
            st.write('Project  Link')

            with open("Ev dash.pbix", "rb") as file:
                st.download_button(
                    label="Download Power BI File",
                    data=file,
                    file_name="EV_Sales_Dashboard.pbix",
                    mime="application/octet-stream"
                )

        with col2:
            st.subheader('Power BI Dashboard')
            st.image('FD (1).png', use_column_width=True)
            st.write('Description of Project - “Created a financial dashboard with dummy data to analyze key metrics, trends, and performance. Utilized Power BI for visual insights and strategic planning.”')
            st.write('Project Link')
            with open("FSD.pbix", "rb") as file:
                st.download_button(
                    label="Download Power BI File",
                    data=file,
                    file_name="FSD.pbix",
                    mime="application/octet-stream"
                )

        with col3:
            st.subheader('Power BI Dashboard')
            st.image('Meat Production.png',use_column_width=True)
            st.write('Description of Project - Analyzed global meat production trends. Found chickens lead with 11 billion produced, while geese are least at 75 million. Visualized using Power BI.')
            st.write('Project Link')
            with open("meat production.pbix", "rb") as file:
                st.download_button(
                    label="Download Power BI File",
                    data=file,
                    file_name="Meat.pbix",
                    mime="application/octet-stream"
                )

elif choice == 'Contact':
    st.image('Contact.png', use_column_width=True)

    st.write('LETS CONNECT MY FRIEND')
if choice =='About Me':

    st.image('Siddharth.png', width=400)
    st.markdown('<p style="font-size: 30px; text-align:Left;">Siddharth Choudhary</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <div style="border: 2px solid #008080; padding: 10px; border-radius: 5px;">
            <p>I’m a Data Analyst currently interning at One X Solutions, where I leverage data analytics to drive 
            strategic decision-making. With a background in digital marketing, I have expertise in SEO, 
            social media marketing, and content writing.</p>
            <p><strong>Skills:</strong> Data Scraping, Data Cleaning, Data Analysis, Presentation, Dashboard making, Data Storytelling</p>
            <p><strong>Tools:</strong> MS Excel,MS Powerpoint,Power BI, Python,MY SQL, Streamlit , R Programming ,Scikit Learn </p>
             <p><strong> Post Graduation:</strong> MBA PGPBADS from Bengal Institute of Business Studies</p>
             <p><strong> Under Graduation:</strong> Bachelors of commerce in accountancy & Finance from Calcutta University </p>
             <p><strong> Higher Secondary Education:</strong> Intermediate in Commerce from Senate Public School </p>
             <p><strong> Secondary Education:</strong> 10th from Senate Public School  </p>
            <p><strong> Work Experience:</strong> Digital Marketing Executive in Floating Numbers Digital Solutions from 16/09/2021 to 30/05/2023 </p>

        </div>
        """, unsafe_allow_html=True
    )
    with open("Siddharth Choudhary Cv.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="Siddharth Choudhary Cv.pdf",
            mime="application/pdf"
        )
    # Create a section for certificates
    st.markdown('<h3 class="outline"> Certifications</h2>', unsafe_allow_html=True)

    col1, col2, col3 ,col4 = st.columns(4)

    with col1:
        st.markdown("Python")
        with open("Data_Analysis.pdf", "rb") as file:
            st.download_button(
                label="Download Certificate ",
                data=file,
                file_name="Data_Analysis.pdf",
                mime="application/pdf"
            )

    with col2:
        st.markdown("IIT Kanpur ML Course")
        with open("IIT kanpur Machine Learning.pdf", "rb") as file:
            st.download_button(
                label="Download Certificate ",
                data=file,
                file_name="IIT kanpur Machine Learning.pdf",
                mime="application/pdf"
            )

    with col3:
        st.markdown("Advance Excel & Tableau")
        with open("Advance Excel with Tableau.pdf", "rb") as file:
            st.download_button(
                label="Download Certificate ",
                data=file,
                file_name="Advance Excel with Tableau.pdf",
                mime="application/pdf"
            )
            with col4:
                st.markdown("MySQL")
                with open("sql_basic certificate.pdf", "rb") as file:
                    st.download_button(
                        label="Download Certificate ",
                        data=file,
                        file_name="sql_basic certificate.pdf",
                        mime="application/pdf"
                    )
    st.markdown('<h3 class="outline">Hobbies</h3>', unsafe_allow_html=True)
    st.markdown("<h5>Book Reading</h5>", unsafe_allow_html=True)
    st.markdown("<h5> Photography </h5>", unsafe_allow_html=True)
    st.markdown("<h5> Computer Games </h5>", unsafe_allow_html=True)







if choice == 'Contact':
    st.markdown('<h4 class="outline">EMAIL</h4>', unsafe_allow_html=True)
    st.write('Email: sidchoudhary8981@gmail.com')
    st.markdown('<h4 class="outline">Social Media </h4>', unsafe_allow_html=True)
    st.write('LinkedIn: https://www.linkedin.com/in/siddharth-choudhary-data-analyst/')
    st.markdown('<h4 class="outline">Github</h4>', unsafe_allow_html=True)
    st.write('Github : https://github.com/Sid8981')

elif choice == 'Study Materials':
    st.image('stu.png', use_column_width=True)
    st.markdown('<h2 class="outline">Study Materials</h2>', unsafe_allow_html=True)
    st.write('Here you can find various study materials.')
    st.markdown('<h5 class="outline">EXCEL</h5>', unsafe_allow_html=True)
    with open("ALL EXCEL FORMULAS.pdf","rb") as file:
        st.download_button(
            label="Excel Formulas",
            data=file,
            file_name="Excel_Formulas.pdf",
            mime="application/pdf"
        )
        st.markdown('<h5 class="outline">Data Science</h5>', unsafe_allow_html=True)
        with open("data-science-roadmap.pdf", "rb") as file:
            st.download_button(
                label="Data Science Roadmap",
                data=file,
                file_name="Data Science Roadmap.pdf",
                mime="application/pdf"
            )
            st.markdown('<h4 class="outline">Python</h4>', unsafe_allow_html=True)
            with open("Learn Python In a Week🔥.pdf", "rb") as file:
                st.download_button(
                    label="Learn Python",
                    data=file,
                    file_name="Learn Python In a Week🔥.pdf.pdf",
                    mime="application/pdf"
                )
                with open("matplotlib Plotting Cookbook_ Learn how to create professional scientific plots using matplotlib, with more than 60 recipes that cover common use cases ( PDFDrive ).pdf", "rb") as file:
                    st.download_button(
                        label="Learn Matplotlib",
                        data=file,
                        file_name="Learn matplotlib",
                        mime="application/pdf"
                    )
                    with open(
                            "Python ebook.pdf",
                            "rb") as file:
                        st.download_button(
                            label="Python Ebook",
                            data=file,
                            file_name="Learn PY",
                            mime="application/pdf"
                        )
                        with open(
                                "object_oriented_python_tutorial.pdf",
                                "rb") as file:
                            st.download_button(
                                label="Object Oriented Programming",
                                data=file,
                                file_name="Tab",
                                mime="application/pdf"
                            )
                        st.markdown('<h5 class="outline"> Statistics</h5>', unsafe_allow_html=True)
                        with open(
                                "Naked Statistics- Stripping the Dread from the Data By.Charles Wheelan_urdukutabkhanapk.pdf",
                                "rb") as file:
                            st.download_button(
                                label="Stats",
                                data=file,
                                file_name="Learn Stats",
                                mime="application/pdf"
                            )
                            st.markdown('<h5 class="outline"> MY SQL</h5>', unsafe_allow_html=True)
                            with open(
                                    "Sql Basic to Advanced.pdf",
                                    "rb") as file:
                                st.download_button(
                                    label="My SQL Ebook",
                                    data=file,
                                    file_name="Learn SQL",
                                    mime="application/pdf"
                                )
                                st.markdown('<h5 class="outline"> Data Visualisation</h5>', unsafe_allow_html=True)

                                with open(
                                        "The Power of Visual Storytelling_ How to Use Visuals, Videos, and Social Media to Market Your Brand ( PDFDrive ).pdf",
                                        "rb") as file:
                                    st.download_button(
                                        label="Learn Data Storytelling",
                                        data=file,
                                        file_name="Learn storytelling",
                                        mime="application/pdf"
                                    )



                                    with open("Practical Tableau_ 100 Tips, Tutorials, and Strategies from a Tableau Zen Master ( PDFDrive ).pdf",
                                            "rb") as file:
                                         st.download_button(
                                           label="Tableau Tips",
                                            data=file,
                                            file_name="Tab",
                                            mime="application/pdf"


                                          )
                                         st.markdown('<h5 class="outline">Machine Learning </h5>',
                                                     unsafe_allow_html=True)
                                         with open("2. End-to-End Machine Learning Project.pdf",
                                            "rb") as file:
                                             st.download_button(
                                                     label="ML Project ebook",
                                                      data=file,
                                                       file_name="ML project",
                                                        mime="application/pdf"

                                             )
                                             with open("Hands on Machine Learning with Scikit Learn and TensorFlow.pdf",
                                                       "rb") as file:
                                                 st.download_button(
                                                     label="Hands on ML",
                                                     data=file,
                                                     file_name="ML ",
                                                     mime="application/pdf"

                                                 )


                                             with open("48 Chatgpt Prompt.pdf","rb") as file:
                                                              st.download_button(
                                                       label="GPT prompts",
                                                       data=file,
                                                       file_name="chatgpt",
                                                       mime="application/pdf"
                                                   )
                                             with open("ARTIFICIAL INTELLIGENCE.pdf", "rb") as file:
                                                 st.download_button(
                                                     label="AI Ebook",
                                                     data=file,
                                                     file_name="AI",
                                                     mime="application/pdf"
                                                 )












