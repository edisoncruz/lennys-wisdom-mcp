# Lenny's Wisdom MCP Server

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green)](https://modelcontextprotocol.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Edison_Cruz-0077B5)](https://www.linkedin.com/in/edisoncruz/)

An MCP (Model Context Protocol) server providing structured access to wisdom from 20 curated Lenny's Podcast episodes featuring world-class product leaders.

---

<p align="center">
  <a href="https://www.lennyspodcast.com/">
    <img src="https://raw.githubusercontent.com/edisoncruz/lennys-wisdom-mcp/main/assets/lennys-podcast-logo_fixed.jpg" alt="Lenny's Podcast" width="300"/>
  </a>
</p>

<h3 align="center">🎙️ Built with transcripts from <a href="https://www.lennyspodcast.com/">Lenny's Podcast</a></h3>

<p align="center">
  <strong>Inspired by Lenny Rachitsky's generous decision to make all 320+ podcast transcripts freely available.</strong><br/>
  <a href="https://www.linkedin.com/posts/lennyrachitsky_here-are-the-full-transcripts-from-all-320-activity-7417011928159629313-am-q/">See his LinkedIn announcement →</a>
</p>

<p align="center">
  <em>This project transforms those transcripts into actionable wisdom accessible directly in your workflow via Claude Desktop.</em>
</p>

---

**Date:** February 9, 2026  
**Status:** MCP with highly adaptable foundation established. The remaining 280 transcripts will be extracted by the end of February 2026.

---

## Why This Matters

We want to **meet users where they are** by making the collective wisdom of Lenny's tech titan guests available in your Claude, ChatGPT, or LLM of choice. 

Instead of generic responses to prompts like *"Look through these transcripts and give me frameworks about product-market fit"* or *"What does Brian Chesky have to say about prioritization?"*, this MCP server **super-powers your LLM** by augmenting its reasoning capabilities with the minds of the most successful leaders in tech.

Ask natural questions. Get specific, actionable advice from world-class PMs—with context, timestamps, and quotes.

---

## Features

### 🔍 Core Tools (4)

- **search_wisdom(query)** - Keyword search across all episodes
- **list_guests()** - Browse all 20 available guests
- **get_episode(episode_id)** - Get full episode details
- **search_by_topic(topic)** - Filter by topic tags

### 🎯 Advanced Tools (5)

- **get_advice_for_situation(situation)** - Get curated advice for specific PM challenges
- **get_actionable_insights(topic)** - Filter for only immediately actionable tactics
- **compare_perspectives(topic, guests)** - Compare how different leaders approach the same topic
- **get_quotes_by_guest(guest_name, topic)** - Deep-dive into a specific leader's philosophy
- **list_frameworks()** - Browse all frameworks (DHM, LNO, JTBD, Pre-mortems, etc.)

### 📚 Episode Library (20 Episodes)

1. **Brian Chesky** (Airbnb) - Founder mode, product obsession
2. **Claire Hughes Johnson** (Stripe COO) - Scaling operations
3. **Matt Mochary** (CEO Coach) - High output management
4. **Kim Scott** - Radical Candor framework
5. **Gibson Biddle** (Netflix VP Product) - DHM framework
6. **Shishir Mehrotra** (Coda CEO) - Growth loops, Eigenquestions
7. **Shreyas Doshi** (Stripe/Twitter) - Pre-mortems, LNO framework
8. **Casey Winters** (Pinterest) - Kindle vs Fire strategies
9. **Dan Shipper** (Every) - AI-first operations
10. **Ben Horowitz** (a16z) - Running towards fear, managerial leverage
11. **Camille Fournier** - Engineering management
12. **Ami Vora** (Meta/WhatsApp) - Product leadership at scale
13. **Deb Liu** (Ancestry CEO) - 30/60/90 onboarding
14. **April Dunford** - Positioning frameworks
15. **Bob Moesta** - Jobs to Be Done
16. **Annie Duke** - Decision-making under uncertainty
17. **Bangaly Kaba** (Instagram) - Growth loops
18. **Bret Taylor** (ex-Salesforce Co-CEO) - Product-led growth
19. **Drew Houston** (Dropbox) - Founder mode, scaling
20. **Dharmesh Shah** (HubSpot) - Culture as product

---

## Installation

### Option 1: Claude Desktop or ChatGPT Desktop

**1. Install the package:**
```bash
pip install -e /path/to/lennys-wisdom-mcp
```

**2. Configure Claude Desktop:**

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%/Claude/claude_desktop_config.json` (Windows):
```json
{
  "mcpServers": {
    "lennys-wisdom": {
      "command": "python",
      "args": ["/path/to/lennys-wisdom-mcp/lennys_wisdom/server.py"]
    }
  }
}
```

**3. Restart Claude Desktop**

### Option 2: Claude Code or Cowork

Claude Code and Cowork automatically detect MCP servers installed via pip:
```bash
pip install -e /path/to/lennys-wisdom-mcp
# MCP server is now available in Claude Code/Cowork
```

---

## Usage Examples
```
"I'm joining a new company as VP Product, what should I do?"
→ get_advice_for_situation() returns curated advice from multiple leaders

"Show me actionable insights about hiring"
→ get_actionable_insights() filters for immediately implementable advice

"How do Brian Chesky and Ben Horowitz approach leadership differently?"
→ compare_perspectives() shows side-by-side comparison

"What frameworks are available?"
→ list_frameworks() catalogs DHM, LNO, JTBD, Pre-mortems, etc.
```

---

## Technical Overview

**Architecture:** FastMCP server with 9 tools accessing 280+ insights from 20 manually extracted episodes (~320,000 words processed)

**Data Format:** JSON files with 15 key insights per episode, including verbatim quotes, timestamps, themes with relevance scores, topic tags, frameworks, and actionable flags

**Search:** Keyword matching with relevance scoring

**Output:** Markdown-formatted responses

**Extracted:** February 2026 using Claude Sonnet 4.5

---

## Contributing

Contributions welcome! Please submit a Pull Request.

---

## Additional Resources

- **[Official Podcast Transcripts](https://github.com/ChatPRD/lennys-podcast-transcripts)** - Full verbatim transcripts of all episodes (maintained by Lenny's co-host)
- **[Lenny's Podcast](https://www.lennyspodcast.com/)** - Subscribe to the podcast
- **[Lenny's Newsletter](https://www.lennysnewsletter.com/)** - Product management insights and advice