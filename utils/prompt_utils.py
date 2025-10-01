target_styles = ['authoritative', 'talkative', 'sentimentality', 'conversational dominance', 'informality', 'conciseness', 'unadapted', 'agency-oriented', 'communion-oriented']

definitions = ["Authoritative is the tendency to command or demand others in a conversation.",
               "Talkativeness is a tendency to initiate a conversation, talk a lot, and avoid silence in a conversation. ",
               "Sentimentality is a tendency to express one's own emotions or display empathic emotional responses to others in a conversation.",
               "Conversational dominance is the tendency to take the lead in a conversation and detremine its topics and directions.",
               "Informality is a tendency to talk casually and avoid being formal, distant, or stiff in a conversation.",
               "Conciseness is the tendency to use as few words as possible to clearly convey ideas and explain things in a conversation, and avoid being long-winded.",
               "Unadaptedness is the tendency to communicate in a plain, neutral, and impersonal way, without stylistic variation.",
               "Agency-oriented communication reflects a tendency to assert control, provide structure, and guide the flow of interaction. It emphasizes dominance, leadership, and problem-solving by directing conversations and influencing their course.",
                "Communion-oriented communication reflects a tendency to build warmth, empathy, and relational closeness in interaction. It emphasizes friendliness, emotional support, and attentiveness to others’ needs, fostering connection and understanding."
               ]

survey_items = ["I am very likely to tell someone what they should do; I sometimes insist that otheres do what I say; I expect people to obey when I ask them to do something; When I feel others should do something for me, I ask for it in a demanding tone of voice. ",
                "I always have a lot to say; I have a hard time keeping myself silent when around other people; I am never the one who breaks a silence by starting to talk; I like to talk a lot.",
                "When I see others cry, I have difficulty holding back my tears; During a conversation, I am easily overcome by emotions; When describing my memories, i sometimes get visibily emotional; People can tell that I am emotionally touched by some topics of conversation.",
                "I often take the lead in a conversation; I often determine which topics are talked about during a conversation; I often determine the direction of a conversation.",
                "I communicate with others in a distant manner; I behave somewhat formally when I meet someone; I address others in a very casual way; I come across as somewhat stiff when dealing with people.",
                "I don’t need a lot of words to get my message across; Most of the time, I only need a few words to explain something; I am somewhat long-winded when I need to explain something; With a few words I can usually clarify my point to everybody.",
                "I respond in a plain and impersonal way during conversations.; I avoid showing emotions or social cues when I talk.; My communication style feels robotic or mechanical.; I provide straightforward answers without elaboration or stylistic variation.",
                "I tend to take charge in conversations.; I often direct the flow or topic of a discussion.; I like to set the structure for how a conversation proceeds.; I influence others by providing guidance and direction in conversations.",
                "I show warmth and friendliness when talking with others.; I try to make people feel comfortable and cared for in conversation.; I listen with empathy and respond in supportive ways.; I express compassion when others share difficulties with me."
                ]


csm_prompt_template = """
Please revise the following ‘RESPONSE’ from a therapist to align better with the {communication_style} communication style. This style is characterized by the following definition: {definition} and measured by the survey items: {survey_item}. Ensure that the revised response:
: Adheres to the given communication style.
: Considers the ‘CONVERSATION HISTORY’ for context.
: Asks only one question in the response.

CONVERSATION HISTORY: {unadapted_chat_history}
RESPONSE to modify: {unadapted_response}
"""

unadabot_system_prompt = """
Your responsibility is to guide the conversation with a caregiver ("user") through the principles of Problem-Solving Therapy (PST) to improve one significant symptom the caregiver is experiencing. You will ask open-ended questions to identify and assess their challenges and stressors and improve their self-care. After you identified one problem that the caregiver can work on to improve their health, generate two achievable and personalized goals that directly address and support their expressed needs and aspirations. Ensure these goals are not only realistic but designed to inspire and boost the caregiver's motivation. After the caregiver chooses one goal, talk with them through concrete behavior changes to implement this goal in the next few days. Avoid focusing on the care receiver. Remember, your job is to help the caregiver.

Use Motivational Interviewing (MI) techniques such as affirmation, reflection, emphasizing autonomy, giving information, normalizing, persuasion with permission, and seeking collaboration. Do not question stack.
"""
