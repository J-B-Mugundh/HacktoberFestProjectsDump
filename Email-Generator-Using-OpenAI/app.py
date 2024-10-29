import streamlit as st
from ml_backend import ml_backend

def main():
    st.title("Email Generator using OpenAI")
    st.text("by Vijai Suria")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Generate Email"])

    if page == "Home":
        st.markdown(""" 
        # Home
        
        This project is done as part of the TNSDC Naanmudhalvan program, Generative AI for Engineering (E2324).
                    
        ### Program Overview:
        
        The Machine Learning to Generative AI program offers an immersive 8-week educational journey aimed at equipping students with modern skills in the rapidly evolving fields of AI and cloud. Through a project-based learning approach, participants will delve into the depths of cutting-edge technologies, enabling them to gain hands-on experience while solving real-world challenges. The program's comprehensive curriculum covers coding principles and advanced learning of various technologies, all culminating in the opportunity to obtain valuable free certificates. By fostering practical expertise and a deep understanding of the subject matter, this program empowers students to excel in the digital era and unlock promising career prospects. 

        
        ### Course Outcome:
        
        Students upon completion of the program will inherit: 
        
        - **Skill Enhancement:** Students learn valuable skills in AI and ML, gaining proficiency in programming, data analysis, and problem-solving, making them more competitive in the job market. 
        
        - **Real-world Applications:** Students understand how AI and ML are used in various industries, connecting theoretical knowledge to practical applications, which enhances their problem-solving abilities. 
        
        - **Critical Thinking:** AI and ML education encourages critical thinking by requiring students to analyse and interpret data, fostering a deeper understanding of the underlying algorithms and models. 
        
        - **Innovation and Creativity:** Students develop a creative mindset as they explore innovative ways to apply AI and ML concepts, leading to the development of new solutions and products. 
        
        - **Adaptability:** Learning AI and ML prepares students for a rapidly changing technological landscape, teaching them to adapt to new tools and methodologies, which is crucial for long-term success in their careers. 
        
                """)
    elif page == "About":
        st.markdown(
        """
        <style>
            @media only screen and (max-width: 600px) {
                .flex-cont {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }
            }
        </style>
        <div class="flex-cont" style="display:flex; margin-top: 36px">
            <div style="flex:1;padding-right:20px;">
                <img src="https://vijaisuria.github.io/vijaisuria.jpg" style="border-radius:50%;width:200px;height:200px;">
            </div>
            <div style="flex:2;">
                <h2>Vijai Suria</h2>
                <h5>Passionate third-year Computer Science Engineering student, adept at merging AI with
                    full-stack expertise to redefine digital experiences and drive technological evolution.</h5>
            </div>
        </div>
        <div style="display:flex; margin-top: 36px">
             <p>Enthusiastic third-year Computer Science Engineering student and IBM Certified Professional Full Stack Developer, driven by a passion for innovation in technology. As an AI enthusiast, I have immersed myself in the realms of creating captivating mobile and web applications. My journey has honed my skills in both front-end and back-end development, enabling me to architect seamless user experiences that resonate with modern demands. With a keen interest in AI and ML, I am actively engaged in AI-ML based projects, aiming to shape the future of digital technologies. Eager to contribute to the ever-evolving landscape of mobile and web development, leveraging my skills and knowledge to drive innovation and transformative experiences.</p>
        </div>
        """,
        unsafe_allow_html=True
        )

        st.markdown("### Contact Links")
        st.markdown("[Portfolio link](https://vijaisuria.github.io/)")
        st.markdown("[LinkedIn Handle](https://www.linkedin.com/in/vijaisuria/)")
        st.markdown("[GitHub profile](https://github.com/vijaisuria)")

    elif page == "Generate Email":
        st.markdown("# Generate Email")

        backend = ml_backend()

        with st.form(key="form"):
            prompt = st.text_input("Describe the Kind of Email you want to be written.")
            st.text(f"(Example: Write me a professional sounding email to my boss)")

            start = st.text_input("Begin writing the first few or several words of your email:")

            slider = st.slider("How many characters do you want your email to be? ", min_value=64, max_value=750)
            st.text("(A typical email is usually 100-500 characters)")

            submit_button = st.form_submit_button(label='Generate Email')

            if submit_button:
                with st.spinner("Generating Email..."):
                    output = backend.generate_email(prompt, start)
                st.markdown("# Email Output:")
                st.subheader(start + output)

                st.markdown("____")
                st.markdown("# Send Your Email")
                st.subheader("You can press the Generate Email Button again if you're unhappy with the model's output")
                
                st.subheader("Otherwise:")
                st.text(output)
                url = "https://mail.google.com/mail/?view=cm&fs=1&to=&su=&body=" + backend.replace_spaces_with_pluses(start + output)

                st.markdown("[Click me to send the email]({})".format(url))

if __name__ == "__main__":
    main()
