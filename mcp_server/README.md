# Lenny's Wisdom MCP Server

An MCP (Model Context Protocol) server providing structured access to wisdom from 20 curated Lenny's Podcast episodes featuring world-class product leaders.

## 🆕 What's New (v2.0)

**5 New Advanced Tools Added:**
1. **Situation-Based Playbooks** - Get curated advice for specific PM challenges
2. **Actionable Insights Filter** - Surface only immediately actionable advice
3. **Compare Perspectives** - See how different leaders approach the same topic
4. **Quote Search by Guest** - Deep-dive into a specific leader's philosophy
5. **Framework Catalog** - Browse all frameworks (DHM, LNO, JTBD, Pre-mortems, etc.)

Now with **9 total tools** to access 280+ insights from 20 product leaders!

## Features

### 🔍 Search Wisdom
Search across 280+ insights from 20 podcast episodes covering product management, growth, leadership, and decision-making.

### 📚 Episode Library
Access detailed insights from guests including:
- **Brian Chesky** (Airbnb) - Product details obsession, founder mode
- **Ben Horowitz** (a16z) - Leadership under pressure, managerial leverage
- **Shreyas Doshi** (Stripe/Twitter) - Pre-mortems, LNO framework, high agency
- **Dan Shipper** (Every) - AI-first operations, compounding engineering
- **Bob Moesta** - Jobs to Be Done framework
- **Dharmesh Shah** (HubSpot) - Culture as product, fighting entropy
- And 14 more product leaders...

### 🛠️ Available Tools (9 Total)

#### Core Search & Discovery

1. **search_wisdom(query, limit=10)**
   - Search across episodes for relevant insights
   - Example: `search_wisdom("growth strategy")`

2. **list_guests()**
   - List all 20 available guests with descriptions

3. **get_episode(episode_id)**
   - Get complete episode details
   - Example: `get_episode("ep-shreyas-doshi")`

4. **search_by_topic(topic, limit=5)**
   - Filter by specific topics
   - Topics: leadership, product-management, growth-marketing, AI-ML, decision-making, hiring, etc.

#### Advanced Tools

5. **get_advice_for_situation(situation, limit=10)** 🆕
   - Get curated advice for specific PM situations
   - Example: `get_advice_for_situation("I'm starting a new role as VP Product")`
   - Returns actionable advice from multiple leaders

6. **get_actionable_insights(topic=None, limit=15)** 🆕
   - Filter for only immediately actionable insights
   - Example: `get_actionable_insights("hiring")`
   - Surfaces practical advice you can implement today

7. **compare_perspectives(topic, guests=None)** 🆕
   - Compare how different leaders approach the same topic
   - Example: `compare_perspectives("leadership", ["Brian Chesky", "Ben Horowitz"])`
   - Shows side-by-side philosophical differences

8. **get_quotes_by_guest(guest_name, topic=None, limit=10)** 🆕
   - Get all quotes from a specific guest
   - Example: `get_quotes_by_guest("Shreyas Doshi", "decision-making")`
   - Deep-dive into a particular leader's philosophy

9. **list_frameworks()** 🆕
   - Catalog all frameworks mentioned across episodes
   - Returns: DHM, LNO, Pre-mortems, JTBD, Eigenquestions, etc.
   - Shows which episodes cover each framework

## Installation

### 1. Install Dependencies

```bash
cd mcp_server
pip install -r requirements.txt
```

### 2. Configure Claude Desktop

Add to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "lennys-wisdom": {
      "command": "python",
      "args": ["/absolute/path/to/LennyWisdom_Phase1_Deliverables/mcp_server/lennys_wisdom_server.py"]
    }
  }
}
```

Replace `/absolute/path/to/` with the actual path on your system.

### 3. Restart Claude Desktop

Quit and reopen Claude Desktop for changes to take effect.

## Usage Examples

Once configured, you can use these tools in Claude Desktop:

### Basic Search & Discovery
```
"Search Lenny's wisdom for insights on product-market fit"
→ Uses search_wisdom() tool

"Show me all episodes about hiring"
→ Uses search_by_topic() tool

"Get the full Shreyas Doshi episode"
→ Uses get_episode() tool

"List all available guests"
→ Uses list_guests() tool
```

### 🆕 Advanced Tools
```
"I'm joining a new company as VP Product, what should I do?"
→ Uses get_advice_for_situation() tool
→ Returns curated advice from multiple leaders

"Show me only actionable insights about hiring"
→ Uses get_actionable_insights() tool
→ Filters for immediately implementable advice

"How do Brian Chesky and Ben Horowitz approach leadership differently?"
→ Uses compare_perspectives() tool
→ Side-by-side comparison of philosophies

"What are all of Shreyas Doshi's quotes about decision-making?"
→ Uses get_quotes_by_guest() tool
→ Deep-dive into specific leader's thinking

"What frameworks are available across all episodes?"
→ Uses list_frameworks() tool
→ Catalog of DHM, LNO, JTBD, Pre-mortems, etc.
```

## Data Structure

Each episode includes:
- **15 key insights** with verbatim quotes and timestamps
- **3-4 key themes** with relevance scores
- **Topics**: leadership, product-management, growth-marketing, AI-ML, etc.
- **Frameworks mentioned**: Pre-mortems, LNO, DHM, JTBD, etc.
- **Actionable flags**: Indicates which insights are immediately applicable

## Episode Coverage (20 Episodes)

1. Brian Chesky - Product details obsession
2. Claire Hughes Johnson - Scaling operations at Stripe
3. Matt Mochary - CEO coaching frameworks
4. Kim Scott - Radical Candor
5. Gibson Biddle - DHM product strategy
6. Shishir Mehrotra - Growth loops (Black/Blue)
7. Shreyas Doshi - Pre-mortems, LNO framework
8. Casey Winters - Kindle vs Fire growth strategies
9. Dan Shipper - AI-first company operations
10. Ben Horowitz - Running towards fear, leadership
11. Camille Fournier - Engineering management
12. Ami Vora - Product leadership at Meta/WhatsApp
13. Deb Liu - Career intentionality, marketplace platforms
14. April Dunford - Positioning frameworks
15. Bob Moesta - Jobs to Be Done
16. Annie Duke - Decision-making under uncertainty
17. Bangaly Kaba - Instagram growth, marketplace dynamics
18. Bret Taylor - Product-led growth, AI integration
19. Drew Houston - Founder mode, Dropbox scaling
20. Dharmesh Shah - HubSpot culture, fighting entropy

## Technical Details

- **Framework**: FastMCP
- **Search**: Simple keyword matching with relevance scoring
- **Output**: Markdown-formatted responses
- **Data Source**: 20 manually extracted JSON files (~320,000 words processed)

## Extraction Metadata

- **Extracted**: February 2026
- **LLM Model**: Claude Sonnet 4.5
- **Total Insights**: 280+ actionable insights
- **Total Frameworks**: 25+ named frameworks
- **Average Episode**: 15,000 words, 15 insights, 4 themes

## License

This MCP server provides access to curated insights from Lenny's Podcast. All original content is copyright of Lenny Rachitsky and respective guests.
