from collections import OrderedDict

import streamlit as st
import options

st.set_page_config(
    page_title="Prompt Based Zero Shot Learning Analysis of Large Language Models",
    page_icon="📚",
    initial_sidebar_state="expanded",
)

st.title("Prompt Based Zero Shot Learning Analysis of Large Language Models")
st.subheader("About the Project")
'We created a user-friendly developer platform and provide api for the same to show how prompt based learning, which is a zero shot learning approach for large language models, can optimize for trivial tasks and find an appropriate response given a suitable prompt. This will help us automate trivial generation tasks which normally need human input in them.'
st.markdown("""
- Github Repository for all the code can be found [here](https://github.com/Hero9868/Prompt-Based-Zero-Shot-Learning-Analysis-of-LLM)
- Know more about the project with this [presentation](GDrive Link here)
- Project proposal can be found [here](https://docs.google.com/document/d/1rSNhyRWpjSmNEXDzQejMFar8P2SgH4fe07EfejVUBbk/edit)

---

""")

OPTIONS = OrderedDict(
    [
        ("—", (options.intro, None)),
        (
            "Transpile Python to JavaScript",
            (
                options.option_a,
                """
                Given a python code as input, we will transform it to a javascript code.
                Click on generate once the prompt is suitable to you.
""",
            ),
        ),
        (
            "Explain Word",
            (
                options.option_b,
                """
                Given a word and its meaning, we will explain the word.
                Click on generate once the prompt is suitable to you.
""",
            ),
        ),
        (
            "Catchy Prompt",
            (
                options.option_c,
                """
                Given a prompt, we will generate a catchy headline.
                Click on generate once the prompt is suitable to you.
""",
            ),
        ),
    ]
)


def run():
    option_name = st.sidebar.selectbox("Select an Option", list(OPTIONS.keys()), 0)
    demo = OPTIONS[option_name][0]
    for i in range(10):
        st.empty()

    demo()

if __name__ == "__main__":
    run()