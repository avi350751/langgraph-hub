from agent import run_workflow

# Main API function that external tools or systems will call
def call_api(prompt, options, context):
    """
    Executes the create blog agent with the given prompt.

    Args:
        prompt (str): The blog title.
        options (dict): Additional options for future extension (currently unused).
        context (dict): Contextual information (currently unused).

    Returns:
        dict: A dictionary containing the agent's output or an error message.
    """
    try:
        # Run the research agent and get the result
        result = run_workflow(prompt)
        # Wrap and return the result inside a dictionary
        return {"output": result}
    except Exception as e:
        # Handle any exceptions and return an error summary
        return {"output": {"summary": f"Error: {str(e)}"}}

# If this file is run directly, execute a simple test
if __name__ == "__main__":
    print("✅ Testing create blog Agent provider...")
    test_prompt = "Rise of Artificial Intelligence in India"
    result = call_api(test_prompt, {}, {})
    print("Provider executed successfully.")
    print("Provider result - Title: ", result['output']['title'])
    print("Provider result - Outline:\n", result['output']['outline'])