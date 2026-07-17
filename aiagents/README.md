# Test Case Generator AI Agent

Reads an ADO user story (title, description, acceptance criteria, discussion
comments) and generates prioritised test cases covering **business**,
positive, negative and edge scenarios. Output columns: Test Case Number,
Test Case Title, Test Case Steps, Expected Result.

## Setup
```powershell
pip install -r aiagents/requirements.txt
copy aiagents\.env.example aiagents\.env   # then fill in your secrets
```

## Run
```powershell
# generate + preview + CSV
python aiagents/run_agent.py --story 12345

# also create the test cases in ADO (PAT needs Read & Write on Work Items)
python aiagents/run_agent.py --story 12345 --push
```

## Agent 2: Playwright POM Script Generator
Converts the generated test cases into Playwright (Python) scripts following
the Page Object Model. Each test is isolated and ends with a unique
`expect(...)` assertion. Locators centralised in page classes with priority:
`get_by_role` > `get_by_test_id` > `get_by_label` > `get_by_placeholder` >
`get_by_text` > CSS/XPath.

```powershell
# chain: ADO story -> test cases -> Playwright POM scripts
python aiagents/run_playwright_agent.py --story 12345

# or from a saved test cases JSON
python aiagents/run_playwright_agent.py --from-json testcases.json --title "Login"
```
Generated files go to `PlaywrightFramework/pageobjects/generated/` and
`PlaywrightFramework/tests/generated/`.

## Files
- `config.py` - env-based settings (no hardcoded secrets)
- `ado_client.py` - reads story/comments, writes Test Case work items
- `test_case_agent.py` - LLM prompt + generation (business-first)
- `formatter.py` - Markdown + CSV output in the required columns
- `run_agent.py` - CLI entry point (test cases)
- `playwright_agent.py` - converts test cases to Playwright POM code
- `run_playwright_agent.py` - CLI entry point (Playwright scripts)

