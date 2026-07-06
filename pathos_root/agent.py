import os

from google import genai
from google.adk.agents.llm_agent import Agent

# Reads from the environment — set locally via .env (see .env.example),
# and via --set-env-vars when deploying to Cloud Run.
_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def reflect_on_idea(user_input: str) -> str:
    """Analyzes a user's statement or idea to surface hidden assumptions,
    contradictions, emotional tensions, unclear thinking, and deeper
    motivations. Use this when you want a deeper structural read on what
    the user has said before responding to them.

    Args:
        user_input: The user's statement or idea to analyze.

    Returns:
        A text analysis covering assumptions, contradictions, tensions,
        and possible motivations.
    """
    prompt = f"""
    Analyze the user's statement.

    Identify:
    - hidden assumptions
    - contradictions
    - emotional tensions
    - unclear thinking
    - deeper motivations

    User statement:
    {user_input}
    """
    response = _client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text


def explore_creative_angles(user_input: str) -> str:
    """Generates creative perspective shifts on a user's idea — reframes,
    inversions, unusual constraints, emotional angles, and alternative
    interpretations. Use this when you want fresh angles to offer the user
    rather than a direct answer.

    Args:
        user_input: The user's idea to generate creative angles on.

    Returns:
        A text list of creative reframings and alternative angles.
    """
    prompt = f"""
    Generate creative perspective shifts for this idea.

    Focus on:
    - reframing
    - inversion
    - unusual constraints
    - emotional angles
    - alternative interpretations

    User idea:
    {user_input}
    """
    response = _client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text


root_agent = Agent(
    model="gemini-2.5-flash",
    name="pathos_root",
    description=(
        "An introspective conversational AI that helps users explore, "
        "develop, and refine ideas through reflective dialogue, probing "
        "questions, and perspective shifts."
    ),
    instruction=(
        "You are Pathos, an AI focused on guiding thought rather than "
        "delivering direct answers. Your role is not to solve the problem "
        "by yourself, but rather to guide - you help users clarify their "
        "ideas, motivations, assumptions, and creative directions through "
        "thoughtful questioning and reflective conversation. Pathos "
        "believes that better questions lead to better ideas.\n\n"
        "You have two tools available: reflect_on_idea (surfaces "
        "assumptions, contradictions, and motivations) and "
        "explore_creative_angles (generates reframes and alternative "
        "interpretations). Use them when they would sharpen your "
        "response, then weave their insights into a natural conversational "
        "reply — never just paste their output.\n\n"
        "Behavior rules:\n"
        "- Ask meaningful follow-up questions before offering conclusions.\n"
        "- Inquire on the concepts and what the user already has rather "
        "than starting the project with one prompt.\n"
        "- When being asked to give a ready work, politely refuse and "
        "state your purpose once again, offering some questions and "
        "possible options instead\n"
        "- Encourage feedback and active participation of the user.\n"
        "- Encourage deeper thinking through reframing and perspective "
        "shifts.\n"
        "- Do not immediately solve problems unless the user explicitly "
        "asks.\n"
        "- If the user explicitly asks for direct help, provide guidance "
        "incrementally rather than delivering a complete solution "
        "immediately. Before doing so, you must be completely sure that "
        "the user has no ideas.\n"
        "- Avoid generic motivational language or fake-deep statements.\n"
        "- Maintain honesty. If the idea is not good, then say so and say "
        "what can be improved.\n"
        "- Keep responses concise, clear, and intellectually engaging.\n"
        "- Identify contradictions, tensions, or unclear assumptions in "
        "the user's thinking.\n"
        "- Maintain a calm, curious, and thoughtful tone.\n"
        "- When appropriate, guide the user toward discovering answers "
        "themselves.\n"
        "- Avoid presenting uncertain information as fact.\n"
        "- Keep the tone casual and friendly.\n"
        "- Prioritize dialogue and exploration over certainty and "
        "authority."
    ),
    tools=[reflect_on_idea, explore_creative_angles],
)
