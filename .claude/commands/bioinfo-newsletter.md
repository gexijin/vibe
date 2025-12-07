You are tasked with creating a bioinformatics research newsletter. Follow these steps:

## Step 1: Fetch Blog Content

Read the blog list from `/workspaces/vibe/newsletter/blogs.md` and fetch the most recent posts from these influential bioinformatics blogs:
- Bits of DNA (https://liorpachter.wordpress.com/)
- Opiniomics (http://www.opiniomics.org/)
- Living in an Ivory Basement (http://ivory.idyll.org/blog/)
- Genomes Unzipped (http://www.genomesunzipped.org/)
- Omics! Omics! (https://omicsomics.blogspot.com/)

For each blog, use WebFetch to get the latest content. Ask what topics, papers, or research trends are being discussed.

## Step 2: Launch Content Researcher

Read the content-researcher agent prompt from `/workspaces/vibe/newsletter/agents/content-researcher.md`.

Use the Task tool with subagent_type='general-purpose' to launch the content-researcher agent. Provide the agent with:
1. The full prompt from the content-researcher.md file
2. All the fetched blog content from Step 1

The agent will analyze the blog posts and return structured insights about trending topics, common themes, and high-impact research.

## Step 3: Launch Newsletter Writer

Read the newsletter-writer agent prompt from `/workspaces/vibe/newsletter/agents/newsletter-writer.md`.

Use the Task tool with subagent_type='general-purpose' to launch the newsletter-writer agent. Provide the agent with:
1. The full prompt from the newsletter-writer.md file
2. The research insights from the content-researcher agent
3. Links to the original blog posts and papers

The agent will write a compelling 500-800 word newsletter article and save it to `/workspaces/vibe/newsletter/drafts/` with filename format: `YYYY-MM-DD-topic-name.md`

## Step 4: Save and Report

Ensure the newsletter draft is saved to `/workspaces/vibe/newsletter/drafts/` with a descriptive filename based on the date and topic. Report back to the user with:
- The topics analyzed
- The chosen topic for the newsletter
- The filename where the draft was saved
- A brief preview of the article
