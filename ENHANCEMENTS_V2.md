# Lenny's Wisdom MCP Server v2.0 - Enhancement Summary

## 🎉 What's New

We've added **5 powerful new tools** to the Lenny's Wisdom MCP Server, taking it from 4 basic tools to **9 advanced tools** for accessing 280+ insights from 20 world-class product leaders.

---

## 🆕 New Tools Added

### 1. **Situation-Based Playbooks** (`get_advice_for_situation`)

**What it does:** Get curated advice for specific PM situations or challenges

**Example queries:**
- "I'm joining a new company as VP Product, what should I do?"
- "How do I make decisions when both options seem bad?"
- "My product has good retention but slow growth"
- "I need to have a difficult conversation with my team"

**What you get:**
- Relevant advice from multiple product leaders
- Specific quotes and actionable insights
- Context from their experiences
- Prioritizes actionable advice

**Use case:** When you're facing a specific challenge and want to hear from multiple experts on how to handle it.

---

### 2. **Actionable Insights Filter** (`get_actionable_insights`)

**What it does:** Surface only the most practical, immediately actionable advice

**Example queries:**
- `get_actionable_insights()` → All actionable insights
- `get_actionable_insights("hiring")` → Actionable hiring advice
- `get_actionable_insights("growth-marketing")` → Actionable growth tactics

**What you get:**
- Only insights marked as "✅ Actionable"
- Practical advice you can implement today
- Filtered theoretical content

**Use case:** When you want tactics and techniques, not theory. Perfect for "what should I do RIGHT NOW?"

---

### 3. **Compare Perspectives** (`compare_perspectives`)

**What it does:** See how different product leaders approach the same topic

**Example queries:**
- `compare_perspectives("leadership")`
- `compare_perspectives("hiring", ["Ben Horowitz", "Shishir Mehrotra"])`
- `compare_perspectives("product-market fit")`

**What you get:**
- Side-by-side comparison of approaches
- Different philosophies and frameworks
- Multiple perspectives on the same challenge

**Use case:** When you want to see the spectrum of thinking on a topic. Great for understanding trade-offs and different schools of thought.

---

### 4. **Quote Search by Guest** (`get_quotes_by_guest`)

**What it does:** Get all quotes from a specific guest, optionally filtered by topic

**Example queries:**
- `get_quotes_by_guest("Ben Horowitz")`
- `get_quotes_by_guest("Brian Chesky", "leadership")`
- `get_quotes_by_guest("Deb Liu", "career")`

**What you get:**
- All verbatim quotes from a specific leader
- Their unique philosophy and advice
- Deep-dive into one person's thinking

**Use case:** When you want to learn from a specific leader's experiences and philosophy. Perfect for role models or when you resonate with a particular guest.

---

### 5. **Framework Catalog** (`list_frameworks`)

**What it does:** Browse all frameworks and mental models mentioned across episodes

**Example query:**
- `list_frameworks()`

**What you get:**
- Complete catalog of all frameworks
- Which episodes cover each framework
- Categories: Product Strategy, Decision-Making, Growth, Leadership

**Frameworks included:**
- **Product Strategy:** DHM, Eigenquestions, Pre-mortems
- **Decision-Making:** LNO, Pre-mortems, Hypothesis-Based Coaching
- **Growth:** Black/Blue Loops, Maker Billing
- **Leadership:** Managerial Leverage, Good PM/Bad PM, Personal Operating Principles
- **Company Building:** House Architecture, Explorer Not Lecturer

**Use case:** When you want to explore and apply specific frameworks to your work. Great reference for methodologies used by top PMs.

---

## 📊 Comparison: Before vs After

| Feature | v1.0 (Original) | v2.0 (Enhanced) |
|---------|-----------------|-----------------|
| **Total Tools** | 4 | 9 |
| **Search Capabilities** | Keyword search only | Keyword + Situation + Guest + Framework |
| **Filtering** | Topic-based | Topic + Actionable + Guest + Framework |
| **Analysis** | Single perspective | Multi-perspective comparison |
| **Use Cases** | General search | Specific situations, deep-dives, comparisons |

---

## 🎯 When to Use Each Tool

### For General Discovery:
1. **search_wisdom()** - When you have a topic or keyword
2. **list_guests()** - When browsing available guests
3. **get_episode()** - When you want full episode details
4. **search_by_topic()** - When filtering by specific topics

### For Specific Needs:
5. **get_advice_for_situation()** - When facing a specific challenge
6. **get_actionable_insights()** - When you need tactics, not theory
7. **compare_perspectives()** - When you want multiple viewpoints
8. **get_quotes_by_guest()** - When learning from a specific leader
9. **list_frameworks()** - When exploring methodologies

---

## 🚀 Example Workflows

### Workflow 1: New VP Product Onboarding
```
1. get_advice_for_situation("I'm joining a new company as VP Product")
   → Get specific onboarding advice

2. get_quotes_by_guest("Deb Liu", "onboarding")
   → Deep-dive into Deb's 30/60/90 framework

3. compare_perspectives("leadership", ["Brian Chesky", "Ben Horowitz"])
   → Understand different leadership styles

4. get_actionable_insights("hiring")
   → Tactical hiring advice for building your team
```

### Workflow 2: Growth Strategy Development
```
1. search_wisdom("growth strategy")
   → Broad search for growth insights

2. list_frameworks()
   → Browse available growth frameworks (Black/Blue Loops, etc.)

3. get_episode("ep-shishir-mehrotra")
   → Deep-dive into Black/Blue Loops framework

4. compare_perspectives("growth", ["Casey Winters", "Bangaly Kaba"])
   → Compare different growth philosophies

5. get_actionable_insights("growth-marketing")
   → Specific tactics to implement
```

### Workflow 3: Decision-Making Framework
```
1. get_advice_for_situation("I need to make a high-stakes decision")
   → Get decision-making advice

2. list_frameworks()
   → Browse decision frameworks (LNO, Pre-mortems, etc.)

3. get_quotes_by_guest("Ben Horowitz", "decision-making")
   → Learn Ben's approach to hard decisions

4. get_actionable_insights("decision-making")
   → Specific techniques to apply
```

---

## 💡 Pro Tips

1. **Start with situations, not keywords** - Use `get_advice_for_situation()` instead of generic searches when you have a specific challenge

2. **Use compare_perspectives for trade-offs** - When deciding between approaches, compare how different leaders handle it

3. **Filter for action when in execution mode** - Use `get_actionable_insights()` when you need to ship fast

4. **Deep-dive with specific guests** - Use `get_quotes_by_guest()` to learn from leaders whose style resonates with you

5. **Reference frameworks by name** - Use `list_frameworks()` to find the exact framework you need, then search for it

---

## 🔧 Technical Changes

**Files modified:**
- `lennys_wisdom_server.py` - Added 5 new MCP tools
- `README.md` - Updated documentation with new tools and examples

**New functions:**
1. `list_frameworks()` - Lines added above `get_quotes_by_guest()`
2. `get_quotes_by_guest()` - Lines added above `compare_perspectives()`
3. `compare_perspectives()` - Lines added above `get_actionable_insights()`
4. `get_actionable_insights()` - Lines added above `get_advice_for_situation()`
5. `get_advice_for_situation()` - Lines added above `search_by_topic()`

**Backward compatible:** All original 4 tools still work exactly as before

---

## ✅ Next Steps

To use the enhanced MCP server:

1. **Restart Claude Desktop** (if already configured)
   - Quit and reopen Claude Desktop
   - The new tools will be automatically available

2. **Try the new tools:**
   - "I'm starting a new PM role, what should I do?" → Situation-based advice
   - "Show me actionable insights about hiring" → Filtered tactics
   - "Compare Brian Chesky and Ben Horowitz on leadership" → Perspectives
   - "What are all of Shreyas Doshi's quotes?" → Guest deep-dive
   - "What frameworks are available?" → Framework catalog

3. **Build workflows:**
   - Combine multiple tools for complex research
   - Use situation → framework → actionable pattern
   - Compare perspectives before making decisions

---

## 📈 Impact

**What this enables:**
- More targeted advice for specific situations
- Faster filtering for actionable vs theoretical content
- Multi-perspective analysis for better decision-making
- Deep-dives into specific leaders' philosophies
- Framework-based learning and application

**Bottom line:** The MCP server went from a basic search tool to a comprehensive PM advisory system powered by 20 world-class product leaders.

---

**Version:** 2.0
**Date:** February 10, 2026
**Total Tools:** 9 (4 original + 5 new)
**Total Insights:** 280+ from 20 episodes
**Status:** ✅ Ready to use
