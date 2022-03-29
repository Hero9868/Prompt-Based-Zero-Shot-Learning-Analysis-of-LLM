from get_results import inference

def get_generation(PROMPT):
    return PROMPT + inference(PROMPT)
