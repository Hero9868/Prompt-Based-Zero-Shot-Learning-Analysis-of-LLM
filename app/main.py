import inspect
import textwrap
from collections import OrderedDict

import streamlit as st
import options

st.set_page_config(
    page_title="Prompt Based Zero Shot Learning Analysis of Large Language Models",
    page_icon="📚",
    initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
)

st.title("Prompt Based Zero Shot Learning Analysis of Large Language Models")
st.subheader("About the Project")
'We created a user-friendly developer platform and provide api for the same to show how prompt based learning, which is a zero shot learning approach for large language models, can optimize for trivial tasks and find an appropriate response given a suitable prompt. This will help us automate trivial generation tasks which normally need human input in them.'
st.markdown("""
- Github Repository for all the code can be found [here](github link here)
- Know more about the project with this [presentation](GDrive Link here)
- Project proposal can be found [here](Google Doc Link Here)

---

""")

OPTIONS = OrderedDict(
    [
        ("—", (options.intro, None)),
        (
            "Option A",
            (
                options.option_a,
                """
                Description
""",
            ),
        ),
        (
            "Option B",
            (
                options.option_b,
                """
                Description
""",
            ),
        ),
        (
            "Option C",
            (
                options.option_c,
                """
                Description
""",
            ),
        ),
    ]
)


def run():
    option_name = st.sidebar.selectbox("Select an Option", list(OPTIONS.keys()), 0)
    demo = OPTIONS[option_name][0]

    if option_name == "—":
        show_code = False
    else:
        show_code = st.sidebar.checkbox("Show code", False)
        st.markdown("# %s" % option_name)
        description = OPTIONS[option_name][1]
        if description:
            st.write(description)
        # Clear everything from the intro page.
        # We only have 4 elements in the page so this is intentional overkill.
        for i in range(10):
            st.empty()

    demo()

    if show_code:
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))


if __name__ == "__main__":
    run()